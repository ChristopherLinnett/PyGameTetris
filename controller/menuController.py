from model.menu.configModel import configModel
from model.menu.highscoreModel import highScoreModel
import controller.gameController as game
from controller.audioController import AudioController
from view.menu.menuScreen import MainMenu
from view.menu.configureScreen import ConfigScreen
from view.menu.topScoreScreen import HighScoreScreen

import pygame

# The MenuController class is a class that controls the menu
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
        """
        The function takes in a value and sets the highName attribute to that value
        
        :param value: The value to be set to the highName variable
        """
        self.highName = value

    def goToConfig(self):
        """
        It creates a new instance of the ConfigScreen class and assigns it to the menu variable
        """
        self.menu = ConfigScreen(self)

    def goToMainMenu(self):
        """
        It sets the volume of the music to 1 if the audio is enabled, otherwise it sets it to 0
        """
        self.audioController.startMenuMusic()
        self.audioController.mixer.music.set_volume(1 if self.config['audioEnabled']== True else 0)
        self.menu = MainMenu(self)
        


    def goToHighScore(self):
        """
        It creates a new instance of the HighScoreScreen class and assigns it to the menu variable.
        """
        self.menu = HighScoreScreen(self)
    def saveHighScore(self):
        """
        It takes a dictionary of high scores, and if the current score is higher than any of the scores
        in the dictionary, it adds the current score to the dictionary, and then saves the dictionary to
        a file
        """
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
        """
        It starts the game music and then starts the game.
        """
        self.audioController.startGameMusic()
        screen = game.GameController(self)

    def setExtendedMode(self, value):
        """
        It sets the extended mode to the value passed in.
        
        :param value: True or False
        """
        self.newConfig['extendedMode'] = value
    
    def setAIMode(self, value):
        """
        The function takes in a value, and sets the value of the key 'aiMode' in the dictionary
        'newConfig' to the value that was passed in
        
        :param value: The value of the parameter
        """
        self.newConfig['aiMode'] = value
    
    def setStartingLevel(self, value):
        """
        It takes a value and sets the startingLevel key in the newConfig dictionary to that value
        
        :param value: The value to set the parameter to
        """
        self.newConfig['startingLevel'] = value
    
    def setPlayWidth(self, value):
        """
        It takes a value and sets the width of the playfield to that value
        
        :param value: The value that the user has entered into the textbox
        """
        self.newConfig['playfieldSize']['width'] = value
    
    def setPlayHeight(self, value):
        """
        It takes a value, and sets the height of the playfield to that value
        
        :param value: The value to set the parameter to
        """
        self.newConfig['playfieldSize']['height'] = value
    
    def setAudioEnabled(self, value):
        """
        If the audio is enabled, set the volume to 1. If the audio is disabled, set the volume to 0
        
        :param value: True or False
        """
        self.newConfig['audioEnabled'] = value
        self.audioController.mixer.music.set_volume(0 if self.newConfig['audioEnabled']== False else 1)

    
    def saveNewConfig(self):
        """
        It saves the new config to the database.
        """
        self.configModel.saveConfig(self.newConfig)