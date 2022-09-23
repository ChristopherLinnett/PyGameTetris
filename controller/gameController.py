import view.menu.menuScreen as menuScreen
import sys
from tkinter import *
from tkinter import messagebox
from model.game.tetronomo import Tetronomo
import model.game.shapesData as sd
from model.game.grid import PlayField
import view.menu.topScoreScreen as topScoreScreen

import pygame
import random

class GameController():
    def __init__(self, controller):
            pygame.font.init()
            self.controller = controller
            self.surface = controller.surface
            self.s_width = controller.config['screenSize']['width']
            self.s_height = controller.config['screenSize']['height']
            self.play_width = 300  # meaning 300 // 10 = 30 width per block
            self.play_height = 600  # meaning 600 // 20 = 20 height per block
            self.block_size = (self.play_width if (self.play_width<self.play_height) else self.play_height)//10
            self.top_left_x = (self.s_width - self.play_width)//2
            self.top_left_y = self.s_height - self.play_height
            self.score = 0
            self.playField = PlayField()
            self.tetroLanded = False
            self.run = True
            self.mainTetronomo = Tetronomo(5,0,random.choice(sd.shapes))
            self.nextTetronomo = Tetronomo(5,0,random.choice(sd.shapes))
            self.clock = pygame.time.Clock()
            self.fallTime = 0
            self.fallSpeed = 0.27
            self.pause = False
            self.win = pygame.display.set_mode((self.s_width, self.s_height))
            pygame.display.set_caption('Tetris')
            self.startGame()  # start game

    def showPopUpBox(self):
        boxResponse = messagebox.askyesno(title="Exit Game?",message="Are you sure you want to quit")
        if boxResponse == True:
            menuScreen.MainMenu(self.controller)

    def freeSpace(self):
        accepted_pos = [[(j,i) for j in range(10) if self.playField.grid[i][j]== (0,0,0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]
        formatted = self.mainTetronomo.rotate()
        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True

    def loseCondition(self):
        for pos in self.playField.locked_positions:
            x,y = pos
            if y < 1:
                return True
        return False
    
    def drawPlayField(self):
        sx = self.top_left_x
        sy = self.top_left_y

        for i in range(len(self.playField.grid)):
            pygame.draw.line(self.surface, (128,128,128), (sx, sy+i*self.block_size), (sx+self.play_width, sy+i*self.block_size))
            for j in range(len(self.playField.grid[i])+1):
                pygame.draw.line(self.surface, (128,128,128), (sx+j*self.block_size, sy), (sx+j*self.block_size, sy+self.play_height))


    def drawNextTetronomo(self,tetronomo):
        font = pygame.font.SysFont('arial', 30)
        label = font.render("Next Shape", 1, (255,255,255))

        sx = self.top_left_x + self.play_width +50
        sy = self.top_left_y + self.play_height/2-100
        format = tetronomo.shape[tetronomo.rotation % len(tetronomo.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(self.surface, tetronomo.colour, (sx+j*self.block_size, sy+i*self.block_size, self.block_size, self.block_size),0)
        self.surface.blit(label, (sx+10, sy-30))

    def drawWindow(self, playField):
        self.surface.fill((0,0,0))
        pygame.font.init()
        font = pygame.font.SysFont('arial', 60)
        menuFont = pygame.font.SysFont('arial', 24)

        fontLabel = font.render('Tetris', 1, (255,255,255))
        label2 = menuFont.render('Group: 10', 1, (255,255,255))
        scoreLabel = menuFont.render(f'Score: {self.score}', 1, (255,255,255))
        levelLabel = menuFont.render('Level: 1', 1, (255,255,255))
        modeLabel = menuFont.render('Mode: Player', 1, (255,255,255))

        self.surface.blit(fontLabel, (0+self.s_width//2 - fontLabel.get_width()//2, 30))
        self.surface.blit(label2, (0, 15))
        self.surface.blit(scoreLabel, (0+self.s_width - scoreLabel.get_width(), 15))
        self.surface.blit(levelLabel, (0+self.s_width *4/5 - levelLabel.get_width(), 15))
        self.surface.blit(modeLabel, (self.s_width*1/5, 15))

        for i in range(len(playField)):
            for j in range(len(playField[i])):
                pygame.draw.rect(self.surface, playField[i][j], (self.top_left_x+j*self.block_size, self.top_left_y+i*self.block_size, self.block_size, self.block_size), 0) #Draw blocks

        self.drawPlayField()
        


    def startGame(self):
        while self.run:
            self.playField.update()
            if self.pause == False:
                self.fallTime += self.clock.get_rawtime() 
                self.clock.tick()

            if self.fallTime/1000 > self.fallSpeed:
                self.fallTime = 0
                self.mainTetronomo.y += 1
                if not(self.freeSpace()) and self.mainTetronomo.y > 0:
                    self.mainTetronomo.y -= 1
                    self.tetroLanded = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.pause == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.mainTetronomo.x -= 1
                            if not(self.freeSpace()):
                                self.mainTetronomo.x+=1
                        if event.key == pygame.K_RIGHT:
                            self.mainTetronomo.x += 1
                            if not(self.freeSpace()):
                                self.mainTetronomo.x-=1
                        if event.key == pygame.K_DOWN:
                            self.mainTetronomo.y += 1
                            if not(self.freeSpace()):
                                self.mainTetronomo.y-=1
                        if event.key == pygame.K_UP:
                            self.mainTetronomo.rotation += 1
                            if not(self.freeSpace()):
                                self.mainTetronomo.rotation-=1
                        if event.key == pygame.K_ESCAPE:
                            self.pause = True
                            self.showPopUpBox()
                            self.pause = False  
                        if event.key == pygame.K_p:
                            self.pause = True
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.pause = False

                        
            tetroRotationState = self.mainTetronomo.rotate()
            for i in range(len(tetroRotationState)):
                x,y = tetroRotationState[i]
                if y > -1:
                    self.playField.grid[y][x] = self.mainTetronomo.colour

            if self.tetroLanded:
                global score
                for pos in tetroRotationState:
                    p = (pos[0], pos[1])
                    self.playField.locked_positions[p] = self.mainTetronomo.colour
                self.mainTetronomo = self.nextTetronomo
                self.nextTetronomo = Tetronomo(5,0,random.choice(sd.shapes))
                self.tetroLanded = False
                clearedRows = self.playField.clearRows()
                self.score += 50*clearedRows**2+50*clearedRows
                
                
            self.drawWindow(self.playField.grid)
            self.drawNextTetronomo(self.nextTetronomo)
            pygame.display.update()

            if self.loseCondition():
                run = False
        topScoreScreen.HighScoreScreen(self.controller)

  