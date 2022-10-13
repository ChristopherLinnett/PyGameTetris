from unittest import TestCase, main
from controller.menuController import MenuController
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
    pass

# Menu test
class MyTests(TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTests, self).__init__(*args, **kwargs)
        self.game = MenuController.__new__(MenuController)
        custominit(self.game)
    # F-REQ2, F-REQ3, F-REQ4, F-REQ5, F-REQ6, F-REQ7, F-REQ8, F-REQ9, 
    # F-REQ10, F-REQ11, F-REQ12, F-REQ13
    def test_one(self):
        self.assertIsInstance(self.game, MenuController);
    
    # F-REQ9,F-REQ38
    def test_two(self):
        self.game.modifyHighName("Duwon")
        self.assertEqual(self.game.highName, "Duwon")

    # Extended mode
    def test_three(self):
        self.game.setExtendedMode(True)
        self.assertEqual(self.game.newConfig['extendedMode'],True)

    # Set AI mode
    def test_four(self):
        self.game.setAIMode(True)
        self.assertEqual(self.game.newConfig['aiMode'],True)    
    
    # Set Starting Level
    def test_five(self):
        self.game.setStartingLevel(2)
        self.assertEqual(self.game.newConfig['startingLevel'],2)

    # Set Playfield width
    def test_six(self):
        self.game.setPlayWidth(10)
        self.assertEqual(self.game.newConfig['playfieldSize']['width'],10)

    # Set Playfield height
    def test_seven(self):
        self.game.setPlayHeight(20)
        self.assertEqual(self.game.newConfig['playfieldSize']['height'],20)

    # Set AudioEnabled
    def test_eight(self):
        self.game.setAudioEnabled(1)
        self.assertEqual(self.game.newConfig['audioEnabled'],1)

    # Checks ConfigScreen Instance Created or Not
    def test_nine(self):
        self.menu = ConfigScreen.__new__(ConfigScreen)
        self.assertIsInstance(self.menu, ConfigScreen)


    # Checks MainMenu Instance Created or Not
    def test_ten(self):
        self.menu = MainMenu.__new__(MainMenu)
        self.assertIsInstance(self.menu, MainMenu)


    # Checks ConfigScreen Instance Created or Not
    def test_eleven(self):
        self.menu = ConfigScreen.__new__(ConfigScreen)
        self.assertIsInstance(self.menu, ConfigScreen)        

    # Checks HighScoreScreen Instance Created or Not
    def test_twelve(self):
        self.menu = HighScoreScreen.__new__(HighScoreScreen)
        self.assertIsInstance(self.menu, HighScoreScreen)  


if __name__ == '__main__':  
    main()
    # main.testLoadr();


    
