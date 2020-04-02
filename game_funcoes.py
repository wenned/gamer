import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, sy, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.mov_r = True

    elif event.key == pygame.K_LEFT:
        ship.mov_l = True
    
    elif event.key == pygame.K_SPACE: 
        fire_bullet(sy, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()
 
def fire_bullet(sy, screen, ship, bullets):
        
    if len(bullets) < sy.bullets_allowed:
        new_bullet = Bullet(sy, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, sy,screen, ship, bullets):

    if event.key == pygame.K_RIGHT:
        ship.mov_r = False

    elif event.key == pygame.K_LEFT:
        ship.mov_l = False
            
def check_events(sy, screen, ship, bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
       
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sy, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, sy, screen, ship, bullets)



def update_screen(settings, screen, ship, alien, bullets):
    screen.fill(settings.bg)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

    pygame.display.flip()

def update_bullets(bullets):

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


    


    
    bullets.update()
