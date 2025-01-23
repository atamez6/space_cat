#!/usr/bin/env python

import settings, pygame, sys
from utils import Background,Sounds
from player import Player
from enemies import *
from  game_functions import *
from levels import *
from obstacles import Obstacle

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Space Cat!")
    clock = pygame.time.Clock()

   
    bg = Background.background()
    music = Sounds.music_main()
    banana_group = pygame.sprite.Group()
    banana_spawn_timer = random.randint(6000, 12000)  # Tiempo en milisegundos entre 6-12 segundos
    pygame.time.set_timer(pygame.USEREVENT + 1, banana_spawn_timer)


    running = True
    game_over = True
    while running:
        if game_over:
            utils.screen_no_game.screen(screen, clock)
            game_over = False
            all_sprites = pygame.sprite.Group()
            obstacle_group = pygame.sprite.Group()
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
            if event.type == pygame.USEREVENT + 1:
                new_banana = Banana.spawn_randomly(settings.WIDTH, settings.HEIGHT)
                banana_group.add(new_banana)
                all_sprites.add(new_banana)

        # Actualizar sprites
        all_sprites.update()

        # Verificar impactos y colisiones
        game_functions.shoot_impact(enemies_list, bullets,all_sprites)
        enemies_list = pygame.sprite.Group(*green_alien_manager.enemies, *red_alien_manager.enemies)

        live_after_colission =  game_functions.colission_detection(player, enemies_list, green_alien_manager, red_alien_manager,all_sprites)
        if not live_after_colission:
            utils.screen_no_game.screen_lost(screen, clock)
            game_over = True
        
        collected_banana = pygame.sprite.spritecollideany(player, banana_group)
        if collected_banana:
            Sounds.play_banana_power_sound()  # Reproducir el sonido
            collected_banana.kill()  # Eliminar la banana
            game_functions.banana_effect(enemies_list, green_alien_manager, red_alien_manager, level_manager)  # Aplicar efecto
            enemies_list = pygame.sprite.Group(*green_alien_manager.enemies, *red_alien_manager.enemies)
        
        if game_functions.get_score() % 200 == 0 and len(obstacle_group) == 0:
            game_functions.spawn_obstacles(obstacle_group, all_sprites,center_only=True)

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
        game_functions.draw_text(screen, f"Score: {game_functions.get_score()}", 25, settings.WIDTH // 2, 10)
        game_functions.draw_live_board(screen,5,5,player.live_player)
        level_manager.draw_level(screen)
        pygame.display.flip()

    pygame.quit()





if __name__== "__main__":
    main()