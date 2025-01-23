import pygame, settings, random, levels

class Enemies(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        image_resize = (80, 80)  # Cambiar al tamaño deseado
        self.image = pygame.transform.scale(self.image, image_resize)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(settings.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        
        
        self.speed_axe_y = 0
        self.speed_axe_x = 0

    def update(self):
        self.rect.y += self.speed_axe_y
        self.rect.x += self.speed_axe_x
        if self.rect.left < 0 or self.rect.right > settings.WIDTH:  # Rebota en los bordes
            self.speed_axe_x = -self.speed_axe_x
        if self.rect.top > settings.HEIGHT + 9:
            self.rect.x = random.randrange(settings.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-140, -100)
            
            
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
        self.num_enemies = num_enemies
        for _ in range(num_enemies):
            self.add_enemy(1)

# Agregar enemigos según el nivel
    def add_enemy(self, level):
        for _ in range(level):  # Generar más enemigos según el nivel
            enemy = Greenalien()
            enemy.speed_axe_y = random.randint(1, 2) 
            enemy.speed_axe_x = random.randint(-2, 1)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
            print(f"Enemigo añadido: Nivel {level}, Total: {len(self.enemies)}")  # DEBUG

class RedalienManager:
    def __init__(self, num_enemies, all_sprites_group):
        self.enemies = pygame.sprite.Group()
        self.all_sprites = all_sprites_group
        self.num_enemies = num_enemies
        for _ in range(num_enemies):
            self.add_enemy(1)
    def add_enemy(self, level):
        for _ in range(level):  # Generar más enemigos según el nivel
            enemy = Redalien()
            enemy.speed_axe_y = random.randint(3, 4) 
            enemy.speed_axe_x = random.randint(2, 4)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
            print(f"Enemigo añadido: Nivel {level}, Total: {len(self.enemies)}")  # DEBUG

