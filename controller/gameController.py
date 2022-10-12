import sys
from model.game.tetronomoFactory import TetronomoFactory
import model.game.shapesData as sd
from model.game.grid import PlayField
import view.menu.topScoreScreen as topScoreScreen
from view.game.gameView import GameView
from controller.playerController import playerController
import pygame
import random
import controller.aiController as aiController


# The GameController class is responsible for managing the game state and the game loop
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
        self.aiMode = controller.config['aiMode']
        self.ai = aiController.AIController(self, self.width, self.height)

        self.gameView = GameView(self, pygame, controller.surface, self.width, self.height)
        self.playField = PlayField(self.width,self.height)
        self.tetroLanded = False
        self.run = True
        self.totalClearedRows = 0
        self.mainTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
        self.nextTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
        self.clock = pygame.time.Clock()
        self.fallTime = 0
        self.fallSpeed = 0.3/(1+(.5*(self.level-1)))
        self.pause = False
        self.startGame()  # start game

    def freeSpace(self):
        """
        It checks if the current tetronomo can move down one space
        :return: a boolean value.
        """
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
        """
        If any of the filled positions are in the top row, return True
        :return: The position of the block that is at the top of the playfield.
        """
        for pos in self.playField.filledPositions:
            x, y = pos
            if y < 0:
                return True
        return False

    def startGame(self):
        """
        It's a game loop that runs the tetris game until the player loses
        """
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
            for event in list(pygame.event.get()):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if  self.pause == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            self.controller.audioController.mixer.music.set_volume(0 if float(self.controller.audioController.mixer.music.get_volume()) > 0 else 1)
                        if event.key == pygame.K_ESCAPE:
                            self.pause = True
                            self.gameView.showPopUpBox()
                            self.pause = False
                        if event.key == pygame.K_p:
                            self.pause = True
                            self.controller.audioController.playSound('pauseGameSound')
                            self.controller.audioController.pauseMusic()
                        if self.aiMode == False:
                            playerController(self, event, pygame)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.controller.audioController.playSound('pauseGameSound')
                            self.controller.audioController.resumeMusic()
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
                if self.aiMode == True:
                    self.ai.createGhost(self.mainTetronomo.x, self.mainTetronomo.y, self.mainTetronomo.shape, self.mainTetronomo.rotation)
                self.nextTetronomo = TetronomoFactory.createTetronomo(self.width//2, 0, random.choice(self.possibleShapes))
                self.tetroLanded = False
                clearedRows = self.playField.clearRows()
                self.totalClearedRows+=clearedRows
                if clearedRows != 0:
                    self.controller.audioController.playSound('clearRowSound')
                else:
                    self.controller.audioController.playSound('brickDroppedSound')

                self.score += 50 * clearedRows**2 + 50 * clearedRows
                if self.score >= self.level*500:
                    self.level+=1
                    self.fallSpeed = 0.3/(1+(.095*(self.level-1)))
                    self.controller.audioController.playSound('levelUpSound')

            self.gameView.drawWindow(self.playField.grid)
            self.gameView.drawNextTetronomo(self.nextTetronomo)
            pygame.display.update()


            if self.loseCondition():
                self.run = False
        self.controller.audioController.playSound('endGameSound')
        self.controller.audioController.startMenuMusic()
        topScoreScreen.HighScoreScreen(self.controller, score=self.score)
