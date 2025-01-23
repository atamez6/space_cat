import pygame
import settings
from enemies import *
from player import *
from obstacles import Obstacle


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/avatars/banana.png").convert_alpha()
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
    
    def banana_effect(self, enemies_list, green_manager, red_manager, level_manager):
        # Contar enemigos eliminados
        eliminated_count = len(enemies_list)

        # Incrementar el puntaje proporcionalmente
        self._score_ += eliminated_count * 25

        # Eliminar todos los enemigos
        for enemy in enemies_list:
            enemy.kill()

        # Subir solo un nivel
        if eliminated_count > 0:
            print(f"¡Banana recogida! Eliminaste {eliminated_count} enemigos.")
            level_manager.level += 1  # Incrementar solo un nivel
            level_manager.level_up_sound.play()  # Reproducir sonido de nivel
            green_manager.add_enemy(level_manager.level)
            if level_manager.level >= 3:  # Ajustar para niveles altos
                red_manager.add_enemy(level_manager.level // 2)  # Menos enemigos rojos

        print(f"Nuevo nivel: {level_manager.level}")

        
    def spawn_obstacles(self, obstacle_group, all_sprites, center_only=True):
        for _ in range(2):  # Generar dos obstáculos
            if center_only:
                x = random.randint(settings.WIDTH // 3, (settings.WIDTH * 2) // 3)
                y = random.randint(settings.HEIGHT // 3, (settings.HEIGHT * 2) // 3)
            else:
                x = random.randint(50, settings.WIDTH - 50)
                y = random.randint(50, settings.HEIGHT - 50)
            obstacle = Obstacle(x, y)
            obstacle_group.add(obstacle)
            all_sprites.add(obstacle)
            
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






class Banana(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/avatars/banana.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajustar tamaño
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = random.randint(2, 4)  # Velocidad vertical aleatoria

    def update(self):
        self.rect.y += self.speed_y  # Movimiento vertical
        if self.rect.top > settings.HEIGHT:  # Si sale de la pantalla
            self.kill()  # Elimina la banana del grupo de sprites

    @staticmethod
    def spawn_randomly(width, height):
        x = random.randint(0, width - 50)  # Posición horizontal aleatoria
        y = -50  # Comienza fuera de la pantalla
        return Banana(x, y)