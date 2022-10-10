from model.game.tetronomo import Tetronomo

class shapeS(Tetronomo):
        def __init__(self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '......',
        '..00..',
        '.00...',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

                self.colour = (0, 255, 0)

class shapeZ(Tetronomo):
        def __init__(self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

                self.colour = (255, 0, 0)

class shapeI(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

                self.colour = (0, 255, 255)

class shapeO(Tetronomo):
         def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']]

                self.colour = (255, 255, 0)

class shapeJ(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

                self.colour = (255, 165, 0)

class shapeL(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

                self.colour = (0, 0, 255)

class shapeT(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]

                self.colour = (128, 0, 128)
class shapeSmallI(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['..0..',
        '..0..',
        '..0..',
        '.....',
        '.....'],
        ['.....',
        '000.',
        '.....',
        '.....',
        '.....']]

                self.colour = (0, 255, 255)

class shapeSmallL(Tetronomo):
        def __init__ (self, x, y):
                super().__init__(x,y)
                self.shape = [['.....',
        '...0.',
        '..00.',
        '.....',
        '.....'],
        ['.....',
        '.....',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.00..',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '.....',
        '.....']]

                self.colour = (0, 0, 255)

shapes = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']
extendedShapes = ['smallL', 'smallI']