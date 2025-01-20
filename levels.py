import pygame
import settings
from  game_functions import *
from enemies import *

class Levels:
    def __init__(self):
        self.level = 1
        self.base_score = 125  # Puntaje base para el nivel 1
        self.next_level_score = self.base_score  # Puntaje requerido para el siguiente nivel
        self.level_up_sound = pygame.mixer.Sound("assets/sounds/level_up.wav")

    def check_level_up(self, score):
        # Comparar el puntaje actual con el puntaje requerido para subir de nivel
        if score >= self.next_level_score:
            self.level += 1
            self.level_up_sound.play()  # Reproducir sonido al subir de nivel
            print(f"Subiendo al nivel {self.level}")  # DEBUG
            # Incrementar el puntaje requerido para el próximo nivel
            self.next_level_score += self.base_score
            return True
        return False

    def draw_level(self, surface):
        # Dibujar el nivel actual en pantalla
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(f"Nivel: {self.level}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(settings.WIDTH // 2, 35))
        surface.blit(text_surface, text_rect)

    def increase_difficulty(self, green_manager, red_manager):
    # Incrementar velocidad de los enemigos existentes
        for enemy in green_manager.enemies:
            enemy.speed_axe_y = min(enemy.speed_axe_y + 1, 10)  # Limitar la velocidad máxima
        for enemy in red_manager.enemies:
            enemy.speed_axe_y = min(enemy.speed_axe_y + 2, 15)  # Limitar la velocidad máxima

        # Agregar enemigos adicionales
        #if enemy menor a 3 solo verde mayor a 3 sale rojo y en el 5 salen banana y aliens

        for _ in range(self.level):  # Agregar enemigos igual al nivel actual
            green_manager.add_enemy(self.level)
            red_manager.add_enemy(self.level)
