import pygame, sys
from pygame.sprite import Sprite, Group

# --- Settings ---
WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 40)
SHIP_SPEED = 5
BULLET_SPEED = 7
ALIEN_SPEED = 1
ALIEN_DROP = 10

# --- Initialize ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()

# --- Ship ---
class Ship(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/iTA/Downloads/ship.jpeg')
        self.image = pygame.transform.scale(self.image, (50, 38))
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT - 10))
        self.speed = SHIP_SPEED
        self.moving_left = self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_right and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def blitme(self):
        screen.blit(self.image, self.rect)

# --- Bullet ---
class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x - 2, y, 4, 12)
        self.color = (255, 255, 255)
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# --- Alien ---
class Alien(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('C:/Users/iTA/Downloads/—Pngtree—alien spaceships ufo with blue_6329025 (1).png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction=1):
        self.rect.x += ALIEN_SPEED * direction

    def blitme(self):
        screen.blit(self.image, self.rect)

# --- Game Setup ---
ship = Ship()
bullets = Group()
aliens = Group()

def create_fleet():
    alien = Alien(0,0)
    alien_width, alien_height = alien.rect.size
    cols = (WIDTH - 2 * alien_width) // (alien_width + 10)
    rows = 3
    for row in range(rows):
        for col in range(cols):
            x = alien_width + col * (alien_width + 10)
            y = alien_height + row * (alien_height + 10)
            aliens.add(Alien(x, y))

create_fleet()
fleet_direction = 1

# --- Main Loop ---
running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                ship.moving_left = True
            elif e.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif e.key == pygame.K_SPACE:
                bullets.add(Bullet(ship.rect.centerx, ship.rect.top))
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                ship.moving_left = False
            elif e.key == pygame.K_RIGHT:
                ship.moving_right = False

    # Update ship
    ship.update()

    # Update bullets
    bullets.update()

    # Update aliens
    edge_hit = False
    for alien in aliens.sprites():
        alien.update(fleet_direction)
        if alien.rect.right >= WIDTH or alien.rect.left <= 0:
            edge_hit = True
    if edge_hit:
        fleet_direction *= -1
        for alien in aliens.sprites():
            alien.rect.y += ALIEN_DROP

    # Collision detection
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Draw all elements
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw()
    for alien in aliens.sprites():
        alien.blitme()

    pygame.display.flip()

pygame.quit()
sys.exit()

