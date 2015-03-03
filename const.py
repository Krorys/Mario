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
menu_curseur_position1 = (195,160)
menu_curseur_position2 = (195,195)
menu_curseur_position3 = (195,230)
levelselection_curseur_position1 = (80,100)
levelselection_curseur_position2 = (270,100)
levelselection_curseur_position3 = (80,300)
levelselection_curseur_position4 = (270,300)

#Images
icon = pygame.image.load("icon.png")
bg = pygame.image.load("bg.png")
levelselection_bg = pygame.image.load("levelselection_bg.png")
menuImage = pygame.image.load("menu.png")
menuCurseur = pygame.image.load("curseur.png")
options = pygame.image.load("options.png")
levelselection_stage_1_1 = pygame.image.load("levelselection_stage_1_1.png")
levelselection_stage_1_2 = pygame.image.load("levelselection_stage_1_2.png")
levelselection_stage_1_3 = pygame.image.load("levelselection_stage_1_3.png")
levelselection_stage_1_4 = pygame.image.load("levelselection_stage_1_4.png")

pygame.display.set_icon(icon)
screen.blit(menuImage, (0,0))
screen.blit(menuCurseur, menu_curseur_position1)