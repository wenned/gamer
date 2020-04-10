import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def check_keyup_events(event, sy, screen, ship, bullets):

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



def update_screen(settings, screen, ship, aliens, bullets):
    screen.fill(settings.bg)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    
    pygame.display.flip()

def update_bullets(bullets):

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
   
    bullets.update()

def get_num_ali_x(sy, alien_width):
    available_sp_x = sy.screen_w - 2 * alien_width
    num_ali_x = int(available_sp_x / (2 * alien_width))
    return num_ali_x


def creat_alien(sy, screen, aliens, alien_nu):
    alien = Alien(sy, screen)
    alien_w = alien.rect.width
    alien.x = alien_w + 2 * alien_w * alien_nu
    alien.rect.x = alien.x
    aliens.add(alien)

def creat_fleet(sy, screen, aliens):
    alien = Alien(sy, screen)
    number_ali_x = get_num_ali_x(sy, alien.rect.width)

    for alien_n in range(number_ali_x):
        creat_alien(sy, screen, aliens, alien_n)

