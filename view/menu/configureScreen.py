import pygame_menu
class MenuScreen:
    def __init__(self, surface, controller):

        self.menuController = controller
        self.surface = surface

        self.configMenu = pygame_menu.Menu(title='Settings', width=surface.get_width(), height=surface.get_height())
        widthInput = self.configMenu.add.text_input(title="Play Width: ", input_type='input-int', maxchar=4, onchange=self.menuController.setPlayWidth)
        widthInput.set_value(self.menuController.config['screenSize']['width'])

        heightInput = self.configMenu.add.text_input(title="Play Height: ", input_type='input-int', maxchar=4, onchange=self.menuController.setPlayHeight)
        heightInput.set_value(self.menuController.config['screenSize']['height'])

        startingLevelInput = self.configMenu.add.range_slider(title="Starting Level", increment=1,default=1, range_values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),range_text_value_enabled=False, onchange=self.menuController.setStartingLevel)
        startingLevelInput.set_value(self.menuController.config['startingLevel'])

        extendedModeInput = self.configMenu.add.toggle_switch(title='Extended Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=self.menuController.setExtendedMode)
        extendedModeInput.set_default_value(self.menuController.config['extendedMode'])

        aiModeInput = self.configMenu.add.toggle_switch(title='AI Mode', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=self.menuController.setAIMode)
        aiModeInput.set_default_value(self.menuController.config['aiMode'])

        audioInput= self.configMenu.add.toggle_switch(title='Audio', state_values=tuple((False, True)), state_text=tuple(("Off", "On")), onchange=self.menuController.setAudioEnabled)
        audioInput.set_default_value(self.menuController.config['audioEnabled'])

        self.configMenu.add.label(" ")
        self.configMenu.add.button("Save", self.menuController.saveNewConfig)
        self.configMenu.add.button('Back', pygame_menu.events.BACK)