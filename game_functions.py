import pygame
import settings
from enemies import *
from player import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/avatars/banana_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 24))  # Tamaño ajustado
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -12

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:  # Eliminar la bala cuando salga de la pantalla
            self.kill()


    


from utils import Sounds
class GameFunctions:
    
    
    def __init__(self):
        self._score_ = 0  # Inicializa el puntaje en 0
    @staticmethod
    def draw_text(surface, text, size, x, y):
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, settings.YELLOW)
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
        collision_sound = Sounds.shoot_sound()

    def shoot_impact(self, enemies_list, bullets, all_sprites):
        impacts = pygame.sprite.groupcollide(enemies_list, bullets, True, True)
        for impact in impacts:
            collision_sound = Sounds.collision_sound()
            explosion = Explosion(impact.rect.center)
            all_sprites.add(explosion)
            self._score_ += 25  # Incrementar el puntaje


    def colission_detection(self, player, enemies, green_manager, red_manager,all_sprites):
        from enemies import Greenalien, Redalien
        
        collision = pygame.sprite.spritecollide(player, enemies, True)
        for hit in collision:
            collision_sound = Sounds.collision_sound()
            explosion = Explosion(hit.rect.center)
            all_sprites.add(explosion)
            player.live_player -=25
            print(player.live_player)
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

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center):
        super().__init__()
        self.explosion_animation_list = []
        self.explosion_animation()  # Inicializar la lista de animaciones
        self.image = self.explosion_animation_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate  = 55

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_animation_list):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_animation_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


    def explosion_animation(self):
        self.explosion_animation_list = []
        for i in range(1,4):
            file=f"assets/images/images/explosion{i}.png"
            img = pygame.image.load(file).convert_alpha()
            img.set_colorkey(settings.BLACK)
            img_scale = pygame.transform.scale(img, (80, 80))
            self.explosion_animation_list.append(img_scale)
