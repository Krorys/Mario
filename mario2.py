__author__ = 'Chèvre'

import pygame, sys
from pygame.locals import *
from const import *
from classes_foncts import *
pygame.init()
menu_music = pygame.mixer.Sound('menu_music.wav')
menu_music.play()

#Variables
menu_curseur_actuel, levelselection_curseur_actuel = 1, 1
continuer, menu, optionsOn, levelselection, jeu_en_cours = 1, 1, 0, 0, 1
level_current = 0
#y = 0

marioSprite = SpriteImage("mario.png")
marioImage1 = marioSprite.get_image(0, 7, 18, 23) #Récupère l'image en position (0,7) de taille (18,23)
mariox2 = pygame.transform.scale2x(marioImage1) #Double la taille du Mario

mario = Mario(mariox2)
#perso = Perso()

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(bg, (0,0))
    bloc1.draw()
    mario.draw()
    mario.move()
    #perso.draw()
    pygame.display.flip()
    clock.tick(30)