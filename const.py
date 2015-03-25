import sys
import pygame
from pygame.locals import *
pygame.mixer.pre_init(frequency=22050, size=-16, channels=8, buffer=256)

# Init
pygame.init()
clock = pygame.time.Clock()
screenX, screenY = 516, 435
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Mario Ninja")
vertFond = (166, 177, 65)
noirFond = (0, 4, 0)
blancFond = (255, 255, 255)
kakiFond = (0, 64, 64)
taille_sprite = 29
block_list, monstres_list, item_list, flag_list, coin_list, active_sprite_list, fireball_list = pygame.sprite.Group(),\
pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
shuriken_list, shuriken_list2 = pygame.sprite.Group(), pygame.sprite.Group()
marioGroup = pygame.sprite.GroupSingle()
volume_default, volume = 0.3, 3

# Coordonnées
menu_Curseur_Coord = [(193, 160), (193, 195), (193, 230), (193, 265)]
levelSelection_Curseur_Coord = [(90, 200), (280, 200), (90, 250), (280, 250)]
levelSelection_Stages_Coord = [(110, 200), (300, 200), (110, 250), (300, 250)]
menuCurseurPos, levelCurseurPos = 0, 0


# Images
bg_list = [(pygame.image.load("images/bg.png")), (pygame.image.load("images/bg2.png")),
           (pygame.image.load("images/bg3.png")), (pygame.image.load("images/bg4.png"))]
levelselection_list = [(pygame.image.load("images/levelselection_stage_1_1.png")), (pygame.image.load("images/levelselection_stage_1_2.png")),
                       (pygame.image.load("images/levelselection_stage_1_3.png")), (pygame.image.load("images/levelselection_stage_1_4.png"))]
images_menu_list = [(pygame.image.load("images/menu_menu.png")), (pygame.image.load("images/menu_options.png")),
                       (pygame.image.load("images/menu_controls.png")), (pygame.image.load("images/menu_levelSelect.png"))]
menu_fond = pygame.image.load("images/menu_fond.jpg")
volume_redsquare = pygame.image.load("images/vol_redsquare.png")
volume_bar = pygame.image.load("images/vol_bar.jpg")
menuCurseurImage = pygame.image.load("images/curseur.png")
icon = pygame.image.load("images/icon.png")
shuri_ghost_on = pygame.image.load('images/shuri_ghost_on.png')
item_off = pygame.image.load('images/item_off.png')


# Musiques/sons
menu_music = pygame.mixer.Sound('sons/menu_music.wav')
levels_music = [(pygame.mixer.Sound('sons/level1_music.wav')), (pygame.mixer.Sound('sons/level2_music.wav')),
                (pygame.mixer.Sound('sons/level3_music.wav')), (pygame.mixer.Sound('sons/level4_music.wav'))]
sound_list = [(pygame.mixer.Sound('sons/jump.wav')), (pygame.mixer.Sound('sons/death.wav')),
              (pygame.mixer.Sound('sons/bloc_break.wav')), (pygame.mixer.Sound('sons/bloc_item.wav')),
              (pygame.mixer.Sound('sons/goomba_stomp.wav')), (pygame.mixer.Sound('sons/item_pick_sound.wav')),
              (pygame.mixer.Sound('sons/liveUp_sound.wav')), (pygame.mixer.Sound('sons/coin_sound.wav')),
              (pygame.mixer.Sound('sons/deUpgrade_sound.wav')), (pygame.mixer.Sound('sons/fireball_sound.wav')),
              (pygame.mixer.Sound('sons/mario_sound.wav')), (pygame.mixer.Sound('sons/boomerang_sound.wav')),
              (pygame.mixer.Sound('sons/boomerang_return_sound.wav')), (pygame.mixer.Sound('sons/chainsaw_sound.wav')),
              (pygame.mixer.Sound('sons/wall_sound.wav')), (pygame.mixer.Sound('sons/tornado_sound.wav')),
              (pygame.mixer.Sound('sons/phoenix_sound.wav'))]


# Variables
continuer, menu, jeu, levelCurrent, generation_level = 1, 1, 0, -1, 1
controlsOn, optionsOn, levelSelectionOn = 0, 0, 0
font = pygame.font.SysFont("Arial", 10)


#Init n°2
pygame.display.set_icon(icon)
menu_music.set_volume(volume_default)
menu_music.play()