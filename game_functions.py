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
        self._score_ = 0  # Inicializa el puntaje en 0
    @staticmethod
    def draw_text(surface, text, size, x, y):
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, settings.GRAY)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    def shoot(self, player, all_sprites, bullets):
        bullet = Bullet(player.rect.centerx, player.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def shoot_impact(self, enemies_list, bullets):
        impacts = pygame.sprite.groupcollide(enemies_list, bullets, True, True)
        for impact in impacts:
            self._score_ += 25  # Incrementar el puntaje
            print(f"Enemigo impactado, nuevo puntaje: {self._score_}")  # DEBUG

    def colission_detection(self, player, enemies):
        collision = pygame.sprite.spritecollide(player, enemies, True)
        if collision:
            print("Colisión detectada, fin del juego.")  # DEBUG
            return True
        return False


    def get_score(self):
        return self._score_
