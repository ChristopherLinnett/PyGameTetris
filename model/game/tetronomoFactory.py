from model.game.shapesData import *

class TetronomoFactory(object):
    def createTetronomo(x, y, tetronomoType):
        if tetronomoType == 'S':
            return shapeS(x, y)
        elif tetronomoType == 'Z':
            return shapeZ(x, y)
        elif tetronomoType == 'I':
            return shapeI(x, y)
        elif tetronomoType == 'O':
            return shapeO(x, y)
        elif tetronomoType == 'J':
            return shapeJ(x, y)
        elif tetronomoType == 'L':
            return shapeL(x, y)
        elif tetronomoType == 'T':
            return shapeT(x, y)
        else:
            print('Invalid Tetronomo Type')