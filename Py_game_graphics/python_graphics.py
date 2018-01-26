# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)


done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
screen.fill(BLUE)

'''sun'''
    pygame.draw.ellipse(screen, YELLOW, [20, 20, 100, 100])
    pygame.draw.line(screen, YELLOW, [0, 60], [30, 60], 3)
    pygame.draw.line(screen, YELLOW, [5, 30], [30, 40], 3)


pygame.draw.rect(screen, RED, [350, 200, 200, 300])
pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

y = 380
for x in range(5, 800, 30):
    pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                        [x+10, y+40], [x, y+40],
                                        [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)
    
pygame.display.flip()

