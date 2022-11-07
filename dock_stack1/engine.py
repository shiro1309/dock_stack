import pygame as pg, sys
from pygame.locals import *

class world:
    def world_read(self, path):
        file = open(path + ".txt", "r")
        data = file.read()
        file.close()
        data = data.split("\n")
        game_map = []
        for i in data:
            game_map.append(list(i))
        return game_map

    def world_painter(self, worldfile, screen,tile_size, img_a,img_b):
        y = 0
        for row in worldfile:
            x = 0
            for tile in row:
                if tile == "1":
                    screen.blit(img_a, (x*tile_size+x, y*tile_size+y))
                if tile == "2":
                    screen.blit(img_b, (x*tile_size+x, y*tile_size+y))
                x += 1
            y+= 1
    
    def world_movement(self, worldfile, display,tile_size, img_a,img_b, scroll, tile_rects):
        y = 0
        for row in worldfile:
            x = 0
            for tile in row:
                if tile == "1":
                    display.blit(img_a, (x*tile_size-scroll[0], y*tile_size-scroll[1]))
                if tile == "2":
                    display.blit(img_b, (x*tile_size-scroll[0], y*tile_size-scroll[1]))
                if tile != "0":
                    tile_rects.append(pg.Rect(x*tile_size,y*tile_size,tile_size,tile_size))
                x += 1
            y+= 1

class input:
    
    def user(self, player_mov):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    player_mov['right'] = True
                if event.key == K_LEFT:
                    player_mov['left'] = True

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    player_mov['right'] = False
                if event.key == K_LEFT:
                    player_mov['left'] = False
        
        print(player_mov)
        return player_mov
        