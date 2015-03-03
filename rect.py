__author__ = 'Alexandre'

__author__ = 'Alexandre'

import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((516, 435))
pygame.display.set_caption("Test: Plateformes avec rectangles")
bg = pygame.image.load("bg.png")
ciel, vert, bleu, orange, rouge, jaune, violet, black, white, grey = (0,100,150), (30,180,7), (0,100,200), (200,130,10), (200,0,30), (250,250,80), (180,60,230), (0,0,0), (255,255,255), (170, 170, 170)

class Perso():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.l = 20
        self.h = 50
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        self.changeX = 0
        self.changeY = 3
        self.hp = 3
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        pygame.draw.rect(screen, rouge, self.rect)
    def move(self):
        self.x += self.changeX
        if self.rect.collidelist(sols): #Si le perso NE TOUCHE PAS aucun des murs
            self.y += self.changeY
    def jump(self):
        pass
    def kill(self, monster):
        pass

sols = []
class Plateforme():
    def __init__(self):
        self.x = 100
        self.y = 200
        self.l = 200
        self.h = 10
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        sols.append(self.rect)
    def draw(self):
        pygame.draw.rect(screen, black, self.rect)

perso = Perso()
sol = Plateforme()

ty = 100
test1 = pygame.Rect(100, ty, 10, 40)
test2 = pygame.Rect(100, 300, 200, 10)

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