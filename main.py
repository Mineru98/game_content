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
    def __init__(self, img_name, screen):
        self.img_name = pygame.image.load('res/'+img_name+'.png')
        self.imagex = 598
        self.imagey = 285
        screen.blit(self.img_name, (self.imagex, self.imagey))
        pygame.display.update()

if __name__ == "__main__":

    pygame.init()

    FPS = 10 #frames per second setting
    fpsClock = pygame.time.Clock()

    #set up the window
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    pygame.display.set_caption('animation')

    #set up the colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 180)
    red = (255, 0, 0)

    card_e = pygame.image.load('res/empty_card.png')
    card_1 = pygame.image.load('res/card_1.png')
    card_2 = pygame.image.load('res/card_2.png')
    image = card_1
    imagex = 598
    imagey = 285
    BackGround = Background('res/background2.jpg', [0,0])
    direction = 'left'

    while True: # the main game loop.
        mouse_pos = pygame.mouse.get_pos()
        mouse_pres = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN) and mouse_pres[0] == 1:
                if (mouse_pos[0] - 52 <= imagex and imagex <= mouse_pos[0] + 52) and (mouse_pos[1] - 75 <= imagey and imagey <= mouse_pos[1] + 75):
                    print(mouse_pos[0] - 52)
                    print(imagex)
                    print(mouse_pos[0] + 52)
                    if DragMode == True:
                        DragMode = False
                    else:
                        DragMode = True

        if DragMode == True:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN) and mouse_pres[0] == 1:
                    if (598 <= mouse_pos[0] and mouse_pos[0] <= 703) and (285 <= mouse_pos[1] and mouse_pos[1] <= 420):
                        print("Left Click")
                        if img_num == 0:
                            image = card_e
                            img_num = 1
                        elif img_num == 1:
                            image = card_1
                            img_num = 2
                        elif img_num == 2:
                            image = card_2
                            img_num = 0
                elif (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN) and mouse_pres[2] == 1 :
                    print("Right Click")
                pygame.display.update()
        elif DragMode == False:
            imagex = mouse_pos[0] - 52
            imagey = mouse_pos[1] - 75
            pygame.display.update()

        # if (598 <= mouse_pos[0] and mouse_pos[0] <= 703) and (285 <= mouse_pos[1] and mouse_pos[1] <= 435):
        #     print("OK")
        #     pygame.draw.line(screen, red, (598, 285), (703, 285), 2)
        #     pygame.draw.line(screen, red, (598, 435), (598, 285), 2)
        #     pygame.draw.line(screen, red, (598, 435), (703, 435), 2)
        #     pygame.draw.line(screen, red, (703, 435), (703, 285), 2)
        #     pygame.display.update()

        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(image, (imagex, imagey))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)
