import json

class configModel(object):
    def __init__(self):
        with open('data/config.json') as configFile:
            self.config = json.load(configFile)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(configModel, cls).__new__(cls)
        return cls.instance

    def saveConfig(self, newConfig):
        with open('data/config.json', 'w') as configFile:
            json.dump(newConfig, configFile)
        self.config = newConfig

    def getConfig(self):
        return self.config
