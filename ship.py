import pygame

class Ship:

    def __init__(self, sy, screen):
        self.sy = sy
        self.screen = screen
        
        
        self.image = pygame.image.load('imagens/nave.bmp')
        self.rect = self.image.get_rect()
        self.screen_r = screen.get_rect()

        self.rect.centerx = self.screen_r.centerx
        self.rect.bottom = self.screen_r.bottom
                
        self.c = float(self.rect.centerx)

        #flag de movimento
        self.mov_r = False
        self.mov_l = False

    def update(self):
        
        if self.mov_r and self.rect.right < self.screen_r.right:
            self.c += self.sy.ship_speed
        if self.mov_l and self.rect.left > 0:
            self.c -= self.sy.ship_speed

        self.rect.centerx = self.c
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

