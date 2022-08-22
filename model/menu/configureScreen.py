import pygame
import pygame_menu
import json
import model.menu.menuScreen as menuScreen

f = open('config.json')
config = json.load(f)
def showConfigScreen():
    pygame.init()
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))

    def changeScreenSlider(newValue):
        pass

    def back():
        menuScreen.gameLaunched()
 

    def showHighScores():
        pass

    menu = pygame_menu.Menu(title='Main Menu', width=surface.get_width(), height=surface.get_height())
    # Adding a slider to the menu.
    menu.add.range_slider(title="Screen Size",increment=0.05, range_values=(0.2,1.8), default=1, onchange=changeScreenSlider)
    menu.add.button('High Scores', showHighScores)
    menu.add.button('Back', back)

    menu.mainloop(surface)