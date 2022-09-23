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
        self.gameView = GameView(self, pygame, controller.surface)
        self.controller = controller
        self.score = 0
        self.playField = PlayField()
        self.tetroLanded = False
        self.run = True
        self.mainTetronomo = TetronomoFactory.createTetronomo(5, 0, random.choice(sd.shapes))
        self.nextTetronomo = TetronomoFactory.createTetronomo(5, 0, random.choice(sd.shapes))
        self.clock = pygame.time.Clock()
        self.fallTime = 0
        self.fallSpeed = 0.2
        self.pause = False
        self.startGame()  # start game

    def freeSpace(self):
        emptySpaces = [
            [(j, i) for j in range(10) if self.playField.grid[i][j] == (0, 0, 0)]
            for i in range(20)
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
                global score
                for pos in tetroRotationState:
                    p = (pos[0], pos[1])
                    self.playField.filledPositions[p] = self.mainTetronomo.colour
                self.mainTetronomo = self.nextTetronomo
                self.nextTetronomo = TetronomoFactory.createTetronomo(5, 0, random.choice(sd.shapes))
                self.tetroLanded = False
                clearedRows = self.playField.clearRows()
                self.score += 50 * clearedRows**2 + 50 * clearedRows
            self.gameView.drawWindow(self.playField.grid)
            self.gameView.drawNextTetronomo(self.nextTetronomo)
            pygame.display.update()

            if self.loseCondition():
                self.run = False
        topScoreScreen.HighScoreScreen(self.controller)
