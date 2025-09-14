# game_functions.py
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and stats.game_active:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Initialize new game state and start."""
    ai_settings.initialize_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    stats.game_over = False

    # reset scoreboard displays
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    pygame.mouse.set_visible(False)
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Draw everything on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # draw aliens
    for alien in aliens.sprites():
        alien.blitme()

    sb.show_score()

    if not stats.game_active:
        if stats.game_over:
            draw_game_over(screen)
        play_button.draw_button()

    pygame.display.flip()

def draw_game_over(screen):
    font = pygame.font.SysFont(None, 64)
    small = pygame.font.SysFont(None, 30)
    msg_image = font.render("GAME OVER", True, (255, 60, 60))
    msg_rect = msg_image.get_rect()
    msg_rect.center = (screen.get_rect().centerx, screen.get_rect().centery - 40)
    tip = small.render("Press P to Play again or Q to Quit", True, (230, 230, 230))
    tip_rect = tip.get_rect()
    tip_rect.center = (screen.get_rect().centerx, screen.get_rect().centery + 10)
    screen.blit(msg_image, msg_rect)
    screen.blit(tip, tip_rect)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # collisions between bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens_hit in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens_hit)
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # level cleared
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# --- Fleet creation helpers ---
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)
    return max(1, number_aliens_x)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height - 60
    number_rows = available_space_y // (2 * alien_height)
    return max(1, number_rows)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.x = float(alien.rect.x)
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    aliens.empty()
    sample_alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, sample_alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, sample_alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# --- Fleet movement & collisions ---
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        pygame.time.delay(500)
    else:
        stats.game_active = False
        stats.game_over = True
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens reached bottom of screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check for collision with ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # check if aliens reached bottom
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()