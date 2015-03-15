import sys
import pygame
from pygame.locals import *
pygame.mixer.pre_init(frequency=22050, size=-16, channels=8, buffer=256)

# Init
pygame.init()
clock = pygame.time.Clock()
screenX, screenY = 516, 435
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Mariolike")
vertFond = (166, 177, 65)
noirFond = (0, 4, 0)
blancFond = (255, 255, 255)
taille_sprite = 29
block_list, monstres_list, item_list = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
active_sprite_list = pygame.sprite.Group()
volume_default, volume = 0.3, 3


# Coordonnées
menu_Curseur_Coord = [(195, 160), (195, 195), (195, 230)]
levelSelection_Curseur_Coord = [(80, 100), (270, 100), (80, 300), (270, 300)]
levelSelection_Stages_Coord = [(110, 100), (300, 100), (110, 300), (300, 300)]
menuCurseurPos, levelCurseurPos = 0, 0


# Images
bg_list = [(pygame.image.load("images/bg.png")), (pygame.image.load("images/bg2.png")),
           (pygame.image.load("images/bg3.png")), (pygame.image.load("images/bg4.png"))]
levelselection_list = [(pygame.image.load("images/levelselection_stage_1_1.png")), (pygame.image.load("images/levelselection_stage_1_2.png")),
                       (pygame.image.load("images/levelselection_stage_1_3.png")), (pygame.image.load("images/levelselection_stage_1_4.png"))]
volume_redsquare = pygame.image.load("images/vol_redsquare.png")
volume_bar = pygame.image.load("images/vol_bar.jpg")
levelselection_bg = pygame.image.load("images/levelselection_bg.png")
menuImage = pygame.image.load("images/menu.png")
menuCurseurImage = pygame.image.load("images/curseur.png")
options = pygame.image.load("images/options.png")
icon = pygame.image.load("images/icon.png")


# Musiques/sons
levels_music = [(pygame.mixer.Sound('sons/level1_music.wav')), (pygame.mixer.Sound('sons/level2_music.wav')),
                (pygame.mixer.Sound('sons/level3_music.wav')), (pygame.mixer.Sound('sons/level4_music.wav'))]
menu_music = pygame.mixer.Sound('sons/menu_music.wav')
jump_sound = pygame.mixer.Sound('sons/jump.wav')
death_sound = pygame.mixer.Sound('sons/death.wav')
bloc_break_sound = pygame.mixer.Sound('sons/bloc_break.wav')
bloc_item_sound = pygame.mixer.Sound('sons/bloc_item.wav')
goomba_stomp_sound = pygame.mixer.Sound('sons/goomba_stomp.wav')
upgrade_sound = pygame.mixer.Sound('sons/item_pick_sound.wav')


# Variables
continuer, menu, optionsOn, levelSelection, jeu, levelCurrent, generation_level = 1, 1, 0, 0, 0, -1, 1
reset, willRespawn, on_level = 0, 0, 0


#Init n°2
pygame.display.set_icon(icon)
menu_music.set_volume(volume_default)
menu_music.play()