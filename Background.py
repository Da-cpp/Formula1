import pygame
Racetrack = 'racetrack.jpg'
from pygame.locals import *
from sys import exit

pygame.init()



#Can  be adjusted appropriately...
test_screen = pygame.display.set_mode((1002,797))
pygame.display.set_caption("Test")


Bg = pygame.image.load(Racetrack)

while True:
    test_screen.fill((0,0,0))

    test_screen.blit(Bg,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()