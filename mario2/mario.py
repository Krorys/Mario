__author__ = 'Chèvre'

import pygame, sys
from pygame.locals import *
from const import *
from classes_foncts import *

pygame.init()

menu_music = pygame.mixer.Sound('menu_music.wav')
menu_music.play()

marioSprite = SpriteImage("mario.png")
marioImage1 = marioSprite.get_image(0, 7, 18, 23) #Récupère l'image en position (0,7) de taille (18,23)
mariox2 = pygame.transform.scale2x(marioImage1) #Double la taille du Mario

mario = Mario(mariox2)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if menu:
            screen.blit(menuImage, (0,0))
            screen.blit(menuCurseurImage, menuCurseurList[menuCurseurPos])
            menuCurseurPos = choixMenu(event, menuCurseurPos)
            if event.type == KEYDOWN and event.key == K_RETURN:
                levelSelection, optionsOn, continuer = menuTo(menuCurseurPos)
                menu = 0
        elif optionsOn:
            screen.blit(options, (0,0))
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, optionsOn = 1, 0
        elif levelSelection:
            levelSelectionDraw()
            screen.blit(menuCurseurImage, levelCurseurList[levelCurseurPos])
            levelCurseurPos = choixLevel(event, levelCurseurPos)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, levelSelection = 1, 0
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, levelSelection, jeu, levelCurrent = 0, 0, 1, levelCurseurPos
        elif jeu:
            jeuFonct(event, mario)
    #Niveaux
    if levelCurrent == 0:
        choix = 'n1.txt'
        if generation_level == 1:
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(screen)
            generation_level = 0
        screen.blit(bg, (0, 0))
        block_list.draw(screen)
        mario.draw()
        mario.move()
    if levelCurrent == 1 :
        choix = 'n1.txt'
        if generation_level == 1:
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(screen)
            generation_level = 0
        screen.blit(bg, (0, 0))
        block_list.draw(screen)
        mario.draw()
        mario.move()
    if levelCurrent == 2 :
        choix = 'n1.txt'
        if generation_level == 1:
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(screen)
            generation_level = 0
        screen.blit(bg, (0, 0))
        block_list.draw(screen)
        mario.draw()
        mario.move()
    if levelCurrent == 3 :
        choix = 'n1.txt'
        if generation_level == 1:
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(screen)
            generation_level = 0
        screen.blit(bg, (0, 0))
        block_list.draw(screen)
        mario.draw()
        mario.move()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()