from model.menu.configModel import configModel
from model.menu.highscoreModel import highscoreModel
import controller.gameController as game

from view.menu.menuScreen import MainMenu
from view.menu.configureScreen import ConfigScreen
from view.menu.topScoreScreen import HighScoreScreen

import pygame

class MenuController:
    def __init__(self):
        pygame.init()
        self.configModel = configModel()
        self.highscoreModel = highscoreModel()
        self.highScores = self.highscoreModel.getHighScores()
        self.config = self.configModel.getConfig()
        self.newConfig = self.configModel.getConfig()
        self.surface = pygame.display.set_mode((self.config['screenSize']['width'], self.config['screenSize']['height']),pygame.RESIZABLE)
        self.menu = MainMenu(self)

    def goToConfig(self):
        self.menu = ConfigScreen(self)

    def goToMainMenu(self):
        self.menu = MainMenu(self)

    def goToHighScore(self):
        self.menu = HighScoreScreen(self)

    def startTheGame(self):
        screen = game.GameController(self)

    def setExtendedMode(self, value):
        self.newConfig['extendedMode'] = value
    
    def setAIMode(self, value):
        self.newConfig['aiMode'] = value
    
    def setStartingLevel(self, value):
        self.newConfig['startingLevel'] = value
    
    def setPlayWidth(self, value):
        self.newConfig['screenSize']['width'] = value
    
    def setPlayHeight(self, value):
        self.newConfig['screenSize']['height'] = value
    
    def setAudioEnabled(self, value):
        self.newConfig['audioEnabled'] = value
    
    def saveNewConfig(self):
        self.configModel.saveConfig(self.newConfig)
        self.surface = pygame.display.set_mode((self.newConfig['screenSize']['width'], self.newConfig['screenSize']['height']))

    def setStartingLevel(self):
        pass