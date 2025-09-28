import pygame
#Racetrack = 'race track.png'

from pygame.locals import *
from sys import exit


def load_background(scale_factor=0.255, filename="race track.png"):
    # Racetrack = 'race track.png'

    # Load the background image
    Racetrack = pygame.image.load(filename)

    pygame.init()

    bg_width, bg_height = Racetrack.get_size()

    new_width = int(bg_width * scale_factor)
    new_height = int(bg_height * scale_factor)

    Racetrack = pygame.transform.scale(Racetrack, (new_width, new_height))

    # Can be adjusted appropriately...
    # test_screen = pygame.display.set_mode((1002,797))
    test_screen = pygame.display.set_mode((new_width, new_height))
    pygame.display.set_caption("Formula One")

    # Bg = pygame.image.load(Racetrack)
    Bg = Racetrack

    return Bg, test_screen