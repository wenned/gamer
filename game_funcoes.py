import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


            
def check_events(sy, screen, stats, play_button, ship, aliens, bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
       
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(sy, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sy, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, sy, screen, ship, bullets)

def check_play_button(sy, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):


    clic = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if clic and not stats.game_active:

        sy.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True
        
        aliens.empty()
        bullets.empty()

        creat_fleet(sy, screen, ship, aliens)
        ship.center_ship()

def check_keydown_events(event, sy, screen, ship, bullets):
    
    if event.key == pygame.K_RIGHT:
        ship.mov_r = True

    elif event.key == pygame.K_LEFT:
        ship.mov_l = True
    
    elif event.key == pygame.K_SPACE: 
        fire_bullet(sy, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()
 
def check_keyup_events(event, sy, screen, ship, bullets):

    if event.key == pygame.K_RIGHT:
        ship.mov_r = False

    elif event.key == pygame.K_LEFT:
        ship.mov_l = False

def fire_bullet(sy, screen, ship, bullets):
        
    if len(bullets) < sy.bullets_allowed:
        new_bullet = Bullet(sy, screen, ship)
        bullets.add(new_bullet)

def update_screen(sy, screen, stats, sb, ship, aliens, bullets, play_button):
    
    screen.fill(sy.bg)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)
    
    sb.show_score()   # desenha a informação sobre a pontuação

    if not stats.game_active:
        play_button.draw_button()


    pygame.display.flip()

def update_bullets(sy, screen, stats, sb, ship, aliens, bullets):

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collision(sy, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collision(sy, screen,stats, sb, ship, aliens, bullets):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        
        for aliens in collisions.values():
            stats.score += sy.alien_points * len(aliens)
            sb.prep_score()
        
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        sy.increase_speed()
        creat_fleet(sy, screen, ship, aliens)

    bullets.update()

def get_num_ali_x(sy, alien_width):
    
    available_sp_x = sy.screen_w - 2 * alien_width
    num_ali_x = int(available_sp_x / (1.8 * alien_width))
    return num_ali_x

def creat_alien(sy, screen, aliens, alien_nu, row_number):
    
    alien = Alien(sy, screen)
    alien_w = alien.rect.width
    alien.x = alien_w + 2 * alien_w * alien_nu
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(sy, screen, ship, aliens):
    
    alien = Alien(sy, screen)
    number_ali_x = get_num_ali_x(sy, alien.rect.width)
    number_rows = get_nu_rows(sy, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_n in range(number_ali_x):
            creat_alien(sy, screen, aliens, alien_n, row_number)

def get_nu_rows(sy, ship_h, alien_h):
    
    available_sp_y = (sy.screen_h -(3* alien_h) - ship_h)
    number_rows = int(available_sp_y / (2* alien_h))
    return number_rows

def check_aliens_bottom(sy, stats, screen, ship, aliens, bullets):

    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(sy, stats, screen, ship, aliens, bullets)
            break

def update_aliens(sy, stats, screen, ship, aliens, bullets):
    
    fleet_edges(sy, aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(sy, stats, screen, ship, aliens, bullets)
    
    check_aliens_bottom(sy, stats, screen, ship, aliens, bullets)

def fleet_edges(sy, aliens):

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(sy, aliens)
            break

def change_fleet_direction(sy, aliens):

    for alien in aliens.sprites():
        alien.rect.y += sy.fleet_drop
    sy.fleet_direction *= -1

def ship_hit(sy, stats, screen, ship, aliens, bullets):
    
    if stats.ships_l > 0:
        stats.ships_l -= 1

        aliens.empty()
        bullets.empty()

        creat_fleet(sy, screen, ship, aliens) 
        ship.center_ship()
        sleep(0.5)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

