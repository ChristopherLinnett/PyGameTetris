import pygame
import pygame_menu
import view.menu.menuScreen as menuScreen
import controller.menu.menuController as menuController


def showConfigScreen():
    pygame.init()
    config = menuController.getConfig()
    newConfig = config
    surface = pygame.display.set_mode((config['screenSize']['width'], config['screenSize']['height']))

    def back():
        menuScreen.gameLaunched()

    def setExtendedMode(value):
        newConfig['extendedMode'] = value
    
    def setAIMode(value):
        newConfig['aiMode'] = value
    
    def setPlayWidth(value):
        newConfig['screenSize']['width'] = value
    
    def setPlayHeight(value):
        newConfig['screenSize']['height'] = value
    
    def setAudioEnabled(value):
        newConfig['audioEnabled'] = value
    
    def saveNewConfig():
        menuController.saveConfig(newConfig)
        showConfigScreen()

    menu = pygame_menu.Menu(title='Settings', width=surface.get_width(), height=surface.get_height())
    widthInput = menu.add.text_input(title="Play Width: ", input_type='input-int', maxchar=4, onchange=setPlayWidth)
    widthInput.set_value(config['screenSize']['width'])
    
    heightInput = menu.add.text_input(title="Play Height: ", input_type='input-int', maxchar=4, onchange=setPlayHeight)
    heightInput.set_value(config['screenSize']['height'])

    menu.add.range_slider(title="Starting Level", increment=1,default=1, range_values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),range_text_value_enabled=False,)

    extendedModeInput = menu.add.toggle_switch(title='Extended Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=setExtendedMode)
    extendedModeInput.set_default_value(config['extendedMode'])

    aiModeInput = menu.add.toggle_switch(title='AI Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=setAIMode)
    aiModeInput.set_default_value(config['aiMode'])

    audioInput= menu.add.toggle_switch(title='Audio', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=setAudioEnabled)
    audioInput.set_default_value(config['audioEnabled'])

    menu.add.label(" ")
    menu.add.button("Save", saveNewConfig)
    menu.add.button('Back', back)

    menu.mainloop(surface)