from tkinter import messagebox

# It's a class that draws the game to the screen.
class GameView():
    def __init__(self,controller,pygame, surface, gridResX,gridResY):
        self.pygame = pygame
        self.controller = controller
        self.surface = surface
        self.s_width, self.s_height = self.surface.get_size()
        self.gridResX = gridResX
        self.gridResY = gridResY
        self.play_width = 600*(gridResX/gridResY) if gridResX<=1.5*gridResY else 900
        self.play_height = 600 if gridResX<=1.5*gridResY else 900*(gridResY/gridResX)
        self.block_size = (self.play_height/gridResY if gridResX<=1.5*gridResY else self.play_width/gridResX)
        if gridResX>=1.5*gridResY:
            print(gridResX, gridResY*1.5, gridResX>=gridResY)
        self.top_left_x = (self.s_width - self.play_width)/2
        self.top_left_y = self.s_height - self.play_height
        self.win = pygame.display.set_mode((self.s_width, self.s_height))
        pygame.display.set_caption('Tetris')


    """
    It draws the play field.
    """
    def drawPlayField(self):
        sx = self.top_left_x
        sy = self.top_left_y

        for i in range(len(self.controller.playField.grid)):
            self.pygame.draw.line(self.surface, (128,128,128), (sx, sy+i*self.block_size), (sx+self.play_width, sy+i*self.block_size))
            for j in range(0,len(self.controller.playField.grid[i])+1):
                self.pygame.draw.line(self.surface, (128,128,128), (sx+j*self.block_size, sy), (sx+j*self.block_size, sy+self.play_height))
        self.pygame.draw.line(self.surface, (255,0,0), (sx, sy+(len(self.controller.playField.grid))*self.block_size), (sx+self.play_width, sy+(len(self.controller.playField.grid))*self.block_size))



    def drawNextTetronomo(self,tetronomo):
        """
        It draws the tetronomo preview.
        
        :param tetronomo: the tetronomo object
        """
        font = self.pygame.font.SysFont('arial', 30)
        label = font.render("Next Shape", 1, (255,255,255))

        sx = self.top_left_x + self.play_width+50
        sy = self.top_left_y + self.play_height/2-100
        format = tetronomo.shape[tetronomo.rotation % len(tetronomo.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    self.pygame.draw.rect(self.surface, tetronomo.colour, (sx+j*self.block_size, sy+i*self.block_size, self.block_size, self.block_size),0)
        self.surface.blit(label, (sx+10, sy-30))

    def drawWindow(self, playField):
        """
        It draws the window
        
        :param playField: The playfield that is being drawn
        """
        self.surface.fill((0,0,0))
        self.pygame.font.init()
        font = self.pygame.font.SysFont('arial', 60)
        menuFont = self.pygame.font.SysFont('arial', 24)

        fontLabel = font.render('Tetris', 1, (255,255,255))
        groupLabel = menuFont.render('Group: 10', 1, (255,255,255))
        scoreLabel = menuFont.render(f'Score: {self.controller.score}', 1, (255,255,255))
        clearedRowsLabel = menuFont.render(f'Cleared Rows: {self.controller.totalClearedRows}', 1, (255,255,255))

        levelLabel = menuFont.render(f'level: {self.controller.level}', 1, (255,255,255))
        modeLabel = menuFont.render('Mode: Player', 1, (255,255,255))
        extendedLabel = menuFont.render(f'Extended Mode: {self.controller.extendedMode}', 1, (255,255,255))

        self.surface.blit(fontLabel, (0+self.s_width/2 - fontLabel.get_width()/2, 30))
        self.surface.blit(groupLabel, (2, 15))
        self.surface.blit(scoreLabel, (-2+self.s_width - scoreLabel.get_width(), 15))
        self.surface.blit(clearedRowsLabel, (-2+self.s_width - clearedRowsLabel.get_width(), 45))

        self.surface.blit(levelLabel, (0+self.s_width *4/5 - levelLabel.get_width(), 15))
        self.surface.blit(modeLabel, (self.s_width*1/5, 15))
        self.surface.blit(extendedLabel, (self.s_width*1/5, 45))


        for i in range(len(playField)):
            for j in range(len(playField[i])):
                self.pygame.draw.rect(self.surface, playField[i][j], (self.top_left_x+j*self.block_size, self.top_left_y+i*self.block_size, self.block_size, self.block_size), 0) #Draw blocks

        self.drawPlayField()

    def showPopUpBox(self):
        """
        It creates a pop-up box that asks the user if they want to quit the game. 
        If they click yes, the game will quit
        """
        boxResponse = messagebox.askyesno(
            title="Exit Game?", message="Are you sure you want to quit"
        )
        if boxResponse == True:
            self.controller.run=False

        