import pygame, sys
from pygame.locals import *

#Init
clock = pygame.time.Clock()
screen = pygame.display.set_mode((516, 435))
pygame.display.set_caption("Mariolike")
orange = (255, 128, 64)
choix = "n1.txt"
taille_sprite = 29

#Coordonnées
menuCurseurList = [(195,160), (195,195), (195,230)]
levelCurseurList = [(80,100), (270,100), (80,300), (270,300)]
menuCurseurPos, levelCurseurPos = 0, 0

#Images
icon = pygame.image.load("icon.png")
bg = pygame.image.load("bg.png")
levelselection_bg = pygame.image.load("levelselection_bg.png")
menuImage = pygame.image.load("menu.png")
menuCurseurImage = pygame.image.load("curseur.png")
options = pygame.image.load("options.png")
levelselection_stage_1_1 = pygame.image.load("levelselection_stage_1_1.png")
levelselection_stage_1_2 = pygame.image.load("levelselection_stage_1_2.png")
levelselection_stage_1_3 = pygame.image.load("levelselection_stage_1_3.png")
levelselection_stage_1_4 = pygame.image.load("levelselection_stage_1_4.png")

#Variables
continuer, menu, optionsOn, levelSelection, jeu, levelCurrent = 1, 1, 0, 0, 0, -1

pygame.display.set_icon(icon)