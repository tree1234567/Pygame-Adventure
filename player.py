import pygame as pg
from constants import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10,10))
        self.image.fill(WHITE)
        # self.game = game
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT/2
        self.position = vec(WIDTH/4, HEIGHT/4)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
    def jump(self):
        self.velocity.y = -7
        
    def update(self):
        self.acceleration = vec (0,PLAYER_GRAVITY)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.acceleration.x = - PLAYER_ACCELERATION
        if keystate[pg.K_RIGHT]:
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