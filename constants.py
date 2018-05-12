import pygame as pg 


WIDTH = 640
HEIGHT = 400
screen_size = (WIDTH, HEIGHT)
title = "Bob's Adventure"
FPS = 60

#Useful colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
VIOLET = (255,0,255)
CYAN = (0,255,255)

 #imports a vector from pygame
PLAYER_FRICTION = -0.05
PLAYER_ACCELERATION = .5
PLAYER_GRAVITY = .5

vec = pg.math.Vector2
player_x_speed = .5 * WIDTH / 1000
player_y_speed = .5 * HEIGHT / 1000

LEVEL = "level1.txt"

