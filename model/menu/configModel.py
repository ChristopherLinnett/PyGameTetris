import json

# This class is used to store the configuration of the model.
class configModel(object):
    def __init__(self):
        with open('data/config.json') as configFile:
            self.config = json.load(configFile)

    def __new__(cls):
        """
        If the class has an instance, return it. Otherwise, create one and return it
        
        :param cls: the class of the object being created
        :return: The instance of the class.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(configModel, cls).__new__(cls)
        return cls.instance

    def saveConfig(self, newConfig):
        """
        It opens the config.json file, dumps the new config into it, and then sets the config variable
        to the new config
        
        :param newConfig: The new config to save
        """
        with open('data/config.json', 'w') as configFile:
            json.dump(newConfig, configFile)
        self.config = newConfig

    def getConfig(self):
        """
        It returns the config object
        :return: The config object
        """
        return self.config
