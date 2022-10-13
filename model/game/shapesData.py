from model.game.tetronomo import Tetronomo


class shapeS(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", "......", "..00..", ".00...", "....."],
            [".....", "..0..", "..00.", "...0.", "....."],
        ]

        self.colour = (0, 255, 0)


# This class is a subclass of Tetronomo. It has a shape of Z and a color of red.
class shapeZ(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", ".....", ".00..", "..00.", "....."],
            [".....", "..0..", ".00..", ".0...", "....."],
        ]

        self.colour = (255, 0, 0)


# This class is a subclass of Tetronomo. It has a shape of I, and it has a color of blue.
class shapeI(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            ["..0..", "..0..", "..0..", "..0..", "....."],
            [".....", "0000.", ".....", ".....", "....."],
        ]

        self.colour = (0, 255, 255)


# This class is a subclass of Tetronomo. It has a shape of O and a color of yellow.
class shapeO(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [[".....", ".....", ".00..", ".00..", "....."]]

        self.colour = (255, 255, 0)


# This class is a subclass of Tetronomo. It has a shape of J and a color of blue.
class shapeJ(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", ".0...", ".000.", ".....", "....."],
            [".....", "..00.", "..0..", "..0..", "....."],
            [".....", ".....", ".000.", "...0.", "....."],
            [".....", "..0..", "..0..", ".00..", "....."],
        ]

        self.colour = (255, 165, 0)


# This class is a subclass of Tetronomo. It has a shape of L and a color of orange.
class shapeL(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", "...0.", ".000.", ".....", "....."],
            [".....", "..0..", "..0..", "..00.", "....."],
            [".....", ".....", ".000.", ".0...", "....."],
            [".....", ".00..", "..0..", "..0..", "....."],
        ]

        self.colour = (0, 0, 255)

# The class shapeT is a subclass of Tetronomo
class shapeT(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", "..0..", ".000.", ".....", "....."],
            [".....", "..0..", "..00.", "..0..", "....."],
            [".....", ".....", ".000.", "..0..", "....."],
            [".....", "..0..", ".00..", "..0..", "....."],
        ]

        self.colour = (128, 0, 128)


# This class is a subclass of Tetronomo. It has a shape of a small I.
class shapeSmallI(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            ["..0..", "..0..", "..0..", ".....", "....."],
            [".....", "000.", ".....", ".....", "....."],
        ]

        self.colour = (0, 255, 255)


# This class is a subclass of the Tetronomo class. It has a shape of a small L.
class shapeSmallL(Tetronomo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape = [
            [".....", "...0.", "..00.", ".....", "....."],
            [".....", ".....", "..0..", "..00.", "....."],
            [".....", ".....", ".00..", ".0...", "....."],
            [".....", ".00..", "..0..", ".....", "....."],
        ]

        self.colour = (0, 0, 255)


shapes = ["S", "Z", "I", "O", "J", "L", "T"]
extendedShapes = ["smallL", "smallI"]
