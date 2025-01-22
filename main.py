#!/usr/bin/env python

import settings, pygame, sys
from utils import Background,Sounds
from player import Player
from enemies import *
from  game_functions import *
from levels import *


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Space Cat!")
    clock = pygame.time.Clock()

   
    bg = Background.background()
    music = Sounds.music_main()

    running = True
    game_over = True
    while running:
        if game_over:
            utils.screen_no_game.screen(screen, clock)
            game_over = False
            all_sprites = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)

            green_alien_manager = GreenalienManager(2, all_sprites)
            red_alien_manager = RedalienManager(0, all_sprites)
            enemies_list = pygame.sprite.Group(*green_alien_manager.enemies,*red_alien_manager.enemies)
            bullets = pygame.sprite.Group()
            game_functions = GameFunctions()
            level_manager = Levels()
        
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    game_functions.shoot(player, all_sprites, bullets)

        # Actualizar sprites
        all_sprites.update()

        # Verificar impactos y colisiones
        game_functions.shoot_impact(enemies_list, bullets,all_sprites)
        enemies_list = pygame.sprite.Group(*green_alien_manager.enemies, *red_alien_manager.enemies)

        live_after_colission =  game_functions.colission_detection(player, enemies_list, green_alien_manager, red_alien_manager,all_sprites)
        if not live_after_colission:
            utils.screen_no_game.screen_lost(screen, clock)
            game_over = True


        # Cambiar nivel y generar enemigos adicionales

        # Verificar si se sube de nivel
        if level_manager.check_level_up(green_alien_manager, red_alien_manager):
            lm=level_manager.increase_difficulty(green_alien_manager, red_alien_manager,screen,bg,clock)
            enemies_list = pygame.sprite.Group(*green_alien_manager.enemies, *red_alien_manager.enemies)
            print(f"Nueva lista de enemigos generada: {len(enemies_list)} enemigos para Nivel {level_manager.level}")  # DEBUG

            if not lm:
                game_over = True

            
            # Actualizar lista de enemigos

                # Dibujar todo en pantalla
        screen.blit(bg, [0, 0])
        all_sprites.draw(screen)
        game_functions.draw_text(screen, f"Puntaje: {game_functions.get_score()}", 25, settings.WIDTH // 2, 10)
        game_functions.draw_live_board(screen,5,5,player.live_player)
        level_manager.draw_level(screen)
        pygame.display.flip()

    pygame.quit()





if __name__== "__main__":
    main()