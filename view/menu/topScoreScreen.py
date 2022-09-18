import pygame_menu

class HighScoreScreen:
    def __init__(self,controller):
        self.menu = pygame_menu.Menu(title='High Scores', width=controller.surface.get_width(), height=controller.surface.get_height(), theme=pygame_menu.themes.THEME_DARK)
        names = list(controller.highScores.keys())
        for user in names:
            self.menu.add.label(f'{names.index(user)+1}    {user}       {controller.highScores[user]}')
        self.menu.add.label(" ")
        self.menu.add.button('Back', controller.goToMainMenu)
        self.menu.mainloop(controller.surface)