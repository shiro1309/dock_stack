import pygame as pg, numpy as np, sys, math, engine as eg, threading as th
from load_props import *


pg.init()


reselution = [1920/2,1080/2]
scroll = [0,0]
display = pg.Surface((reselution[0]/2, reselution[1]/2))
player_movment = {
    'right': False,
    'left': False,
    'up': False,
    'down': False,
}

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(reselution, 0, 32)
        self.clock = pg.time.Clock()

        self.world = eg.world()
        self.input = eg.input()
        
        self.game_map = self.world.world_read("map")
        
    def run(self):
        global player_movment
        while True:
            display.fill((255,255,255))
            #thred_1 = th.Thread(target=self.world.world_painter, args=(self.game_map, display, tile_size, dirt, grass))
            
            #thred_1.start()
            player_movment = self.input.user(player_movment)

            self.world.world_painter(self.game_map, display, tile_size, dirt, grass)
            #thred_1.join()
            self.clock.tick(600)
            pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')
            #print(player_movment)
            surf = pg.transform.scale(display, reselution)
            self.screen.blit(surf, (0, 0))
            pg.display.update()

if __name__ == '__main__':
    app = App()
    app.run()
