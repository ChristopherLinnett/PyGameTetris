import json

# It's a singleton class that loads a json file and allows you to get and set the data in that file.
class highScoreModel(object):
    def __init__(self):
        with open('data/highscores.json') as highscoreFile:
         self.highscores = json.load(highscoreFile)

    def __new__(cls):
        """
        If the class has an instance, return it. Otherwise, create a new instance, set the instance
        attribute to the new instance, and return the new instance
        
        :param cls: the class of the object being created
        :return: The instance of the class.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(highScoreModel, cls).__new__(cls)
        return cls.instance

    def getHighScores(self):
        """
        This function returns the highscores
        :return: The highscores list.
        """
        return self.highscores
 
    def saveHighScores(self, newHighscores):
        """
        It opens the highscores.json file, dumps the new highscores into it, and then sets the highscores
        variable to the new highscores
        
        :param newHighscores: A list of dictionaries, each dictionary containing the name and score of a
        player
        """
        with open('data/highscores.json', 'w') as highscoreFile:
            json.dump(newHighscores, highscoreFile)
        self.highscores = newHighscores