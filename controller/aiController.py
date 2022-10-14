from types import NoneType
import copy

# This class is a controller for an AI.
class AIController:
    def __init__(self, controller, width, height):
        """
        This function initializes the game, and sets the clock, counter, width, height, and bestOutput
        to 0.
        
        :param controller: The controller object that will be used to control the game
        :param width: The width of the screen
        :param height: The height of the screen
        """
        self.controller = controller
        self.width = width
        self.height = height
        self.bestOutput = None

    def createGhost(self, rotation):
        """
        It creates a copy of the current tetronomo, rotates it, and then runs the AI to find the best
        path for it

        :param rotation: the rotation of the tetronomo
        """
        self.ghostTetro = copy.deepcopy(self.controller.mainTetronomo)
        self.ghostTetro.rotation = rotation
        self.bestOutput = self.testPaths()
        self.run_ai()

    def freeSpace(self):
        """
        It checks if the current tetronomo can move down one space
        :return: a boolean value.
        """
        emptySpaces = [
            [
                (j, i)
                for j in range(self.width)
                if self.controller.playField.grid[i][j] == (0, 0, 0)
            ]
            for i in range(self.height)
        ]
        emptySpaces = [j for sub in emptySpaces for j in sub]
        formatted = self.ghostTetro.rotate()
        for pos in formatted:
            if pos not in emptySpaces:
                if pos[1] > -1:
                    return False
        return True

    def testPaths(self):
        """
        It tests all possible positions and rotations of the ghost tetromino and returns the position
        and rotation that will result in the highest score
        :return: The x and y coordinates of the best position for the ghost tetromino.
        """
        bestScore = 0
        xGoal = None
        rotationGoal = None
        for num in range(0, self.width):
            self.ghostTetro.x = num
            self.ghostTetro.y = 0
            if self.freeSpace():
                for num in range(len(self.ghostTetro.shape)):
                    self.ghostTetro.rotation = num
                    while self.freeSpace() or self.ghostTetro.y < 0:
                        self.ghostTetro.y += 1
                    self.ghostTetro.y -= 1
                    greatestbot = 0
                    greatestTop = self.height
                    for pos in self.ghostTetro.rotate():
                        if pos[1] < greatestTop:
                            greatestTop = pos[1]
                        if pos[1] > greatestbot:
                            greatestbot = pos[1]
                    if greatestbot+self.ghostTetro.y+greatestTop > bestScore:
                        bestScore = greatestbot+self.ghostTetro.y+greatestTop
                        xGoal = self.ghostTetro.x
                        rotationGoal = self.ghostTetro.rotation
        if xGoal != None and rotationGoal != None:
            return xGoal, rotationGoal

    def run_ai(self):
        """
        If the current position of the tetronomo is not the same as the best output, then move the
        tetronomo to the best output
        :return: The best output is being returned.
        """
        if type(self.bestOutput) == NoneType:
            return
        if (
            self.controller.mainTetronomo.x != self.bestOutput[0]
            or self.controller.mainTetronomo.rotation != self.bestOutput[1]
        ):
            if self.controller.mainTetronomo.rotation != self.bestOutput[1]:
                self.controller.mainTetronomo.rotation += 1
            elif self.controller.mainTetronomo.x < self.bestOutput[0]:
                self.controller.mainTetronomo.x += 1
            elif self.controller.mainTetronomo.x > self.bestOutput[0]:
                self.controller.mainTetronomo.x -= 1
