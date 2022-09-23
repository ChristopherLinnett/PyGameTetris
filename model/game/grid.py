class PlayField():
    def __init__(self):
        self.locked_positions = {}
        self.update()

    def update(self):
        self.grid = [[(0,0,0) for x in range(10)] for x in range(20)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j,i) in self.locked_positions:
                    c = self.locked_positions[(j,i)]
                    self.grid[i][j] = c
        
    def clearRows(self):
        delRowCount = 0
        for i in range(len(self.grid)-1,-1,-1):
            row = self.grid[i]
            if (0,0,0) not in row:
                delRowCount += 1
                index = i
                for j in range(len(row)):
                    try:
                        del self.locked_positions[(j,i)]
                    except:
                        continue
        if delRowCount > 0:
            for key in sorted(list(self.locked_positions), key = lambda x: x[1])[::-1]:
                x,y = key
                if y < index:
                    newKey = (x,y + delRowCount)
                    self.locked_positions[newKey] = self.locked_positions.pop(key)
        return delRowCount
