import model.game.shapesData as sd


class Tetronomo(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = sd.colours[sd.shapes.index(shape)]
        self.rotation = 0

    def rotate(self):
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
