import sys
import time
import random
import pygame, sys
from pygame.locals import *

img_num = 0
LEFT = 1
RIGHT = 3
DragMode = False

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Card:
    img_name = None
    imagex = 0
    imagey = 0
    def __init__(self, img_name):
        self.img_name = pygame.image.load('res/'+img_name+'.png')
        self.imagex = 598
        self.imagey = 285

    def create(self, screen, pygame):
        screen.blit(self.img_name, (self.imagex, self.imagey))
        pygame.display.update()

if __name__ == "__main__":

    pygame.init()

    FPS = 10
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((1280, 720), 0, 32)
    pygame.display.set_caption('animation')

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 180)
    red = (255, 0, 0)

    card = Card("empty_card")
    BackGround = Background('res/background2.jpg', [0,0])
    direction = 'left'

    while True:
        screen.blit(BackGround.image, BackGround.rect)
        card.create(screen,pygame)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)
