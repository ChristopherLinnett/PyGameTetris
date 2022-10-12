from abc import ABC

# > This class defines the basic properties and methods of a tetronomo.
class Tetronomo(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0

    def rotate(self):
        """
        It takes the shape of the tetromino, and then it takes the rotation of the tetromino, and then
        it takes the x and y coordinates of the tetromino, and then it returns the positions of the
        tetromino
        :return: The positions of the shape.
        """
        positions = []
        format = self.shape[self.rotation % len(self.shape)]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    positions.append((self.x + j, self.y + i))
        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)
        return positions
