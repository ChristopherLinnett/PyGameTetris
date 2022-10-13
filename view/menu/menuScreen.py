import pygame_menu


# It creates a class called MainMenu.
class MainMenu:
    def __init__(self, controller):
        """
        This function creates a menu with the title '2022 3815ICT', with a width and height of the
        controller's surface, with a dark theme. It then adds an image, a play button, a high score
        button, a settings button, a quit button, and a label. It then runs the menu on the controller's
        surface
        
        :param controller: The controller object that is passed in from the main.py file
        """
        menu = pygame_menu.Menu(title='2022 3815ICT', width=controller.surface.get_width(), height=controller.surface.get_height(), theme=pygame_menu.themes.THEME_DARK)
        menu.add.image(image_path="assets/tetrisTitle.png",scale=(0.2,0.2))
        menu.add.button('Play', controller.startTheGame)
        menu.add.button('High Scores', controller.goToHighScore)
        menu.add.button('Settings', controller.goToConfig)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.add.label(title="Christopher Linnett, Lachlan Manson, Duwon Ha")
        menu.mainloop(controller.surface)