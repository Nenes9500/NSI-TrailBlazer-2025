import pygame
import sys

# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

# Check for connected joysticks
# Use the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Pygame window setup
clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle joystick events
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0 and (event.value >0.1 or event.value <-0.1):
                print(event.axis, event.value)

    # Show axis values
    # Display on screen
    clock.tick(60)  # Cap the frame rate

# Cleanup
pygame.quit()