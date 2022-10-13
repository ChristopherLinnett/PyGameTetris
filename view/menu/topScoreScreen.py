import pygame_menu

# This class is a screen that displays the high scores.
class HighScoreScreen:
    def __init__(self,controller,score=None):
        """
        It creates a menu with a list of high scores, and if the user has a high score, it asks them to
        input their name.
        
        :param controller: the controller object
        :param score: the score of the player
        """
        self.menu = pygame_menu.Menu(title='High Scores', width=controller.surface.get_width(), height=controller.surface.get_height(), theme=pygame_menu.themes.THEME_DARK)
        names = list(controller.highScores.keys())
        self.controller = controller
        for user in names:
            if score and score > int(controller.highScores[user]):
                self.controller.tempHighScore = score
                if self.controller.config['aiMode']==True:
                    self.controller.modifyHighName('AI')
                    self.controller.saveHighScore()
                else:
                    self.addHighScoreInput(score)
                score = 0
            self.menu.add.label(f'{names.index(user)+1}    {user}       {controller.highScores[user]}')
        self.menu.add.label(" ")
        self.menu.add.button('Back', controller.goToMainMenu)
        self.menu.mainloop(controller.surface)
    def addHighScoreInput(self, score):
        self.menu.add.text_input('Enter Name:           ',default='',onchange=self.controller.modifyHighName)
        self.menu.add.button('Save',self.controller.saveHighScore)
