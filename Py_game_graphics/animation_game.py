# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random
shot_fired = False

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
LAWN_GREEN = (124,252,0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0,0,0)

# Settings
stormy = True

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, DARK_BLUE, rect)

''' Make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

is_raining = True

''' Make rain '''
if is_raining:
    num_drops = 700
    rain = []

    for i in range(num_drops):
        x = random.randrange(0, 1000)
        y = random.randrange(-100, 600)
        r = random.randrange(1, 5)
        stop = random.randrange(400, 700)
        drop = [x, y, r, r, stop]
        rain.append(drop)

if not is_raining:
    num_drops = 0
    rain = []

    for i in range(num_drops):
        x = random.randrange(0, 1000)
        y = random.randrange(-100, 600)
        r = random.randrange(1, 5)
        stop = random.randrange(400, 700)
        drop = [x, y, r, r, stop]
        rain.append(drop)


''' Make stars '''
stars = []
for i in range(200):
    x= random.randrange(0,800)
    y = random.randrange(0, 400)
    r = random.randrange(1,5)
    s = [x, y, r, r]
    stars.append(s)

# Block
block_loc = [380, 540]
vel = [0, 0]
speed = 10

def draw_block(loc):
    x = block_loc[0]
    y = block_loc[1]
    
    pygame.draw.rect(screen, WHITE, [x, y, 40, 240])
    
# Make Bullets
bullets = []

def draw_bullet(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.rect(screen, GREEN, [x, y, 5, 15])


lightning_timer = 0
daytime = True
is_raining = True


# Game loop
done = False
     
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            if event.key == pygame.K_TAB:
                is_raining = not is_raining
            for event in pygame.event.get():
                if event.key == pygame.K_d:
                    vel[0] = speed
                if event.key == pygame.K_a:
                    vel[0] =-1 *  speed
                if event.key == pygame.K_w:
                    shot_fired = True
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                vel[0] = 0
            if event.key == pygame.K_a:
                vel[0] = 0


    # Game logic

    ''' move block and bullets'''

    block_loc[0] += vel[0]

    if shot_fired == True:
        bullets.append([block_loc[0] + 17.5, block_loc[1]])
        shot_fired = False
        
    for b in bullets:
        b[1] -= 24



    ''' move clouds '''
    if is_raining:
        for c in far_clouds:
            c[0] -= 1

            if c[0] < -100:
                c[0] = random.randrange(800, 1600)
                
                c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    ''' move rain '''
    if is_raining:
        for r in rain:
            r[0] -= 1
            r[1] += 4

            if r[1] > r[4]:
                r[0] = random.randrange(0, 1000)
                r[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
    
    # Drawing code

    '''block '''
    draw_block(block_loc)
    '''bullet '''
    for b in bullets:
        draw_bullet(b)
        
    ''' sky '''
    if daytime:
        screen.fill(GRAY)
        if lightning_timer > 0:
            screen.fill(YELLOW)
    if not daytime:
        screen.fill(BLACK)
        if lightning_timer > 0:
            screen.fill(YELLOW)
    if not is_raining:
        screen.fill(BLUE)
        if not daytime:
            screen.fill(BLACK)



    ''' sun '''
    if not is_raining:
        if daytime:
            pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
            
    ''' moon '''
    

    ''' grass '''
    if is_raining:
        pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    if not is_raining:
        pygame.draw.rect(screen, LAWN_GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' clouds '''
    if is_raining:
        for c in far_clouds:
            draw_cloud(c, NOT_QUITE_DARK_GRAY)

    ''' rain '''
    if is_raining:
        for r in rain:
            draw_raindrop(r)
            

    ''' clouds '''
    if is_raining:
        for c in near_clouds:
            draw_cloud(c, DARK_GRAY)
    if not is_raining:
        for c in near_clouds:
            draw_cloud(c, WHITE)
            if not daytime:
                draw_cloud(c, BLACK)
    ''' stars '''
    if not is_raining:
        if not daytime:
                for s in stars:
                    pygame.draw.ellipse(screen, WHITE, s)

    '''block '''
    draw_block(block_loc)

    '''bullet '''
    for b in bullets:
        draw_bullet(b)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

