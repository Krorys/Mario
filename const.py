import sys

import pygame
from pygame.locals import *

pygame.mixer.pre_init(frequency=22050, size=-16, channels=8, buffer=256)
pygame.init()

# Init
clock = pygame.time.Clock()
screenX, screenY = 516, 435
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Mariolike")
orange = (255, 128, 64)
vertFond = (166, 177, 65)
noirFond = (0, 4, 0)
blancFond = (255, 255, 255)
choix = "n1.txt"
taille_sprite = 29
on_level = 0
block_list = pygame.sprite.Group()
monstres_list = pygame.sprite.Group()
volume_default = 0.3
volume = 3
willDie = 0 #Sensé se mettre à 1 seulement si collision horizontale avec goomba le fdp OU sensé s'annuler lors d'une collision verticale (faudra choisir l'un ou l'autre).
respawn = 0

#Coordonnées
menuCurseurList = [(195, 160), (195, 195), (195, 230)]
levelCurseurList = [(80, 100), (270, 100), (80, 300), (270, 300)]
menuCurseurPos, levelCurseurPos = 0, 0

#Images
icon = pygame.image.load("images/icon.png")
bg_list = [(pygame.image.load("images/bg.png")), (pygame.image.load("images/bg2.png")),
           (pygame.image.load("images/bg3.png")), (pygame.image.load("images/bg4.png"))]
volume_redsquare = pygame.image.load("images/vol red square.png")
volume_bar = pygame.image.load("images/vol0.jpg")
levelselection_bg = pygame.image.load("images/levelselection_bg.png")
menuImage = pygame.image.load("images/menu.png")
menuCurseurImage = pygame.image.load("images/curseur.png")
options = pygame.image.load("images/options.png")
levelselection_stage_1_1 = pygame.image.load("images/levelselection_stage_1_1.png")
levelselection_stage_1_2 = pygame.image.load("images/levelselection_stage_1_2.png")
levelselection_stage_1_3 = pygame.image.load("images/levelselection_stage_1_3.png")
levelselection_stage_1_4 = pygame.image.load("images/levelselection_stage_1_4.png")
bloc = pygame.image.load("images/bloc.jpg")
mushroom = pygame.image.load("images/mushroom.jpg")
flag = pygame.image.load("images/flag.jpg")

#Musiques/sons
menu_music = pygame.mixer.Sound('sons/menu_music.wav')
levels_music = [(pygame.mixer.Sound('sons/level1_music.wav')), (pygame.mixer.Sound('sons/level2_music.wav')),
                (pygame.mixer.Sound('sons/level3_music.wav')), (pygame.mixer.Sound('sons/level4_music.wav'))]
jump_sound = pygame.mixer.Sound('sons/jump.wav')
death_sound = pygame.mixer.Sound('sons/death.wav')
bloc_break_sound = pygame.mixer.Sound('sons/bloc_break.wav')
goomba_stomp = pygame.mixer.Sound('sons/goomba_stomp.wav')

#Variables
continuer, menu, optionsOn, levelSelection, jeu, levelCurrent, generation_level = 1, 1, 0, 0, 0, -1, 1
reset = 0

#Init n°2
pygame.display.set_icon(icon)
screen.blit(menuImage, (0, 0))
screen.blit(menuCurseurImage, menuCurseurList[0])
menu_music.set_volume(volume_default)
menu_music.play()