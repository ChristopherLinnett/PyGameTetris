import model.menu.configModel as configModel
import pygame_menu
import pygame

class menuController:
    def __init__(self):
        self.config = configModel.config
        pygame.init()
        self.surface = pygame.display.set_mode((self.config['screenSize']['width'], self.config['screenSize']['height']))

    def back(screen):
        screen.gameLaunched()

    def setExtendedMode(self, value):
        self.config['extendedMode'] = value

    def setAIMode(self, value):
        self.config['aiMode'] = value

    def setStartingLevel(self, value):
        self.config['startingLevel'] = value

    def setPlayWidth(self, value):
        self.config['screenSize']['width'] = value

    def setPlayHeight(self, value):
        self.config['screenSize']['height'] = value

    def setAudioEnabled(self, value):
        self.config['audioEnabled'] = value

    def saveNewConfig(self):
        configModel.saveConfig(self.config)
        
