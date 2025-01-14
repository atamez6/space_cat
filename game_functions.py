import pygame

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
    def colission_detection(player,enemies):
        colission= pygame.sprite.spritecollide(player,enemies, True)
        if colission:
            return True
            
    def shoot(player, all_sprites, bullets):
        # Crear una bala en las coordenadas del jugador
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)  # Agregar la bala al grupo de todos los sprites
        bullets.add(bullet) 
        

    def shoot_impact(enemies_list, bullets):
        impacts = pygame.sprite.groupcollide(enemies_list, bullets, True, True)
        for impact in impacts:
            return True