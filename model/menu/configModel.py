import json

with open('data/config.json') as configFile:
    config = json.load(configFile)


def saveConfig(newConfig):
    with open('data/config.json', 'w') as configFile:
        json.dump(newConfig, configFile)