import pygame
import json

pygame.init()

# Load constants and setup screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load sprites
spritesheet = pygame.image.load('./spritesheet.png')
map_image = pygame.image.load('./map.png')

# Define animations from spritesheet
def get_animation(start_frame, frames, width=32, height=32):
    animation_frames = []
    for i in range(frames):
        frame = spritesheet.subsurface((start_frame % 39 * width, start_frame // 39 * height, width, height))
        animation_frames.append(frame)
        start_frame += 1
    return animation_frames

player_animations = {
    'idle-down': get_animation(936, 1),
    'walk-down': get_animation(936, 4),
    'idle-side': get_animation(975, 1),
    'walk-side': get_animation(975, 4),
    'idle-up': get_animation(1014, 1),
    'walk-up': get_animation(1014, 4)
}

# Player setup
player_rect = pygame.Rect(100, 100, 32, 32)  # Initial position
player_speed = 250
player_direction = 'down'
current_animation = player_animations['idle-down']
animation_index = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement logic here similar to key handling in your JS code
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed * clock.get_time() / 1000
        current_animation = player_animations['walk-side']
        player_direction = 'left'
    elif keys[pygame.K_RIGHT]:
        player_rect.x += player_speed * clock.get_time() / 1000
        current_animation = player_animations['walk-side']
        player_direction = 'right'
    elif keys[pygame.K_UP]:
        player_rect.y -= player_speed * clock.get_time() / 1000
        current_animation = player_animations['walk-up']
        player_direction = 'up'
    elif keys[pygame.K_DOWN]:
        player_rect.y += player_speed * clock.get_time() / 1000
        current_animation = player_animations['walk-down']
        player_direction = 'down'

    # Update frame
    animation_index += 1
    if animation_index >= len(current_animation):
        animation_index = 0

    # Render logic
    screen.fill((49, 16, 71))  
    screen.blit(map_image, (0, 0))
    screen.blit(current_animation[animation_index], player_rect)

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
