#!/usr/bin/env python

import settings, pygame, sys
from player import Player

def main():
    pygame.init()
    pygame.mixer.init()
    screen  = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
    pygame.display.set_caption("Space Cat!")
    clock = pygame.time.Clock()


    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Detecta si se presiona ESC
                    pygame.quit()
                    sys.exit() 
        
        all_sprites.update()
        screen.fill(settings.BLACK)
        all_sprites.draw(screen) 
        pygame.display.flip()
    pygame.quit()    






if __name__== "__main__":
    main()