from model.game.shapesData import *

class TetronomoFactory(object):
    def createTetronomo(x, y, tetronomoType):
        """
        It takes in a string and two integers, and returns a tetronomo shape and its rotation variants
        
        :param x: The x coordinate of the top left corner of the tetronomo
        :param y: The y coordinate of the tetronomo
        :param tetronomoType: The type of tetronomo to be created
        :return: a list of lists.
        """
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
        elif tetronomoType == 'smallI':
            return shapeSmallI(x, y)
        elif tetronomoType == 'smallL':
            return shapeSmallL(x, y)
        else:
            print('Invalid Tetronomo Type')