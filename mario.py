from advanced_foncts import *

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if menu:
            screen.blit(menuImage, (0, 0))
            menuCurseurPos = choixMenu(event, menuCurseurPos)
            screen.blit(menuCurseurImage, menu_Curseur_Coord[menuCurseurPos])
            if event.type == KEYDOWN and event.key == K_RETURN:
                levelSelection, optionsOn, controlsOn, continuer = menuTo(menuCurseurPos)
                menu = 0
        elif optionsOn:
            screen.blit(options, (0, 0))
            affichage_volume(volume)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, optionsOn = 1, 0
            if event.type == KEYDOWN and event.key == K_LEFT:  # Baisser le son
                volume_default, volume = volume_down(volume_default, volume)
                affichage_volume(volume)
                menu_music.set_volume(volume_default)
                pygame.mixer.unpause()
                break
            if event.type == KEYDOWN and event.key == K_RIGHT: # Augmenter le son
                volume_default, volume = volume_up(volume_default, volume)
                affichage_volume(volume)
                menu_music.set_volume(volume_default)
                pygame.mixer.unpause()
                break
        elif controlsOn:
            screen.blit(controls, (0,0))
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, controlsOn = 1, 0
        elif levelSelection:
            levelSelectionDraw()
            levelCurseurPos = choixLevel(event, levelCurseurPos)
            screen.blit(menuCurseurImage, levelSelection_Curseur_Coord[levelCurseurPos])
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                menu, levelSelection = 1, 0
            if event.type == KEYDOWN and event.key == K_RETURN:
                menu, levelSelection, jeu, levelCurrent = 0, 0, 1, levelCurseurPos
        elif jeu:
            jeuFonct(event, niveau.mario, SpriteImage, FireBall, Shuriken)

    if jeu:
        choix = "n" + str(levelCurrent + 1) + ".txt"
        if generation_level:
            niveau = generation(choix, levelCurrent)
            generation_level = 0

        if niveau.mario.time == 210: #Tant que Mario n'est pas mouru
            boucle_jeu(levelCurrent, niveau)
        else:
            mort(niveau, levelCurrent)

        if (event.type == KEYDOWN and event.key == K_ESCAPE) or niveau.mario.reset == 1:
            jeu, levelSelection, levelCurrent, generation_level = niveau.reset(levelCurseurPos)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()