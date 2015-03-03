import pygame, sys
from pygame.locals import *
from const import *

def level_selection_cons(): #Fonction qui re-dessine levelselection
    screen.blit(levelselection_bg, (0,0))
    screen.blit(levelselection_stage_1_1, (110,100))
    screen.blit(levelselection_stage_1_2, (300,100))
    screen.blit(levelselection_stage_1_3, (110,300))
    screen.blit(levelselection_stage_1_4, (300,300))
def level1_cons():
    screen.blit(bg, (0,0))

class Sprite():
    sprite_image = None
    def __init__(self, file_name):
        self.sprite_image = pygame.image.load(file_name)
    def get_image(self, x, y, largeur, hauteur):
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(orange)
        return image

class Mario(pygame.sprite.Sprite):
    def __init__(self, sprite):
        self.x = 0
        self.y = 0
        self.changeX = 0
        self.changeY = 0
        self.sprite = sprite
        self.hp = 3
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
        screen.blit(self.sprite)
    def move(self):
        self.x += self.changeX
        if self.rect.collidelist(sols): #Si le perso NE TOUCHE PAS aucun des murs
            self.y += self.changeY
    def jump(self):
        pass
    def death(self):
        pass
    def kill(self, monster):
        pass

class Monstres(Mario):
    pass

sols = []
class Block():
    def __init__(self):
        self.x = 100
        self.y = 200
        self.l = 200
        self.h = 10
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), self.rect)

class Sol(Block):
    def __init__(self):
        sols.append(self.rect)