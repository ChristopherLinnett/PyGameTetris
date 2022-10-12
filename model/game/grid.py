# PlayField is a class that represents the tetris game board.
class PlayField:
    def __init__(self, width, height):
        self.filledPositions = {}
        self.width = width
        self.height = height
        self.update()

    def update(self):
        """
        It updates the grid.
        """
        self.grid = [[(0, 0, 0) for x in range(self.width)] for x in range(self.height)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in self.filledPositions:
                    c = self.filledPositions[(j, i)]
                    self.grid[i][j] = c

    def clearRows(self):
        """
        It deletes rows that are filled with blocks and moves the blocks above the deleted rows down
        :return: The number of rows cleared.
        """
        delRowCount = 0
        for i in range(len(self.grid) - 1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                delRowCount += 1
                index = i
                for j in range(len(row)):
                    try:
                        del self.filledPositions[(j, i)]
                    except:
                        continue
        if delRowCount > 0:
            for key in sorted(list(self.filledPositions), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < index:
                    newKey = (x, y + delRowCount)
                    self.filledPositions[newKey] = self.filledPositions.pop(key)
        return delRowCount
