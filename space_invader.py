import pygame
import random
import math




# Initialize our screen
pygame.init()

game_screen_size_x, game_screen_size_y = pygame.display.get_surface().get_size()


#creating screen
x = 1000
y = 600
screen = pygame.display.set_mode((x, y))

#Background image
bg = pygame.image.load('space.jpg')



#Title and icon for our game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

#loading image
rocket = pygame.image.load('spaceship.png')
pygame.transform.scale2x(rocket)
rocketx = 480
rockety = 480

#loading alien
alien = pygame.image.load('alien.png')
alienx = random.randint(64, game_screen_size_x)
alieny = random.randint(64, 150)
alienx_movement = 2
alieny_movement = 40

#create bullet
bullet = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_movement = 0
bullety_movement = 5
bullet_state = "loaded"


score = 0



# creating player
def player():
    screen.blit(rocket, (rocketx, rockety))

#creating  alien
def enemy():
    screen.blit(alien, (alienx, alieny))

# creating bullet
def Bullet(x, y):
    global bullet_state
    bullet_state = "attack"
    screen.blit(bullet, (x + 5, y - 10))

# shooting
def collide(alienx, alieny, bulletx, bullety):
    distance = math.sqrt((math.pow(alienx-bulletx, 2) + (math.pow(alieny-bullety, 2))))
    if distance < 27:
        return True
    else:
        return False





# Loop the screen
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))


    # rocket movement
    if rocketx <= 0:
        rocketx = 0
    elif rocketx >= game_screen_size_x:
        rocketx = game_screen_size_x

    #alien movement
    alienx += alienx_movement
    if alienx <= 0:
        alienx_movement =  2
        alieny += alieny_movement
    elif alienx >= game_screen_size_x:
        alienx_movement = -2
        alieny += alieny_movement

    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = "loaded"

    if bullet_state is "attack":
        Bullet(bulletx, bullety)
        bullety -= bullety_movement

    # shooting movement
    collision = collide(alienx, alieny, bulletx, bullety)
    if collision:
        bullety = 480
        bullet_state = "loaded"
        score += 1
        print(score)




    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Arrow keys functions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocketx -= 2
    if keys[pygame.K_RIGHT]:
        rocketx += 2
    if keys[pygame.K_SPACE]:
        if bullet_state is "loaded":
            bulletx = rocketx
            Bullet(bulletx, bullety)


        


    
    enemy()
    player()
    pygame.display.update()
