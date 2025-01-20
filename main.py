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
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Space Cat!")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player()
    bg = Background.background()
    all_sprites.add(player)

    green_alien_manager = GreenalienManager(6, all_sprites)
    red_alien_manager = RedalienManager(0, all_sprites)
    enemies_list = pygame.sprite.Group(*green_alien_manager.enemies,*red_alien_manager.enemies)
    largo=len(green_alien_manager.enemies)
    bullets = pygame.sprite.Group()
    game_functions = GameFunctions()
    level_manager = Levels()
    running = True

    while running:
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
        game_functions.shoot_impact(enemies_list, bullets)
        if game_functions.colission_detection(player, enemies_list):
            running = False

        # Cambiar nivel y generar enemigos adicionales

        if level_manager.check_level_up(game_functions.get_score()):
            if level_manager.level <= 2:
                
                    
 
                green_alien_manager.add_enemy(largo)
            if level_manager.level in [3,4]:
                green_alien_manager.add_enemy(int(largo/2))
                red_alien_manager.add_enemy(int(largo/4))
                largo += 1
            if level_manager.level in [5,6,7,8]:
                green_alien_manager.add_enemy(int(largo/3))
                red_alien_manager.add_enemy(int(largo/2))
                largo += 1

            if level_manager.level in [9,10]:
                red_alien_manager.add_enemy(int(largo/2))
                largo += 2

            if level_manager.level > 10:
                print('ganaste')
                
            # Actualizar lista de enemigos
            
            enemies_list = pygame.sprite.Group(*green_alien_manager.enemies, *red_alien_manager.enemies)
            print(f"Nueva lista de enemigos generada: {len(enemies_list)} enemigos para Nivel {level_manager.level}")  # DEBUG

        # Dibujar todo en pantalla
        screen.blit(bg, [0, 0])
        all_sprites.draw(screen)
        game_functions.draw_text(screen, f"Puntaje: {game_functions.get_score()}", 25, settings.WIDTH // 2, 10)
        level_manager.draw_level(screen)
        pygame.display.flip()

    pygame.quit()





if __name__== "__main__":
    main()