import model.menu.configModel as configClass

def getConfig():
    return configClass.config

def saveConfig(newConfig):
    print(newConfig)
    configClass.saveConfig(newConfig)