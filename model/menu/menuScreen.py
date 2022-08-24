import pygame
import pygame_menu
import model.game.gameScreen as gameScreen
import model.menu.configureScreen as configureScreen
import model.menu.topScoreScreen as highScoreScreen
import json



def gameLaunched():
    f = open('config.json')
    config = json.load(f)
    pygame.init()
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))

    def showSettings():
        configureScreen.showConfigScreen()

    def start_the_game():
        gameScreen.loop()

    def showHighScores():
        highScoreScreen.showTopScores()

    menu = pygame_menu.Menu(title='2022 3815ICT', width=surface.get_width(), height=surface.get_height())
    menu.add.image(image_path="assets/tetrisTitle.png",scale=(0.2,0.2))
    menu.add.button('Play', start_the_game)
    menu.add.button('High Scores', showHighScores)
    menu.add.button('Settings', showSettings)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.add.label(title="Christopher Linnett, Lachlan Manson, Duwon Ha")
    menu.mainloop(surface)