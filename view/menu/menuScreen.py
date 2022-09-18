import pygame_menu
import view.menu.topScoreScreen as highScoreScreen


class MainMenu:
    def __init__(self, controller):
        menu = pygame_menu.Menu(title='2022 3815ICT', width=controller.surface.get_width(), height=controller.surface.get_height())
        menu.add.image(image_path="assets/tetrisTitle.png",scale=(0.2,0.2))
        menu.add.button('Play', controller.startTheGame)
        menu.add.button('High Scores', controller.goToHighScore)
        menu.add.button('Settings', controller.goToConfig)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.add.label(title="Christopher Linnett, Lachlan Manson, Duwon Ha")
        menu.mainloop(controller.surface)