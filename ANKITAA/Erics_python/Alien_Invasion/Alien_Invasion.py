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

