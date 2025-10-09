import sys 
import pygame 

from settings import Setting
from ship import Ship 

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        
        self.settings = Setting()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

#Fuera de la clase
if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()