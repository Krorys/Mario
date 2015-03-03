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
y = 0

marioSprite = Sprite("mario.png")
mario = marioSprite.get_image(0, 7, 18, 23)
mariox2 = pygame.transform.scale2x(mario)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if menu == 1:
                if menu_curseur_actuel == 1:
                    if event.key == K_DOWN:
                        screen.blit(menuImage, (0,0))
                        screen.blit(menuCurseur, menu_curseur_position2)
                        menu_curseur_actuel +=1
                        break
                if menu_curseur_actuel == 2:
                    if event.key == K_DOWN:
                        screen.blit(menuImage, (0,0))
                        screen.blit(menuCurseur, menu_curseur_position3)
                        menu_curseur_actuel +=1
                    if event.key == K_UP:
                        screen.blit(menuImage, (0,0))
                        screen.blit(menuCurseur, menu_curseur_position1)
                        menu_curseur_actuel -=1
                if menu_curseur_actuel == 3:
                    if event.key == K_UP:
                        screen.blit(menuImage, (0,0))
                        screen.blit(menuCurseur, menu_curseur_position2)
                        menu_curseur_actuel -=1

                if (event.key == K_RETURN) and (menu_curseur_actuel==1) : #Transition vers levelselection
                    levelselection, menu = 1, 0
                    level_selection_cons()
                    screen.blit(menuCurseur, levelselection_curseur_position1)

                if (event.key == K_RETURN) and (menu_curseur_actuel==2) : #Transition vers options
                    screen.blit(options, (0,0))
                    optionsOn, menu = 1, 0
                    break

                if (event.key == K_RETURN) and (menu_curseur_actuel==3) : #Fin du jeu
                    continuer = 0
                break
            if optionsOn == 1:
                if event.key == K_RETURN:
                    menu, optionsOn = 1, 0
                    screen.blit(menuImage, (0,0))
                    screen.blit(menuCurseur, menu_curseur_position2)

            if levelselection == 1:

                if levelselection_curseur_actuel == 1:
                    if event.key == K_RIGHT:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position2)
                        levelselection_curseur_actuel = 2
                        break
                    if event.key == K_DOWN:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position3)
                        levelselection_curseur_actuel = 3
                        break
                if levelselection_curseur_actuel == 2:
                    if event.key == K_LEFT:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position1)
                        levelselection_curseur_actuel = 1
                        break
                    if event.key == K_DOWN:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position4)
                        levelselection_curseur_actuel = 4
                        break
                if levelselection_curseur_actuel == 3:
                    if event.key == K_RIGHT:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position4)
                        levelselection_curseur_actuel = 4
                        break
                    if event.key == K_UP:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position1)
                        levelselection_curseur_actuel = 1
                        break
                if levelselection_curseur_actuel == 4:
                    if event.key == K_LEFT:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position3)
                        levelselection_curseur_actuel = 3
                        break
                    if event.key == K_UP:
                        level_selection_cons()
                        screen.blit(menuCurseur, levelselection_curseur_position2)
                        levelselection_curseur_actuel = 2
                        break
                if event.key == K_RETURN: #Début du niveau
                    level_current = levelselection_curseur_actuel
                    jeu_en_cours, levelselection = 1, 0
            if (event.key == K_ESCAPE) and (levelselection == 1): #Retour au menu avec échap
                screen.blit(menuImage, (0,0))
                screen.blit(menuCurseur, menu_curseur_position1)
                levelselection, menu = 0, 1
                levelselection_curseur_actuel = 1
    #Niveaux
    if level_current == 1 :
        level1_cons()
        screen.blit(mariox2, (0, 0))
    if level_current == 2 :
        print("niveau2")
    if level_current == 3 :
        print("niveau3")
    if level_current == 4 :
        print("niveau4")

    pygame.display.flip()
    clock.tick(30)