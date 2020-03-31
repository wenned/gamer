import pygame
from settings import Settings
from ship import Ship
import game_funcoes as gf

def run_game():
    pygame.init()
    sy = Settings()
    screen = pygame.display.set_mode((sy.screen_w, sy.screen_h))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(sy, screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(sy, screen, ship)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sy.sys.exit()
        
        screen.fill(sy.bg)
        ship.blitme()
        pygame.display.flip()

run_game()
