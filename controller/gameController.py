import sys
from model.game.tetronomoFactory import TetronomoFactory
import model.game.shapesData as sd
from model.game.grid import PlayField
import view.menu.topScoreScreen as topScoreScreen
from view.game.gameView import GameView

import pygame
import random


class GameController:
    def __init__(self, controller):
        pygame.font.init()
        self.controller = controller
        self.extendedMode = controller.config['extendedMode']
        self.possibleShapes = sd.shapes if not self.extendedMode else sd.shapes+sd.extendedShapes
        self.score = 0
        self.level = int(controller.config['startingLevel'])
        self.width = int(controller.config['playfieldSize']['width']) if int(controller.config['playfieldSize']['width']) > 7 else 7
        self.height = int(controller.config['playfieldSize']['height']) if int(controller.config['playfieldSize']['height']) > 10 else 10
        self.gameView = GameView(self, pygame, controller.surface, self.width, self.height)
        self.playField = PlayField(self.width,self.height)
        self.tetroLanded = False
        self.run = True
        self.mainTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
        self.nextTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
        self.clock = pygame.time.Clock()
        self.fallTime = 0
        self.fallSpeed = 0.3/(1+(.5*(self.level-1)))
        self.pause = False
        self.startGame()  # start game

    def freeSpace(self):
        emptySpaces = [
            [(j, i) for j in range(self.width) if self.playField.grid[i][j] == (0, 0, 0)]
            for i in range(self.height)
        ]
        emptySpaces = [j for sub in emptySpaces for j in sub]
        formatted = self.mainTetronomo.rotate()
        for pos in formatted:
            if pos not in emptySpaces:
                if pos[1] > -1:
                    return False
        return True

    def loseCondition(self):
        for pos in self.playField.filledPositions:
            x, y = pos
            if y < 1:
                print(pos)
                return True
        return False

    def startGame(self):
        while self.run:
            self.playField.update()
            if self.pause == False:
                self.fallTime += self.clock.get_rawtime()
                self.clock.tick()

            if self.fallTime / 1000 > self.fallSpeed:
                self.fallTime = 0
                self.mainTetronomo.y += 1
                if not (self.freeSpace()) and self.mainTetronomo.y > 0:
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
                            if not (self.freeSpace()):
                                self.mainTetronomo.x += 1
                        if event.key == pygame.K_RIGHT:
                            self.mainTetronomo.x += 1
                            if not (self.freeSpace()):
                                self.mainTetronomo.x -= 1
                        if event.key == pygame.K_DOWN:
                            self.mainTetronomo.y += 1
                            if not (self.freeSpace()):
                                self.mainTetronomo.y -= 1
                        if event.key == pygame.K_UP:
                            self.mainTetronomo.rotation += 1
                            if not (self.freeSpace()):
                                self.mainTetronomo.rotation -= 1
                        if event.key == pygame.K_ESCAPE:
                            self.pause = True
                            self.gameView.showPopUpBox()
                            self.pause = False
                        if event.key == pygame.K_p:
                            self.pause = True
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.pause = False

            tetroRotationState = self.mainTetronomo.rotate()
            for i in range(len(tetroRotationState)):
                x, y = tetroRotationState[i]
                if y > -1:
                    self.playField.grid[y][x] = self.mainTetronomo.colour

            if self.tetroLanded:
                for pos in tetroRotationState:
                    p = (pos[0], pos[1])
                    self.playField.filledPositions[p] = self.mainTetronomo.colour
                self.mainTetronomo = self.nextTetronomo
                self.nextTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
                self.tetroLanded = False
                clearedRows = self.playField.clearRows()
                self.score += 50 * clearedRows**2 + 50 * clearedRows
                if self.score >= self.level*500:
                    self.level+=1
                    self.fallSpeed = 0.3/(1+(.095*(self.level-1)))

            self.gameView.drawWindow(self.playField.grid)
            self.gameView.drawNextTetronomo(self.nextTetronomo)
            pygame.display.update()


            if self.loseCondition():
                self.run = False
                topScoreScreen.HighScoreScreen(self.controller)
