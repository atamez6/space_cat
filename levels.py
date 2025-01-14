import pygame
import settings
from  game_functions import *


class levels:

    def level_changer(self,surface, score):
        self.level = 1
        game_functions = GameFunctions()
        
        if score > 300:
            self.level = 2
        if score > 400:
            self.level = 3
        if score > 500:
            game_functions.draw_text(surface, "Has Ganado!!", 100, settings.WIDTH // 2 , 40)
            
        game_functions.draw_text(surface, f"{self.level}", 25, settings.WIDTH // 2 , 35)
