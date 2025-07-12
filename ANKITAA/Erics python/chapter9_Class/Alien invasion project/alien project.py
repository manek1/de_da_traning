import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame project")
clock = pygame.time.Clock()

BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game states
MENU = "menu"
BLUE_SKY = "blue_sky"
CHARACTER = "character"
ROCKET = "rocket"
KEYS = "keys"
SHOOTER = "shooter"
state = MENU

# Character class
class GameCharacter:
    def __init__(self):
        self.image = pygame.image.load("C:/Users/iTA/Knight Character.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        screen.blit(self.image, self.rect)

# Rocket class
class Rocket:
    def __init__(self):
        self.image = pygame.image.load("C:/Users/iTA/rockett.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Shooter classes
class Ship:
    def __init__(self):
        self.image = pygame.image.load("C:/Users/iTA/shipp.bmp")
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.centery = 300
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.rect = pygame.Rect(ship.rect.right, ship.rect.centery - 2, 15, 5)
        self.color = (255, 0, 0)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Initialize
character = GameCharacter()
rocket = Rocket()
ship = Ship()
bullets = pygame.sprite.Group()

# Game loop
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if state == MENU and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                state = BLUE_SKY
            elif event.key == pygame.K_2:
                state = CHARACTER
            elif event.key == pygame.K_3:
                state = ROCKET
            elif event.key == pygame.K_4:
                state = KEYS
            elif event.key == pygame.K_5:
                state = SHOOTER
        elif state == SHOOTER and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.add(Bullet(ship))
        elif state == KEYS and event.type == pygame.KEYDOWN:
            print("Key Pressed:", event.key)

    # Drawing
    if state == MENU:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 40)
        menu_items = [
            "1. Blue Sky",
            "2. Game Character",
            "3. Rocket Movement",
            "4. Key Press Viewer",
            "5. Sideways Shooter",
            "ESC to Quit"
        ]
        for i, item in enumerate(menu_items):
            text = font.render(item, True, BLACK)
            screen.blit(text, (100, 100 + i * 50))

    elif state == BLUE_SKY:
        screen.fill(BLUE)

    elif state == CHARACTER:
        screen.fill(BLUE)
        character.draw()

    elif state == ROCKET:
        screen.fill(BLACK)
        rocket.update(keys)
        rocket.draw()
    elif state == KEYS:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 30)
        msg = font.render("Press any key and check terminal...",True, BLACK)
        screen.blit(msg, (200, 280))

    elif state == SHOOTER:
        screen.fill((30, 30, 30))
        ship.update(keys)
        ship.draw()
        for bullet in bullets.copy():
            bullet.update()
            bullet.draw()
            if bullet.rect.left > 800:
                bullets.remove(bullet)

    pygame.display.flip()
    clock.tick(60)
