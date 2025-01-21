import pygame
import settings
from enemies import *
from player import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/avatars/banana_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 20))  # Tamaño ajustado
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:  # Eliminar la bala cuando salga de la pantalla
            self.kill()


    



class GameFunctions:
    

    def __init__(self):
        self._score_ = 0  # Inicializa el puntaje en 0
    @staticmethod
    def draw_text(surface, text, size, x, y):
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, settings.GRAY)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)
    
    @staticmethod
    def draw_live_board(surface, x, y,live):
        bar = (live/100) * settings.BAR_LENGHT
        borders = pygame.Rect(x,y,settings.BAR_LENGHT,settings.BAR_HEIGHT)
        bar = pygame.Rect(x,y,bar,settings.BAR_HEIGHT)
        pygame.draw.rect(surface,settings.YELLOW,bar)
        pygame.draw.rect(surface,settings.WHITE,borders, 3)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render('Life', True, settings.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x + settings.BAR_LENGHT // 2, y + settings.BAR_HEIGHT + 5)  # Ajustar debajo de la barra

        surface.blit(text_surface, text_rect)
        


    def shoot(self, player, all_sprites, bullets):
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def shoot_impact(self, enemies_list, bullets):
        impacts = pygame.sprite.groupcollide(enemies_list, bullets, True, True)
        for impact in impacts:
            self._score_ += 25  # Incrementar el puntaje


    def colission_detection(self, player, enemies, green_manager, red_manager):
        from enemies import Greenalien, Redalien
        collision = pygame.sprite.spritecollide(player, enemies, True)
        for hit in collision:
            print(player.live_player)
            player.live_player -=25
                    # Identificar el tipo de enemigo

            if isinstance(hit, Greenalien):
                print("Colisionaste con un alien verde.")
                green_manager.add_enemy(1)
                
                
            if isinstance(hit, Redalien):
                print("Colisionaste con un alien rojo.")
                red_manager.add_enemy(1)
                

            if player.live_player == 0:
                return False
            
        return True



    def get_score(self):
        return self._score_
