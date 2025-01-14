import pygame
import settings

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
        self._total_score_ = 0000

    def colission_detection(self,player,enemies):
        colission= pygame.sprite.spritecollide(player,enemies, True)
        if colission:
            return True
            
    def shoot(self,player, all_sprites, bullets):
        # Crear una bala en las coordenadas del jugador
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)  # Agregar la bala al grupo de todos los sprites
        bullets.add(bullet) 
        

    def shoot_impact(self,enemies_list, bullets):
        impacts = pygame.sprite.groupcollide(enemies_list, bullets, True, True)
        for impact in impacts:
            self._total_score_ += 100

            return True
        
    def get_score(self):
        return int(self._total_score_) 
        
    def draw_text(self,surface, text, size, x, y):
        font = pygame.font.SysFont("",size)
        text_to_box = font.render(text,True, settings.GRAY)
        text_rect = text_to_box.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_to_box,text_rect)