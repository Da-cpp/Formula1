import pygame
from sys import exit
pygame.init()

import pygame
from pygame.locals import *
from sys import exit
from Background import load_background
from F1CarMovement import F1Car

pygame.init()

# Load background and screen
Bg, screen = load_background(scale_factor=0.255)

# Create the car
#car = F1Car(position=(screen.get_width()//2, screen.get_height()//2))
car = F1Car(position=(100, 400), screen=screen)

clock = pygame.time.Clock()

# Main game loop
while True:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    car.update(keys, dt)

    screen.fill((0,0,0))
    screen.blit(Bg, (0, 0))  # Draw the background
    car.draw(screen)

    pygame.display.update()