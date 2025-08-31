import pygame
import random


CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger every 2 seconds

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.image.fill(self.color)

# Setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Create sprites
sprite1 = ColorSprite(100, 100, (255, 0, 0))
sprite2 = ColorSprite(200, 100, (0, 255, 0))
all_sprites = pygame.sprite.Group(sprite1,sprite2) # DOUBT : Unable to add sprites to group

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()