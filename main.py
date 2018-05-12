import pygame as pg
import random
from constants import *
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        #initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self, level):
        #resets game 
        self.all_platforms= pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        
        level_creation = self.render_level(level)
        for block in level_creation:
            self.all_sprites.add(block)
            self.all_platforms.add(block)
        
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
        #Add back in once maps can be correcrtly loaded in        
        # self.p1 = Platform(0,HEIGHT-40,WIDTH,40)
        # self.p2 = Platform(WIDTH/2 -50, HEIGHT*3/4,100,20)

        # self.all_sprites.add(self.p1)
        # self.all_sprites.add(self.p2)

        # self.all_platforms.add(self.p1)
        # self.all_platforms.add(self.p2)

    def render_level(self, level):
        level_arr = []
        x_coord = 0
        y_coord = 0
        with open(level,'r') as level:

            level_map = level.readlines()
            print(len(level_map), len(level_map[0]))
            
            
            x_block_size = WIDTH/len(level_map[0])-1
            y_block_size = HEIGHT/len(level_map)-1
            
            for line in level_map:
                x_coord = 0 
                for char in line:
                    if char == "#":
                        block = Platform(x_coord, y_coord, x_block_size, y_block_size)
                        level_arr.append(block)                    
                    x_coord += x_block_size
                y_coord += y_block_size
        
        return level_arr






    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            

    def update(self):
        #update 
        if self.player.velocity.y > 0:    
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                    self.player.position.y = hits[0].rect.top
                    self.player.velocity.y = -0.3
        self.all_sprites.update()
    
    def events(self):
        #Game loop events
        hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
        if hits:
                self.player.position.y = hits[0].rect.top - .25
                self.player.velocity.y = -0.03

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and hits:
                    self.player.jump()
        
                
    
    def draw(self):
        #Game Loop Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #game splash/start screen
        pass
    def show_go_screen(self):
        #Game over screen
        pass

g = Game()
g.show_start_screen()



while g.running:
    g.new(LEVEL)
pg.quit()