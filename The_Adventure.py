#PyGame Template! Please erase me!
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

#Useful colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
VIOLET = (255,0,255)
CYAN = (0,255,255)

vec = pygame.math.Vector2 #imports a vector from pygame
PLAYER_FRICTION = -0.05
PLAYER_ACCELERATION = .5
PLAYER_GRAVITY = .5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,50))
        self.image.fill(VIOLET)
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT/2
        self.position = vec(WIDTH/2, HEIGHT/2)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
    def jump(self):
        self.velocity.y = -10
    def update(self):
        self.acceleration = vec (0,PLAYER_GRAVITY)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.acceleration.x = - PLAYER_ACCELERATION
        if keystate[pygame.K_RIGHT]:
            self.acceleration.x = PLAYER_ACCELERATION

        # applies friction to the 'x' direction
        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        #equations of motion
        self.velocity += self.acceleration
        self.position += self.velocity + (0.5 * self.acceleration)
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH


        self.rect.midbottom = self.position


class Platform (pygame.sprite.Sprite):
    def __init__(self,x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



#initializes pygame and creates window!
pygame.init()
pygame.mixer.init()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Adventure")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_platforms = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
p1 = Platform(0,HEIGHT-40,WIDTH,40)
p2 = Platform(WIDTH/2 -50, HEIGHT*3/4,100,20)
all_sprites.add(p1)
all_platforms.add(p1)
all_sprites.add(p2)
all_platforms.add(p2)

#game loop
running = False
while not running:
    #keep loop running at right speed
    clock.tick(FPS)
    #process input(events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
    # Update
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, all_platforms, False)
    if hits:
        player.position.y = hits[0].rect.top
        player.velocity.y = -0.3



    # draw/render
    DISPLAY.fill(BLACK)
    all_sprites.draw(DISPLAY)

#*after* drawing everything, update display at the end of each loop iteration
    pygame.display.update()
