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

