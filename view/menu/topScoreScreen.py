import pygame
import pygame_menu
import view.menu.menuScreen as menuScreen
import controller.menu.highscoreController as highscore
import controller.menu.menuController as menuController



def showTopScores():
    topScores = highscore.getHighscores()
    config = menuController.getConfig()
    pygame.init()
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))

    def goBack():
        menuScreen.gameLaunched()

    menu = pygame_menu.Menu(title='High Scores', width=surface.get_width(), height=surface.get_height())
    names = list(topScores.keys())
    for user in names:
        menu.add.label(f'{names.index(user)+1}    {user}       {topScores[user]}')
    menu.add.label(" ")
    menu.add.button('Back', goBack)
    menu.mainloop(surface)