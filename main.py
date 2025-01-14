#!/usr/bin/env python

import settings, pygame, sys
from utils import Background
from player import Player
from enemies import *
from  game_functions import *
from levels import *

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

    game_functions = GameFunctions()
    level = levels()
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
                    game_functions.shoot(player, all_sprites, bullets)
                      
        
        all_sprites.update()
        shooted = game_functions.shoot_impact(enemies_list,bullets)
        colission= game_functions.colission_detection(player,enemies_list)
        if colission:
            running = False

        screen.blit(bg,[0,0])
        all_sprites.draw(screen)
        score = game_functions.get_score()
        level_changer = level.level_changer(screen,score)
        draw_score= game_functions.draw_text(screen, f"Score: {score}", 25, settings.WIDTH // 2, 10)
   
        
 
        pygame.display.flip()
    pygame.quit()    






if __name__== "__main__":
    main()