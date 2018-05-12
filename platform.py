import pygame as pg
from constants import *
from random import randrange
class Platform (pg.sprite.Sprite):
    def __init__(self,x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.Surface((w,h))
        # self.image.fill((self.randomNum(),self.randomNum(), self.randomNum()))
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def randomNum(self):
        return randrange(1,255)