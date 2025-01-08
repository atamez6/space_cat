import pygame, settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   
        self.image = pygame.image.load("assets/images/avatars/green_alien.png").convert_alpha()
        image_resize = (80, 80)  # Cambiar al tamaño deseado
        self.image = pygame.transform.scale(self.image, image_resize)

        #self.image.set_colorkey((255, 255, 255))  # Blanco
        #self.image.set_colorkey((0, 0, 0))  # Negro

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)  # Centro de la pantalla

        #self.rect.centerx = settings.WIDTH // 2
        self.rect.bottom = settings.HEIGHT - 10
        self.speed_axe_x = 0
