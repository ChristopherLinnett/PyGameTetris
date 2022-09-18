import model.menu.highscoreModel as hs

def getHighscores():
    return hs.highscores

def saveHighscores(newHighscores):
    hs.saveHighscores(newHighscores)
