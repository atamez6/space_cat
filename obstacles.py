
import settings

import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load('assets/images/avatars/planeta.png').convert_alpha()
        self.image_resize = (80, 80)  # Cambiar al tamaño deseado
        self.image = pygame.transform.scale(self.image, self.image_resize)
        self.rect = self.image.get_rect(center=(x, y))
        shrink_factor = 0.7  # Ajusta este valor según lo necesario
        self.rect.width = int(self.rect.width * shrink_factor)
        self.rect.height = int(self.rect.height * shrink_factor)
        self.rect.center = (x, y)  # Reajustar la posición al centro

    def update(self):
        pass  # Obstáculos estáticos no necesitan actualización
