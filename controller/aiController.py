import pygame
import time
from model.game.tetronomo import Tetronomo

class Event:
    type = None
    key = None

    def __init__(self, type, key):
        self.type = type
        self.key = key
        self.counter = 0

class AIController:
    def __init__(self, controller, width, height):
        self.controller = controller
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.width = width
        self.height = height

    def createGhost(self,x, y, shape, rotation):
        self.ghostTetro = Tetronomo(0, 0)
        self.ghostTetro.shape = shape
        self.ghostTetro.rotation = rotation
        self.bestOutput = self.testPaths()
        self.run_ai()



    def freeSpace(self):
            """
            It checks if the current tetronomo can move down one space
            :return: a boolean value.
            """
            emptySpaces = [
                [(j, i) for j in range(self.width) if self.controller.playField.grid[i][j] == (0, 0, 0)]
                for i in range(self.height)
            ]
            emptySpaces = [j for sub in emptySpaces for j in sub]
            formatted = self.ghostTetro.rotate()
            for pos in formatted:
                if pos not in emptySpaces:
                    if pos[1] > -1:
                        return False
            return True
    
    def testPaths(self):
        bestScore = 0
        for num in range(self.width):
            self.ghostTetro.x = num
            self.ghostTetro.y = 0
            if self.freeSpace():
                for num in range(len(self.ghostTetro.shape)):

                    self.ghostTetro.rotation = num
                    if self.freeSpace():
                        while self.freeSpace():
                            self.ghostTetro.y+=1
                        self.ghostTetro.y-=1
                        # for i in range(len(self.controller.playField.grid) - 1, -1, -1):
                        #     row = self.controller.playField.grid[i]
                        #     if (0, 0, 0) not in row:
                        #         return self.ghostTetro.x, self.ghostTetro.rotation
                        if self.ghostTetro.y > bestScore:
                            bestScore = self.ghostTetro.y
                            xGoal = self.ghostTetro.x
                            rotationGoal = self.ghostTetro.rotation

        return xGoal,rotationGoal

    def run_ai(self):
        while self.controller.mainTetronomo.x != self.bestOutput[0] or self.controller.mainTetronomo.rotation != self.bestOutput[1]:
            if (self.controller.mainTetronomo.x < self.bestOutput[0]):
                self.controller.mainTetronomo.x +=1
            elif (self.controller.mainTetronomo.x > self.bestOutput[0]):
                self.controller.mainTetronomo.x -=1
            elif (self.controller.mainTetronomo.rotation != self.bestOutput[1]):
                self.controller.mainTetronomo.rotation+=1


