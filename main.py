from controller.menu.menuController import menuController
from view.menu.menuScreen import MainMenu

menuControllerObj = menuController()
MainMenu = MainMenu(surface = menuControllerObj.surface, controller = menuControllerObj)