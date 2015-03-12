__author__ = 'Chèvre'

import sys

import pygame
from pygame.locals import *

from const import *
from classes_foncts import *


# Sprites
marioSprite = SpriteImage("images/mario sheet.png", vertFond, 1)
goombaSprite = SpriteImage("images/goomba sheet.png", blancFond, 1)
itemSprite = SpriteImage("images/item_sheet.png", blancFond, 1)
marioStand = marioSprite.get_imageXY(72, 5, 87, 31)
monstresStand = goombaSprite.get_imageXY(72, 5, 87, 31)
mushroomStand = itemSprite.get_imageXY(1, 43, 16, 58)
mario = Mario(marioStand)
monstres = Monstres(monstresStand)
mushroom = Item(mushroomStand)

gameOverSprite = SpriteImage("images/game over.png", noirFond, 0)
gameOver = gameOverSprite.get_imageXY(5, 7, 260, 230)

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(mario)
active_sprite_list.add(monstres)
#active_sprite_list.add(mushroom)

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

        if ((pygame.sprite.collide_rect(mario, monstres)) and mario.willDie == 1) or (mario.rect.y >= screenY) :
            screen.blit(bg_list[levelCurrent], (0, 0))
            block_list.draw(screen)
            block_list_special.draw(screen)
            active_sprite_list.draw(screen)
            mario.death()

        if mario.mush == 1:
            mushroom = Item(mushroomStand)
            active_sprite_list.add(mushroom)
            mushroom.rect.y = mario.rect.y - 80
            mushroom.rect.x = mario.rect.x
            mario.mush = 0

        if mario.pick == 1: #Bug si 2champis en même temps dans l'écran, au pire on s'en fou
            active_sprite_list.remove(mushroom)
            active_sprite_list.update()
            mushroom.update()
            volume_default = pygame.mixer.Sound.get_volume(menu_music)
            item_sound.set_volume(volume_default)
            item_sound.play()
            mario.pick = 0

        if mario.killEnnemy == 1:
            active_sprite_list.remove(monstres)
            active_sprite_list.update()
            monstres.update()
            mario.rect.y -= 5
            mario.changeY = -5
            mario.update()
            volume_default = pygame.mixer.Sound.get_volume(menu_music)
            goomba_stomp.set_volume(volume_default)
            goomba_stomp.play()
            mario.killEnnemy = 0
            willRespawn = 1

        if mario.time == 210: #Tant que Mario n'est pas mouru
            screen.blit(bg_list[levelCurrent], (0, 0))
            block_list.update()
            block_list_special.update()
            block_list_used.update()
            block_list.draw(screen)
            block_list_special.draw(screen)
            block_list_used.draw(screen)
            monstresMovement(monstres, mushroom)
            active_sprite_list.update()
            active_sprite_list.draw(screen)

        if (event.type == KEYDOWN and event.key == K_ESCAPE) or mario.reset == 1:
            block_list.empty()
            block_list_special.empty()
            block_list_used.empty()
            active_sprite_list.remove(mushroom)
            levelSelectionDraw()
            screen.blit(menuCurseurImage, levelCurseurList[levelCurseurPos])
            music_menu(volume_default)
            mario.rect.x, mario.rect.y = 0, 0
            monstres.rect.x, monstres.rect.y = 100, 300
            jeu, levelSelection, levelCurrent, generation_level = 0, 1, -1, 1
            pygame.key.set_repeat(0, 0)
            mario.reset, mario.time = 0, 210
            monstres.direct, mushroom.direct = 1, 1
            if willRespawn == 1:
                monstres = Monstres(monstresStand)
                active_sprite_list.add(monstres)
                willRespawn = 0

    clock.tick(60)
    pygame.display.flip()

pygame.quit()