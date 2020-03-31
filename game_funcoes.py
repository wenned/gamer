import sys
import pygame

def check_events(ship):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                ship.mov_r = True
            
            elif events.key == pygame.K_LEFT:
                ship.mov_l = True

        elif events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT:
                ship.mov_r = False

            elif events.key == pygame.K_LEFT:
                ship.mov_l = False
            
def update_screen(settings, screen, ship):
    screen.fill(settings.bg)
    ship.blitme()

    pygame.display.flip()
