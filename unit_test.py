from unittest import TestCase, TextTestRunner, TestSuite, TestLoader, main
from controller.menuController import MenuController
from sys import argv
from threading import Timer
from model.menu.configModel import configModel
from model.menu.highscoreModel import highScoreModel
import controller.gameController as game
from controller.audioController import AudioController
from view.menu.menuScreen import MainMenu
from view.menu.configureScreen import ConfigScreen
from view.menu.topScoreScreen import HighScoreScreen
import pygame

def custominit(self):
    pygame.init()
    self.audioController = AudioController()
    # self.audioController.startMenuMusic()
    self.configModel = configModel()
    self.highScoreModel = highScoreModel()
    self.highScores = self.highScoreModel.getHighScores()
    self.tempHighScore = 0
    self.highName = ''
    self.config = self.configModel.getConfig()
    self.audioController.mixer.music.set_volume(1 if self.config['audioEnabled']== True else 0)
    self.newConfig = self.configModel.getConfig()
    # self.surface = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
    # self.menu = MainMenu(self)
    pass

# Menu test
class MyTests(TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTests, self).__init__(*args, **kwargs)
        self.game = MenuController.__new__(MenuController)
        custominit(self.game)
    # F-REQ2
    def test_one_REQ2(self):
        # print("This is Test one")
        self.assertIsInstance(self.game, MenuController);
    
    def test_two_REQ3(self):
        self.game.modifyHighName("Duwon")
        # print("This is Test two")
        self.assertEqual(self.game.highName, "Duwon")

if __name__ == '__main__':  
    main()
    # main.testLoadr();