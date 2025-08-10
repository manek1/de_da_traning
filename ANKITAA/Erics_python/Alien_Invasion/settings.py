class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game’s static and dynamic settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)  # Light gray background

        # Ship settings
        self.ship_limit = 3  # Number of lives

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5  # Limit on-screen bullets

        # Alien settings
        self.fleet_drop_speed = 10  # Distance to drop when edge is hit

        # Speed scaling
        self.speedup_scale = 1.1  # How quickly the game speeds up
        self.score_scale = 1.5    # How quickly the alien point value increases

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 3.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 3.5

        # fleet_direction: 1 means right, -1 means left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
