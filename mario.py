from classes import *

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if menu:
            screen.blit(menuImage, (0, 0))
            menuCurseurPos = choixMenu(event, menuCurseurPos)
            screen.blit(menuCurseurImage, menu_Curseur_Coord[menuCurseurPos])
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
            screen.blit(menuCurseurImage, levelSelection_Curseur_Coord[levelCurseurPos])
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, levelSelection = 1, 0
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, levelSelection, jeu, levelCurrent = 0, 0, 1, levelCurseurPos
        elif jeu:
            jeuFonct(event, niveau.mario)

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

        """if mario.mush == 1:
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
            mario.pick = 0"""

        if niveau.mario.time == 210: #Tant que Mario n'est pas mouru
            screen.blit(bg_list[levelCurrent], (0, 0))
            block_list.update()
            block_list.draw(screen)
            active_sprite_list.draw(screen)
            nomarioMovement(monstres_list)
            active_sprite_list.update()
        else:
            if niveau.mario.time > 0:
                niveau.mario.time -= 1
            if niveau.mario.time == 0:
                niveau.mario.reset = 1

        if (event.type == KEYDOWN and event.key == K_ESCAPE) or niveau.mario.reset == 1:
            jeu, levelSelection, levelCurrent, generation_level = niveau.reset(levelCurseurPos)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()