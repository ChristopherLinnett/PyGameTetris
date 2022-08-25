from email.mime import audio
import pygame
import pygame_menu
import json
import model.menu.menuScreen as menuScreen


def showConfigScreen():
    with open('config.json') as f:
        config = json.load(f)
    pygame.init()
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))
    screenWidth = config['screenSize']['width']
    screenHeight = config['screenSize']['height']
    aiMode = config['aiMode']
    extendedMode = config['extendedMode']
    audioEnabled = config['audioEnabled']

    def changeScreenSlider(newValue):
        pass

    def back():
        menuScreen.gameLaunched()
 

    def saveChanges():
        newConfig = { "screenSize": {"width": int(int(config['screenSize']['width'])*0.9), "height": int(int(config['screenSize']['height'])*0.9)},
            "extendedMode": extendedMode, 
            "audioEnabled": audioEnabled,
            "aiMode": aiMode }

        with open('config.json', 'w') as file:
            json.dump(newConfig, file)
        showConfigScreen()

        

    menu = pygame_menu.Menu(title='Main Menu', width=surface.get_width(), height=surface.get_height())
    # Adding a slider to the menu.
    menu.add.label("Screen Width")
    menu.add.label("Screen Height")

    menu.add.range_slider(title="Starting Level", increment=1,default=1, range_values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    menu.add.label("Normal/Extended")
    menu.add.label("Player/AI")
    menu.add.label(" ")
    menu.add.button("Apply", saveChanges)
    menu.add.button('Back', back)

    menu.mainloop(surface)