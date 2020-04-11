import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, sy, screen):
        
        super(Alien, self).__init__()
        self.screen = screen
        self.sy = sy

        self.image = pygame.image.load('imagens/alie1.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        
        elif self.rect.left <= 0:
            return True

    def update(self):
        
        self.x += (self.sy.alien_speed * self.sy.fleet_direction)
        self.rect.x = self.x


