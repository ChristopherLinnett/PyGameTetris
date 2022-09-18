import json

with open('./config.json') as configFile:
    config = json.load(configFile)


def saveConfig(newConfig):
    with open('./config.json', 'w') as configFile:
        json.dump(newConfig, configFile)