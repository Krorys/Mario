__author__ = 'Chèvre'

import sys

import pygame
from pygame.locals import *

from const import *
from classes_foncts import *


# Sprites
marioSprite = SpriteImage("images/mario sheet.png", vertFond, 1)
goombaSprite = SpriteImage("images/goomba sheet.png", blancFond, 1)
marioStand = marioSprite.get_imageXY(72, 5, 87, 31)
monstresStand = goombaSprite.get_imageXY(72, 5, 87, 31)
mario = Mario(marioStand)
monstres = Monstres(monstresStand)

gameOverSprite = SpriteImage("images/game over.png", noirFond, 0)
gameOver = gameOverSprite.get_imageXY(5, 7, 260, 230)

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(mario)
active_sprite_list.add(monstres)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if menu:
            screen.blit(menuImage, (0, 0))
            menuCurseurPos = choixMenu(event, menuCurseurPos)
            screen.blit(menuCurseurImage, menuCurseurList[menuCurseurPos])
            if event.type == KEYDOWN and event.key == K_RETURN:
                levelSelection, optionsOn, continuer = menuTo(menuCurseurPos)
                menu = 0
        elif optionsOn:
            screen.blit(options, (0, 0))
            affichage_volume(volume)
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, optionsOn = 1, 0
            if event.type == KEYDOWN and event.key == K_LEFT:  # baisser le son
                pygame.mixer.pause()
                if volume_default > 0.05 and volume_default < 1.05:
                    volume_default -= 0.1
                if volume > 0 and volume < 11:
                    volume -= 1
                affichage_volume(volume)
                menu_music.set_volume(volume_default)
                pygame.mixer.unpause()
                break
            if event.type == KEYDOWN and event.key == K_RIGHT:
                pygame.mixer.pause()
                if volume_default > -0.5 and volume_default < 0.95:
                    volume_default += 0.1
                if volume > -1 and volume < 10:
                    volume += 1
                affichage_volume(volume)
                menu_music.set_volume(volume_default)
                pygame.mixer.unpause()
                break

        elif levelSelection:
            levelSelectionDraw()
            levelCurseurPos = choixLevel(event, levelCurseurPos)
            screen.blit(menuCurseurImage, levelCurseurList[levelCurseurPos])
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, levelSelection = 1, 0
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, levelSelection, jeu, levelCurrent = 0, 0, 1, levelCurseurPos
        elif jeu:
            jeuFonct(event, mario)
    # Niveaux
    if jeu:
        choix = "n" + str(levelCurrent + 1) + ".txt"
        if generation_level:
            pygame.key.set_repeat(1, 1)
            volume_default = pygame.mixer.Sound.get_volume(menu_music)
            music_levels(levelCurrent, volume_default)
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(screen)
            generation_level = 0

        if (pygame.sprite.collide_rect(mario, monstres)) or (mario.rect.y >= screenY):
            screen.blit(bg_list[levelCurrent], (0, 0))
            block_list.draw(screen)
            active_sprite_list.draw(screen)
            mario.death()

        if mario.time == 210:
            screen.blit(bg_list[levelCurrent], (0, 0))
            block_list.update()
            block_list.draw(screen)
            monstresMovement(monstres)
            active_sprite_list.update()
            active_sprite_list.draw(screen)

        if (event.type == KEYDOWN and event.key == K_ESCAPE) or mario.reset == 1:
            block_list.empty()
            levelSelectionDraw()
            screen.blit(menuCurseurImage, levelCurseurList[levelCurseurPos])
            music_menu(volume_default)
            mario.rect.x, mario.rect.y = 0, 0
            monstres.rect.x, monstres.rect.y = 100, 300
            jeu, levelSelection, levelCurrent, generation_level = 0, 1, -1, 1
            pygame.key.set_repeat(0, 0)
            mario.reset = 0
            mario.time = 210

    clock.tick(60)
    pygame.display.flip()

pygame.quit()