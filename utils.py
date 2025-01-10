import pygame, settings, random

class Background():
    @staticmethod
    def background():
        background = pygame.image.load("assets/images/backgrounds/1.png").convert()
        return pygame.transform.scale(background, (800, 600))