import pygame, settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   
        self.image = pygame.image.load("assets/images/avatars/player_cat.png").convert_alpha()
        image_resize = (80, 80)  # Cambiar al tamaño deseado
        self.image = pygame.transform.scale(self.image, image_resize)
        

        self.rect = self.image.get_rect()
        shrink_factor = 0.8
        self.rect.width = int(self.rect.width * shrink_factor)
        self.rect.height = int(self.rect.height * shrink_factor)
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)  # Centro de la pantalla

        self.rect.bottom = settings.HEIGHT - 10
        self.speed_axe_x = 0
        self.live_player = 100


    def update(self):
        self.speed_axe_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_axe_x = -6
        if keystate[pygame.K_RIGHT]:
            self.speed_axe_x = 5
        self.rect.x += self.speed_axe_x

        if self.rect.right > settings.WIDTH:
            self.rect.right = settings.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0