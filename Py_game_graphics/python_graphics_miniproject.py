
# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Kenneth's Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BRIGHT_BLUE = (39, 172, 244)
PURPLE = (179, 39, 244)
BRIGHT_GREEN = (70, 244, 39)
BROWN = (165, 42, 42)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_tree(x,y):
    #tree trunk (50 wide and 100 tall)
    pygame.draw.rect(screen, BROWN ,(x,y-100,50,100))
    #leaves are a circle
    pygame.draw.circle(screen,(WHITE),(x+25,y-120),50)

def draw_house(x,y):
    pygame.draw.rect(screen, RED, [x+50, y, 300, 200])
    pygame.draw.rect(screen, BLACK, [x+50, y, 300, 200], 3)
    pygame.draw.polygon(screen, BLACK, [[x, y], [450, 150], [650, x]], 5)
    pygame.draw.polygon(screen, PURPLE, [[x, y], [450, 150], [650, x]])
    pygame.draw.rect(screen, BLACK, [x+150, y+100, 100, 150], 5)
    pygame.draw.rect(screen, YELLOW, [x+150, y+100, 100, 150])
    pygame.draw.ellipse(screen, BLACK, [x+165, y+110, 15, 15])

def moon(x,y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])


''' Make stars '''
stars = []
for i in range(200):
    x= random.randrange(0,800)
    y = random.randrange(0, 400)
    r = random.randrange(1,5)
    s = [x, y, r, r]
    stars.append(s)

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic

             
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)

    ''' moon '''
    moon(575, 75)

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    ''' trees '''
    draw_tree(60,400)
    draw_tree(700,400)

    '''house'''
    draw_house(250,250)
    

    ''' grass '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5
                                             , y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)




    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
