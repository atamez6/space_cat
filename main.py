#!/usr/bin/env python

import settings, pygame, sys
from utils import Background
from player import Player
from enemies import *
import game_functions

def main():
    pygame.init()
    pygame.mixer.init()
    screen  = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
    pygame.display.set_caption("Space Cat!")
    clock = pygame.time.Clock()


    all_sprites = pygame.sprite.Group()
    #enemies_list = pygame.sprite.Group()
    player = Player()
    
    bg = Background.background()
    all_sprites.add(player)
    green_alien_manager=GreenalienManager(4,all_sprites)
    red_alien_manager=RedalienManager(3,all_sprites)
    
    enemies_list=[green_alien_manager.enemies,red_alien_manager.enemies]
    enemies_list = pygame.sprite.Group(enemies_list)
    bullets = pygame.sprite.Group()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Detecta si se presiona ESC
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Detecta si se presiona ESC
                    game_functions.GameFunctions.shoot(player, all_sprites, bullets)
                      
        
        all_sprites.update()
        shooted = game_functions.GameFunctions.shoot_impact(enemies_list,bullets)
        colission= game_functions.GameFunctions.colission_detection(player,enemies_list)
        if colission:
            running = False

        screen.blit(bg,[0,0])
        all_sprites.draw(screen) 
        pygame.display.flip()
    pygame.quit()    






if __name__== "__main__":
    main()