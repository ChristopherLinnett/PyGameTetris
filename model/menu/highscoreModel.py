import json

class highscoreModel(object):
    def __init__(self):
        with open('data/highscores.json') as highscoreFile:
         self.highscores = json.load(highscoreFile)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(highscoreModel, cls).__new__(cls)
        return cls.instance

    def getHighScores(self):
        return self.highscores
 
    def saveHighscores(self, newHighscores):
        with open('data/highscores.json', 'w') as highscoreFile:
            json.dump(newHighscores, highscoreFile)
        self.highscores = newHighscores