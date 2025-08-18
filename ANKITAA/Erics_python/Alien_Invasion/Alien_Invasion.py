import sys
import traceback
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf


def game_over(ai_settings, screen, stats, sb):
    """Display Game Over message and stop the game."""
    font = pygame.font.SysFont(None, 74)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(ai_settings.screen_width // 2, ai_settings.screen_height // 2))
    
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    
    # Pause for 2 seconds before quitting
    pygame.time.delay(2000)
    stats.game_active = False
    stats.reset_stats()
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()


def run_game():
    try:
        # Initialize Pygame and game settings
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Create the Play button
        play_button = Button(ai_settings, screen, "Play")

        # Create instances for stats, scoreboard, ship, bullets, aliens
        stats = GameStats(ai_settings)
        sb = Scoreboard(ai_settings, screen, stats)
        ship = Ship(ai_settings, screen)
        bullets = pygame.sprite.Group()
        aliens = pygame.sprite.Group()

        # Create the fleet of aliens
        gf.create_fleet(ai_settings, screen, ship, aliens)

        # Clock to control FPS
        clock = pygame.time.Clock()

        # Main game loop
        while True:
            gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)

            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

                # Check if player has no ships left -> Game Over
                if stats.ships_left <= 0:
                    game_over(ai_settings, screen, stats, sb)

            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

            clock.tick(60)  # Limit to 60 frames per second

    except Exception as e:
        print("An unexpected error occurred:")
        traceback.print_exc()
        pygame.quit()
        sys.exit()


# Run the game
if __name__ == "__main__":
    run_game()
