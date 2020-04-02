import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, sy, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect (0, 0, sy.bullet_width, sy.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)


        #self.rect = pygame.Rect (0, 0, sy.bullet_width, sy.bullet_height)
        #self.rect.centerx = ship.rect.centerx
       # self.rect.top = ship.rect.top

        #self.x = float(self.rect.x)


        self.color = sy.bullet_color
        self.speed_factor = sy.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

        #self.x -= self.speed_factor
        #self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

