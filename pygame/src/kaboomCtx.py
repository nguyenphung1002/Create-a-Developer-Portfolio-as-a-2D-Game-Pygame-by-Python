import pygame

# Constants
SCALE_FACTOR = 4 

# Initialize Pygame
pygame.init()

# Setup the display
screen = pygame.display.set_mode((800, 600)) 

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here

    # Clear the screen
    screen.fill((0, 0, 0))  # Clear the screen with black

    # Update the display
    pygame.display.flip()

pygame.quit()
