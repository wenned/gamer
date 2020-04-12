import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_funcoes as gf

def run_game():
    pygame.init()
    sy = Settings()
    screen = pygame.display.set_mode((sy.screen_w, sy.screen_h))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(sy, screen, 'Play')
    stats = GameStats(sy)
    ship = Ship(sy, screen)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(sy, screen, ship, aliens)
    
    while True:

        gf.check_events(sy, screen, stats, play_button, ship, aliens, bullets)
      
        if stats.game_active:
            ship.update()
            gf.update_bullets(sy, screen, ship, aliens, bullets)
            gf.update_aliens(sy, stats, screen, ship, aliens, bullets)             
            gf.update_screen(sy, screen, stats, ship, aliens, bullets, play_button)
           
        gf.update_screen(sy, screen, stats, ship, aliens, bullets, play_button)
 
run_game()


