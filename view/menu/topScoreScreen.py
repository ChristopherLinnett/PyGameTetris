import pygame_menu

class HighScoreScreen:
    def __init__(self,controller,score=None):
        self.menu = pygame_menu.Menu(title='High Scores', width=controller.surface.get_width(), height=controller.surface.get_height(), theme=pygame_menu.themes.THEME_DARK)
        names = list(controller.highScores.keys())
        self.controller = controller
        for user in names:
            if score and score > int(controller.highScores[user]):
                self.controller.tempHighScore = score
                self.addHighScoreInput(score)
            self.menu.add.label(f'{names.index(user)+1}    {user}       {controller.highScores[user]}')
        self.menu.add.label(" ")
        self.menu.add.button('Back', controller.goToMainMenu)
        self.menu.mainloop(controller.surface)
    def addHighScoreInput(self, score):
        self.menu.add.text_input('',default='Enter Your Name',onchange=self.controller.modifyHighName)
        self.menu.add.button('Save',self.controller.saveHighScore)
