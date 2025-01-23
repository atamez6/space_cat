
import pygame
import settings

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50):
        super().__init__()
        self.image = pygame.image.load("assets/images/avatars/banana.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
