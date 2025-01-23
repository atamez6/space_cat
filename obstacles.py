
import settings

import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path="assets/images/avatars/planeta.png"):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Tamaño ajustado
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 100  # Vida del obstáculo

    def take_damage(self):
        self.health -= 50  # Reduce la vida
        if self.health <= 0:
            self.kill()  # Elimina el obstáculo si su vida es 0 o menos

    def update(self):
        pass  # Los obstáculos no tienen movimiento