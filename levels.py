import pygame, utils, player
import game_functions

import settings

from enemies import *

class Levels:
    def __init__(self):
        self.level = 1
        self.level_up_sound = pygame.mixer.Sound("assets/sounds/level.wav")

    def check_level_up(self, green_manager, red_manager):
        # Subir de nivel si no hay más enemigos
        if len(green_manager.enemies) == 0 and len(red_manager.enemies) == 0:
            self.level += 1
            self.level_up_sound.play()  # Reproducir sonido al subir de nivel
            print(f"Subiendo al nivel {self.level}")  # DEBUG
            return True
        return False

    def draw_level(self, surface):
        # Dibujar el nivel actual en pantalla
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(f"Level: {self.level}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(settings.WIDTH // 2, 35))
        surface.blit(text_surface, text_rect)


    def increase_difficulty(self, green_manager, red_manager,screen,bg,clock):

        # Incrementar velocidad de los enemigos existentes
        for enemy in green_manager.enemies:
            enemy.speed_axe_y = min(enemy.speed_axe_y + 1, 10)  # Limitar la velocidad máxima
        for enemy in red_manager.enemies:
            enemy.speed_axe_y = min(enemy.speed_axe_y + 2, 15)  # Limitar la velocidad máxima

        # Generar enemigos adicionales según el nivel
        if self.level == 2:
            green_manager.add_enemy(self.level+2)
        elif self.level in [3, 4]:
            green_manager.add_enemy(self.level)
            red_manager.add_enemy(self.level // 2 +1)
        elif self.level in [5, 9]:
            green_manager.add_enemy(self.level // 2 +1)
            red_manager.add_enemy(self.level)
        elif self.level == 13:
            utils.screen_no_game.screen_win(screen, clock)
            return False
        return True
 

  