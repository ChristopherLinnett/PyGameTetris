from model.menu.configModel import configModel
from model.menu.highscoreModel import highScoreModel
import controller.gameController as game
from controller.audioController import AudioController
from view.menu.menuScreen import MainMenu
from view.menu.configureScreen import ConfigScreen
from view.menu.topScoreScreen import HighScoreScreen

import pygame

class MenuController:
    def __init__(self):
        pygame.init()
        self.audioController = AudioController()
        self.audioController.startMenuMusic()
        self.configModel = configModel()
        self.highScoreModel = highScoreModel()
        self.highScores = self.highScoreModel.getHighScores()
        self.tempHighScore = 0
        self.highName = ''
        self.config = self.configModel.getConfig()
        self.audioController.mixer.music.set_volume(1 if self.config['audioEnabled']== True else 0)
        self.newConfig = self.configModel.getConfig()
        self.surface = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
        self.menu = MainMenu(self)

    def modifyHighName(self, value):
        self.highName = value

    def goToConfig(self):
        self.menu = ConfigScreen(self)

    def goToMainMenu(self):
        self.audioController.startMenuMusic()
        self.audioController.mixer.music.set_volume(1 if self.config['audioEnabled']== True else 0)
        self.menu = MainMenu(self)
        


    def goToHighScore(self):
        self.menu = HighScoreScreen(self)
    def saveHighScore(self):
        userList = list(self.highScores.keys())
        scoreList = list(self.highScores.values())
        newHighScores = {}
        for scoreInd in range(0,len(scoreList)):
                if self.tempHighScore > int(scoreList[scoreInd]):
                    newHighScores[self.highName] = self.tempHighScore
                    self.highName = ''
                    self.tempHighScore = 0
                if len(list(newHighScores.keys())) < 10:
                    newHighScores[userList[scoreInd]] = scoreList[scoreInd]
        self.highScoreModel.saveHighScores(newHighScores)
        print('saved High Scores')
        self.highScores = self.highScoreModel.getHighScores()
        self.audioController.playSound('saveHighScoreSound')
        self.goToHighScore()
        

    def startTheGame(self):
        self.audioController.startGameMusic()
        screen = game.GameController(self)

    def setExtendedMode(self, value):
        self.newConfig['extendedMode'] = value
    
    def setAIMode(self, value):
        self.newConfig['aiMode'] = value
    
    def setStartingLevel(self, value):
        self.newConfig['startingLevel'] = value
    
    def setPlayWidth(self, value):
        self.newConfig['playfieldSize']['width'] = value
    
    def setPlayHeight(self, value):
        self.newConfig['playfieldSize']['height'] = value
    
    def setAudioEnabled(self, value):
        self.newConfig['audioEnabled'] = value
        self.audioController.mixer.music.set_volume(0 if self.newConfig['audioEnabled']== False else 1)

    
    def saveNewConfig(self):
        self.configModel.saveConfig(self.newConfig)