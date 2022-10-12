import pygame_menu

# A class that is used to create a screen that will be used to configure the program.
class ConfigScreen:
    def __init__(self, controller):
        
        self.menu = pygame_menu.Menu(title='Settings', width=controller.surface.get_width(), height=controller.surface.get_height(), theme=pygame_menu.themes.THEME_DARK)
        widthInput = self.menu.add.text_input(title="Playfield Width: ", input_type='input-int', maxchar=2, onchange=controller.setPlayWidth)
        widthInput.set_value(controller.config['playfieldSize']['width'])
        
        heightInput = self.menu.add.text_input(title="Playfield Height: ", input_type='input-int', maxchar=2, onchange=controller.setPlayHeight)
        heightInput.set_value(controller.config['playfieldSize']['height'])

        startingLevelInput = self.menu.add.range_slider(title="Starting Level", increment=1,default=1, range_values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),range_text_value_enabled=False, onchange=controller.setStartingLevel)
        startingLevelInput.set_value(controller.config['startingLevel'])

        extendedModeInput = self.menu.add.toggle_switch(title='Extended Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=controller.setExtendedMode)
        extendedModeInput.set_default_value(controller.config['extendedMode'])

        aiModeInput = self.menu.add.toggle_switch(title='AI Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=controller.setAIMode)
        aiModeInput.set_default_value(controller.config['aiMode'])

        audioInput= self.menu.add.toggle_switch(title='Audio', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=controller.setAudioEnabled)
        audioInput.set_default_value(controller.config['audioEnabled'])

        self.menu.add.label(" ")
        self.menu.add.button("Save", controller.saveNewConfig)
        self.menu.add.button('Back', controller.goToMainMenu)

        self.menu.mainloop(controller.surface)