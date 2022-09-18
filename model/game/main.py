import view.menu.menuScreen as menuScreen
import sys
from tkinter import *
from tkinter import messagebox
from model.game.tetronomo import Tetronomo
import model.game.shapesData as sd

def runGame(windowSize, playSize):
    import pygame
    import random
    """
    10 x 20 square grid
    shapes: S, Z, I, O, J, L, T
    represented in order by 0 - 6
    """
    import view.menu.topScoreScreen as topScoreScreen
    pygame.font.init()

    # GLOBALS VARS
    s_width = windowSize[0]
    s_height = windowSize[1]
    play_width = 300  # meaning 300 // 10 = 30 width per block
    play_height = 600  # meaning 600 // 20 = 20 height per block
    block_size = (play_width if (play_width<play_height) else play_height)//10
    top_left_x = (s_width - play_width)//2
    top_left_y = s_height - play_height


    # SHAPE FORMATS

    # index 0 - 6 represent shape

    def showPopUpBox():
        boxResponse = messagebox.askyesno(title="Exit Game?",message="Are you sure you want to quit")
        if boxResponse == True:
            menuScreen.gameLaunched()

    def create_grid(locked_positions={}):
        grid = [[(0,0,0) for x in range(10)] for x in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j,i) in locked_positions:
                    c = locked_positions[(j,i)]
                    grid[i][j] = c
        return grid

    def valid_space(tetronomo, grid):
        accepted_pos = [[(j,i) for j in range(10) if grid[i][j]== (0,0,0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = tetronomo.convert_shape_format()

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True

    def check_lost(positions):
        for pos in positions:
            x,y = pos
            if y < 1:
                return True
        return False

    def draw_text_middle(text, size, color, surface):  
        pass
    
    def draw_grid(surface, grid):
        sx = top_left_x
        sy = top_left_y

        for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (sx, sy+i*block_size), (sx+play_width, sy+i*block_size))
            for j in range(len(grid[i])+1):
                pygame.draw.line(surface, (128,128,128), (sx+j*block_size, sy), (sx+j*block_size, sy+play_height))

    def clear_rows(grid, locked):
        pass

    def draw_preview_tetronomo(tetronomo, surface):
        font = pygame.font.SysFont('arial', 30)
        label = font.render("Next Shape", 1, (255,255,255))

        sx = top_left_x + play_width +50
        sy = top_left_y + play_height/2-100
        format = tetronomo.shape[tetronomo.rotation % len(tetronomo.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, tetronomo.colour, (sx+j*block_size, sy+i*block_size, block_size, block_size),0)
        surface.blit(label, (sx+10, sy-30))

    def draw_window(surface, grid):
        surface.fill((0,0,0))
        pygame.font.init()
        font = pygame.font.SysFont('arial', 60)
        menuFont = pygame.font.SysFont('arial', 24)

        label = font.render('Tetris', 1, (255,255,255))
        label2 = menuFont.render('Group: 10', 1, (255,255,255))
        label3 = menuFont.render('Score: 0', 1, (255,255,255))
        label4 = menuFont.render('Level: 1', 1, (255,255,255))
        label5 = menuFont.render('Mode: Player', 1, (255,255,255))

        surface.blit(label, (0+windowSize[0]//2 - label.get_width()//2, 30))
        surface.blit(label2, (0, 15))
        surface.blit(label3, (0+windowSize[0] - label3.get_width(), 15))
        surface.blit(label4, (0+windowSize[0] *4/5 - label4.get_width(), 15))
        surface.blit(label5, (windowSize[0]*1/5, 15))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (top_left_x+j*block_size, top_left_y+i*block_size, block_size, block_size), 0) #Draw blocks

        draw_grid(surface, grid)
        


    def main(win):
        locked_positions = {}
        grid = create_grid(locked_positions)

        change_piece = False
        run = True
        current_tetronomo = Tetronomo(5,0,random.choice(sd.shapes))
        preview_tetronomo = Tetronomo(5,0,random.choice(sd.shapes))
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27
        pause = False

        while run:
            grid = create_grid(locked_positions)
            if pause == False:
                fall_time += clock.get_rawtime() 
                clock.tick()

            if fall_time/1000 > fall_speed:
                fall_time = 0
                current_tetronomo.y += 1
                if not(valid_space(current_tetronomo, grid)) and current_tetronomo.y > 0:
                    current_tetronomo.y -= 1
                    change_piece = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if pause == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            current_tetronomo.x -= 1
                            if not(valid_space(current_tetronomo, grid)):
                                current_tetronomo.x+=1
                        if event.key == pygame.K_RIGHT:
                            current_tetronomo.x += 1
                            if not(valid_space(current_tetronomo, grid)):
                                current_tetronomo.x-=1
                        if event.key == pygame.K_DOWN:
                            current_tetronomo.y += 1
                            if not(valid_space(current_tetronomo, grid)):
                                current_tetronomo.y-=1
                        if event.key == pygame.K_UP:
                            current_tetronomo.rotation += 1
                            if not(valid_space(current_tetronomo, grid)):
                                current_tetronomo.rotation-=1
                        if event.key == pygame.K_ESCAPE:
                            pause = True
                            showPopUpBox()
                            pause = False
            shape_pos = current_tetronomo.convert_shape_format()
            for i in range(len(shape_pos)):
                x,y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_tetronomo.colour

            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_tetronomo.colour
                current_tetronomo = preview_tetronomo
                preview_tetronomo.new_random_shape()
                change_piece = False
            draw_window(win,grid)
            draw_preview_tetronomo(preview_tetronomo, win)
            pygame.display.update()

            if check_lost(locked_positions):
                run = False
        topScoreScreen.showTopScores()

    def main_menu(win):
        main(win)

    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')
    main_menu(win)  # start game