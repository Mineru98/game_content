import sys
import time
import random
import pygame, sys
from pygame.locals import *
import sqlite3

img_num = 0
DragMode = True

BLACK = (0,0,0)

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

    def create(self, screen, pygame):
        screen.blit(self.img_name, (self.imagex, self.imagey))
        pygame.display.update()

def exit_handler(con):
    con.close()

def create_user(id, pw, con, cursor):
    try:
        cursor.execute("INSERT INTO User VALUES('%s', '%s', 0)" % (id, pw))
        con.commit()
        return True
    except:
        return False


def login_user(id, pw, con, cursor):
    cursor.execute("select email,password from User where email='%s' and password='%s'" % (id, pw))
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == id:
            if row[1] == pw:
                return True
            else:
                return False
        else:
            return False

def game_login(con, cursor):
    print("Login")
    _id = input("ID: ")
    _pw = input("PW: ")

    if login_user(_id, _pw, con, cursor) == True:
        return
    else:
        print("SignUp")
        _id = input("ID: ")
        _pw = input("PW: ")
        if create_user(_id, _pw, con, cursor) == True:
            print("SignUp Success!!!")
        else:
            print("SignUp Fail...")


def game_start(con):
    global DragMode
    pygame.init()
    FPS = 500
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    pygame.display.set_caption('Card Game')

    card_e = pygame.image.load('res/empty_card.png')
    card_1 = pygame.image.load('res/card_1.png')
    card_2 = pygame.image.load('res/card_2.png')
    image = card_1
    imagex = 598
    imagey = 285
    BackGround = Background('res/background2.jpg', [0,0])
    direction = 'left'

    cursor = pygame.image.load('res/default_cursor.png')
    c_cursor = pygame.image.load('res/click_cursor.png')
    pygame.mouse.set_visible(False)
    coord = pygame.mouse.get_pos()
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pres = pygame.mouse.get_pressed()
        
        if (0 <= mouse_pos[0] and mouse_pos[0] <= 100) and (0 <= mouse_pos[1] and mouse_pos[1] <= 100):
            coord = pygame.mouse.get_pos()
            screen.blit(c_cursor, (coord[0]-25,coord[1]-15))
            pygame.display.update()
        else:
            coord = pygame.mouse.get_pos()
            screen.blit(cursor, (coord[0]-25,coord[1]-15))
            pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN) and mouse_pres[0] == 1:
                if (0 <= mouse_pos[0] and mouse_pos[0] <= 100) and (0 <= mouse_pos[1] and mouse_pos[1] <= 100):
                    exit_handler(con)
                    pygame.quit()
                    sys.exit()
                if (mouse_pos[0] - 52 <= imagex and imagex <= mouse_pos[0] + 52) and (mouse_pos[1] - 75 <= imagey and imagey <= mouse_pos[1] + 75):
                    if DragMode == True:
                        DragMode = False
                    else:
                        DragMode = True
        if DragMode == True:
            imagex = mouse_pos[0] - 52
            imagey = mouse_pos[1] - 75
            pygame.display.update()

        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(image, (imagex, imagey))
        # 마우스 이미지 교체
       

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)

def main():
    con = sqlite3.connect("DB/cardgame.db")
    sqlite3.Connection
    cursor = con.cursor()
    try:
        try:
            cursor.execute("select * from game_setting")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE game_setting(isFirst INTEGER DEFAULT 1)")
            cursor.execute("CREATE TABLE User(email text, password text, attendance int)")
            print("Create Default Table")
        while True:
            game_login(con, cursor)
            game_start(con)
    finally:
        exit_handler(con)

if __name__ == "__main__":
    main()