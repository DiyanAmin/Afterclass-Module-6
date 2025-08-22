# Parameters:
# Window Size [640,480]
# Caption [My First Game Screen]
# Rectangle [Red] | At Centre of [Screen]
# Display Text [Hi hello | bye bye]
# Background colour of screen [White (255,255,255)]

# Initializing
import pygame
pygame.init()

# Colors and rectangle setup
rouge = pygame.Color('red')
rect_width, rect_height = 60, 60
WindowSize = (640, 480)

# Set up the display
Screen = pygame.display.set_mode(WindowSize)
pygame.display.set_caption("My First Game screen")

# Calculate center position for rectangle
rect_x = (WindowSize[0] - rect_width) // 2
rect_y = (WindowSize[1] - rect_height) // 2
rectPeri = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Font and text rendering
font = pygame.font.Font(None, 36)
text = font.render('Hi hello | bye bye', True, rouge)
text_rect = text.get_rect(center=(WindowSize[0] // 2, WindowSize[1] // 2 + 80))  # Slightly below rectangle

# Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(Screen, rouge, rectPeri)  # Red rectangle at center
    Screen.blit(text, text_rect)  # Display text
    pygame.display.flip()

pygame.quit()