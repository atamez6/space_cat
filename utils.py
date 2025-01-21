import pygame, settings, random

class Background():
    @staticmethod
    def background():
        background = pygame.image.load("assets/images/backgrounds/1.png").convert()
        return pygame.transform.scale(background, (800, 600))

class Sounds():
    @staticmethod
    def music_main():
        pygame.mixer.music.load("assets/sounds/music.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.6)