import pygame, settings, random

class Enemies(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        image_resize = (80, 80)  # Cambiar al tamaño deseado
        self.image = pygame.transform.scale(self.image, image_resize)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(settings.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        
        
        self.speed_axe_y = 0
        self.speed_axe_x = 0

    def update(self):
        self.rect.y += self.speed_axe_y
        self.rect.x += self.speed_axe_x
        if self.rect.left < 0 or self.rect.right > settings.WIDTH:  # Rebota en los bordes
            self.speed_axe_x = -self.speed_axe_x
        if self.rect.top > settings.HEIGHT + 9:
            self.rect.x = random.randrange(settings.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            
            
class Redalien(Enemies):
    def __init__(self):
        super().__init__("assets/images/avatars/red_alien.png")

class Greenalien(Enemies):
    def __init__(self):
        super().__init__("assets/images/avatars/green_alien.png")

class GreenalienManager:
    def __init__(self, num_enemies, all_sprites_group):
        self.enemies = pygame.sprite.Group()
        self.all_sprites = all_sprites_group

        for _ in range(num_enemies):
            enemy = Greenalien()

            enemy.speed_axe_y = random.randrange(1,2)
            enemy.speed_axe_x = random.randrange(-2,2)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)  # Añadir también al grupo principal

    def update(self):
        self.enemies.update()
           

            


class RedalienManager:
    def __init__(self, num_enemies, all_sprites_group):
        self.enemies = pygame.sprite.Group()
        self.all_sprites = all_sprites_group

        for _ in range(num_enemies):
            enemy = Redalien()

            enemy.speed_axe_y = random.randrange(3,5)
            enemy.speed_axe_x = random.randrange(-4,4)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)  # Añadir también al grupo principal

    def update(self):
        self.enemies.update()