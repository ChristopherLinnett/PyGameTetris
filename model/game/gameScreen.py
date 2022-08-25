import sys, pygame
import json
import model.game.main as playGame

def loop(windowSize, playSize):
    playGame.runGame(windowSize, playSize)

def loopTest():
    pygame.init()
    config = json.load(open('config.json'))
    size = width, height = config['screenSize']['width'], config['screenSize']['height']
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()
    time = 0

    while time<300:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        time+=1
        if time%10 == 0:
            print(time)
        clock.tick(60)