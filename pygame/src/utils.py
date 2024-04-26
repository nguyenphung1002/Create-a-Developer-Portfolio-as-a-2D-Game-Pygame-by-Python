import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

def display_dialogue(text, on_display_end):
    dialogue_box = pygame.Rect(100, 450, 600, 100)
    current_text = ""
    index = 0
    typing = True

    while typing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    typing = False

        if index < len(text):
            current_text += text[index]
            index += 1
        else:
            typing = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), dialogue_box)  # Draw the dialogue box
        rendered_text = font.render(current_text, True, (0, 0, 0))
        screen.blit(rendered_text, (110, 470))
        pygame.display.flip()
        clock.tick(30)  # Control the speed of text appearing

    on_display_end()

def on_display_end():
    print("Dialogue ended")

# Example usage
display_dialogue("Hello, welcome to the game!", on_display_end)
def set_cam_scale(screen):
    resize_factor = screen.get_width() / screen.get_height()
    if resize_factor < 1:
        cam_scale = 1  # More vertical screen
    else:
        cam_scale = 1.5  # More horizontal screen

    return cam_scale

# Usage
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
current_scale = set_cam_scale(screen)
print("Camera Scale Set To:", current_scale)
