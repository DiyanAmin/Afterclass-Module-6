import pygame
phast=int(input('Choose your speed: '))
# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprites ')

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprites
player = pygame.Rect(100, 100, 50, 50)  
enemy = pygame.Rect(300, 300, 50, 50)   
speed = phast # --> To increase movement speed use this!

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed

    # Draw sprites
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    pygame.display.update()
    clock.tick(60)

pygame.quit()