__author__ = 'Alexandre'

__author__ = 'Alexandre'

import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((516, 435))
pygame.display.set_caption("Test: Plateformes avec rectangles")
bg = pygame.image.load("bg.png")
orange = (255, 128, 64)
ciel, vert, bleu, orange2, rouge, jaune, violet, black, white, grey = (0,100,150), (30,180,7), (0,100,200), (200,130,10), (200,0,30), (250,250,80), (180,60,230), (0,0,0), (255,255,255), (170, 170, 170)

class SpriteImage():
    sprite_image = None

    def __init__(self, file_name):
        self.sprite_image = pygame.image.load(file_name)

    def get_image(self, x, y, largeur, hauteur):
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(orange)
        return image

marioSprite = SpriteImage("mario.png")
marioImage1 = marioSprite.get_image(0, 7, 18, 23) #Récupère l'image en position (0,7) de taille (18,23)
mariox2 = pygame.transform.scale2x(marioImage1) #Double la taille du Mario

class Mario(pygame.sprite.Sprite):
    def __init__(self, sprite):
        self.x = 100
        self.y = 100
        self.changeX = 0
        self.changeY = 3
        #self.sprite = pygame.image.load(sprite).convert()
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.hp = 3
        super().__init__()

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
        screen.blit(self.sprite, (self.x, self.y))

    def move(self):
        self.x += self.changeX
        if self.rect.collidelist(sols):
            self.y += self.changeY

sols = []
class Block(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.x = 0
        self.y = 0
        self.changeX = 0
        self.changeY = 0
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
        sols.append(self.rect)
    def draw(self):
        self.update()
        screen.blit(self.sprite, (self.x, self.y))


class Sol(Block):
    def __init__(self, sprite):
        Block.__init__(self, sprite)
        #sol_list.add(self)

perso = Mario(mariox2)
sol = Sol("bloc.jpg")
sol.x = 100
sol.y = 400

continuer, menu = 1, 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            pass

    screen.blit(bg, (0, 0))
    sol.draw()
    perso.draw()
    perso.move()

    clock.tick(60)
    pygame.display.flip()