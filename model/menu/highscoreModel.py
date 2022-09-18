import json

with open('data/highscores.json') as highscoreFile:
    highscores = json.load(highscoreFile)


def saveHighscores(newHighscores):
    with open('data/highscores.json', 'w') as highscoreFile:
        json.dump(newHighscores, highscoreFile)