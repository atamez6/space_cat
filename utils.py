import pygame, settings, random


class Background():
    @staticmethod
    def background():
        background = pygame.image.load("assets/images/backgrounds/1.png").convert()
        return pygame.transform.scale(background, (800, 600))
    @staticmethod
    def background2():
        background = pygame.image.load("assets/images/backgrounds/2.png").convert()
        return pygame.transform.scale(background, (800, 600))

class Sounds():
    @staticmethod
    def music_main():
        pygame.mixer.music.load("assets/sounds/music.wav")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.6)
    
    @staticmethod
    def collision_sound():
        # Sonido de colisión
        collision = pygame.mixer.Sound("assets/sounds/collision.wav")
        collision.set_volume(0.6)
        collision.play()

    @staticmethod
    def shoot_sound():
        # Sonido de disparo
        shoot = pygame.mixer.Sound("assets/sounds/shoot.wav")
        shoot.set_volume(0.6)
        shoot.play()
    def play_banana_power_sound():
        banana_power = pygame.mixer.Sound("assets/sounds/banana_power.wav")
        banana_power.set_volume(0.6)
        banana_power.play()
    
from game_functions import GameFunctions

class screen_no_game():
    
    @staticmethod
    def screen(screen,clock):
        screen.blit(Background.background2(), [0, 0])
        overlay = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        overlay.set_alpha(128)
        screen.blit(overlay, [0, 0])
        GameFunctions.draw_text(screen, "Space Cat!", 75, settings.WIDTH // 2, settings.HEIGHT // 4)
        GameFunctions.draw_text(screen, "Press Space to start!", 75, settings.WIDTH // 2, settings.HEIGHT // 2 )
        GameFunctions.draw_text(screen, "instructions => Help the Space Cat to reach 13 Level! The Banana is ally!", 25, settings.WIDTH // 2, settings.HEIGHT // 2 + 80)
        pygame.display.flip()
        seleccionando = True
        while seleccionando:
            
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        seleccionando = False
    @staticmethod
    def screen_win(screen,clock):
        screen.blit(Background.background2(), [0, 0])
        overlay = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        overlay.set_alpha(128)
        screen.blit(overlay, [0, 0])
        GameFunctions.draw_text(screen, "You Win!", 75, settings.WIDTH // 2, settings.HEIGHT // 4)
        GameFunctions.draw_text(screen, "Space Cat!", 75, settings.WIDTH // 2, settings.HEIGHT // 2 )
        GameFunctions.draw_text(screen, "Press Space to restart!", 25, settings.WIDTH // 2, settings.HEIGHT // 2 + 80)
        pygame.display.flip()
        seleccionando = True
        while seleccionando:
            
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        seleccionando = False

    @staticmethod
    def screen_lost(screen,clock):
        screen.blit(Background.background2(), [0, 0])
        overlay = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        overlay.set_alpha(128)
        screen.blit(overlay, [0, 0])
        GameFunctions.draw_text(screen, "Game Over!", 75, settings.WIDTH // 2, settings.HEIGHT // 4)
        GameFunctions.draw_text(screen, "Space Cat!", 75, settings.WIDTH // 2, settings.HEIGHT // 2 )
        GameFunctions.draw_text(screen, "Press Space to restart!", 25, settings.WIDTH // 2, settings.HEIGHT // 2 + 80)

        pygame.display.flip()
        seleccionando = True
        while seleccionando:
            
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        seleccionando = False
                        return True