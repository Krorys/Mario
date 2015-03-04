__author__ = 'Chèvre'

import pygame, sys
from pygame.locals import *
from const import *
from classes_foncts import *
pygame.init()

#Musique
menu_music = pygame.mixer.Sound('menu_music.wav')
menu_music.play()

#Variables
marioSprite = SpriteImage("mario.png")
marioImage1 = marioSprite.get_image(0, 7, 18, 23) #Récupère l'image en position (0,7) de taille (18,23)
mariox2 = pygame.transform.scale2x(marioImage1) #Double la taille du Mario

mario = Mario(mariox2)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if menu == 1: #MENU
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

                if (event.key == K_RETURN) and (menu_curseur_actuel==1) : #ALLER SELECTION NIVEAUX
                    levelselection, menu = 1, 0
                    level_selection_cons()
                    screen.blit(menuCurseur, levelselection_curseur_position1)

                if (event.key == K_RETURN) and (menu_curseur_actuel==2) : #ALLER OPTIONS
                    screen.blit(options, (0,0))
                    optionsOn, menu = 1, 0
                    break

                if (event.key == K_RETURN) and (menu_curseur_actuel==3) : #QUITTER
                    continuer = 0
                break
            if optionsOn == 1:
                if event.key == K_RETURN: #OPTIONS
                    menu, optionsOn = 1, 0
                    screen.blit(menuImage, (0,0))
                    screen.blit(menuCurseur, menu_curseur_position2)

            if levelselection == 1: #SELECTION NIVEAUX

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

                if event.key == K_RETURN: #ALLER JEU
                    level_current = levelselection_curseur_actuel
                    jeu_en_cours, levelselection = 1, 0

                if event.key == K_ESCAPE: #RETOUR MENU
                    screen.blit(menuImage, (0,0))
                    screen.blit(menuCurseur, menu_curseur_position1)
                    levelselection, menu = 0, 1
                    levelselection_curseur_actuel = 1

            if jeu_en_cours == 1: #JEU

                if event.key == K_RIGHT: #DROITE
                    mario.changeX = 5
                    if mario.lookat == "left":
                        mario.sprite = pygame.transform.flip(mario.sprite, True, False)
                        mario.lookat = "right"
                if event.key == K_LEFT: #GAUCHE
                    mario.changeX = -5
                    if mario.lookat == "right":
                        mario.sprite = pygame.transform.flip(mario.sprite, True, False)
                        mario.lookat = "left"
                    # Là faut trouver un moyen de nettoyer block_list à chaque fois qu'on retourne sur la sélection des niveaux (avec echap), sinon les niveaux "s'entassent" dans block_list
                """
                if event.key == K_ESCAPE: #RETOUR SELECTION NIVEAUX
                    level_selection_cons() #on reconstruis l'écran de sélection
                    levelselection_curseur_actuel = 1 #on replace la position du curseur sur le stage 1-1
                    screen.blit(menuCurseur, levelselection_curseur_position1) #on dessine l'image du curseur à la position actuelle du curseur (donc la 1)
                    levelselection, level_current, jeu_en_cours = 1, 0, 0 #on lance la boucle de sélection des niveaux et on ferme les deux boucles de jeu
                    mario.x, mario.y = 100, 100 #on replace mario pour qu'il ne respawn pas à l'endroit où on l'a laissé la dernière fois
                """
        if event.type == KEYUP: #ANTI-REFLET
            if jeu_en_cours == 1:
                if event.key == K_RIGHT:
                    mario.changeX = 0
                if event.key == K_LEFT:
                    mario.changeX = -0

    if level_current == 1 : #NIVEAU 1
        choix = 'n1.txt'
        level1_cons()
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(screen)
        block_list.draw(screen)
        #bloc2.draw()
        mario.draw()
        mario.move()

    if level_current == 2 : #NIVEAU 2
        choix = 'n2.txt'
        level1_cons()
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(screen)
        block_list.draw(screen)
        #bloc2.draw()
        mario.draw()
        mario.move()

    if level_current == 3 : #NIVEAU 3
        choix = 'n3.txt'
        level1_cons()
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(screen)
        block_list.draw(screen)
        #bloc2.draw()
        mario.draw()
        mario.move()

    if level_current == 4 : #NIVEAU 4
        choix = 'n4.txt'
        level1_cons()
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(screen)
        block_list.draw(screen)
        #bloc2.draw()
        mario.draw()
        mario.move()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()