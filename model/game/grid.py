class PlayField():
    def __init__(self,locked_positions={}):
        self.grid = [[(0,0,0) for x in range(10)] for x in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j,i) in locked_positions:
                    c = locked_positions[(j,i)]
                    self.grid[i][j] = c

    def clear_rows(grid, locked):
        pass
