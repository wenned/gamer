import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.mov_r = True
            
    elif event.key == pygame.K_LEFT:
        ship.mov_l = True

def check_keyup_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.mov_r = False

    elif event.key == pygame.K_LEFT:
        ship.mov_l = False
            
def check_events(ship):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(settings, screen, ship):
    screen.fill(settings.bg)
    ship.blitme()

    pygame.display.flip()
