import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# color set
WHITE = (255,255,255)

class Card:
    def __init__(self):
        self.create()
        
    def create(self):
        self.image = pygame.image.load('res/empty_card.png')
        self.position = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))]

    def _click(self):
        for event in pygame.event.get():# User did something
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                print("click")
            elif event.type == pygame.QUIT:
                pass

if __name__ == '__main__':
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Card Game")
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    while True:
        surface.fill(WHITE)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 40)
        window.blit(surface,(0, 0))
    