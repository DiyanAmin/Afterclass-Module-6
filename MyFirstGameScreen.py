import pygame

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

# Define colors
grey= (58, 58, 58)

# Load and scale the image
image = pygame.image.load('leopard.jpeg')
image = pygame.transform.scale(image, (300, 300))

# Calculate center position
image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()