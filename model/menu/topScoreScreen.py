import pygame
import pygame_menu
import model.menu.menuScreen as menuScreen
import json



def showTopScores():
    scores = open('highscores.json')
    with open('config.json') as f:
        config = json.load(f)
    topScores = json.load(scores)
    pygame.init()
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))

    def goBack():
        menuScreen.gameLaunched()

    menu = pygame_menu.Menu(title='High Scores', width=surface.get_width(), height=surface.get_height())
    names = topScores.keys()
    for user in names:
        menu.add.label(f'{user}       {topScores[user]}')
    menu.add.label(" ")
    menu.add.button('Back', goBack)
    menu.mainloop(surface)