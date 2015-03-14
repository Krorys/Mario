from const import *

def affichage_volume(volume):
    if volume > -1 and volume < 11:
        # screen.blit(volume_images[volume], (404,159))
        screen.blit(volume_bar, (404, 159))
        for x in range(0, volume):
            coordX = 406 + 7 * x
            screen.blit(volume_redsquare, (coordX, 161))


def music_levels(levelCurrent, volume_default):
    pygame.mixer.stop()
    levels_music[levelCurrent].set_volume(volume_default)
    levels_music[levelCurrent].play()


def music_menu(volume_default):
    pygame.mixer.stop()
    menu_music.set_volume(volume_default)
    menu_music.play()


def jump_sound_play(volume_default):
    jump_sound.set_volume(volume_default)
    jump_sound.play()


def death_sound_play(volume_default):
    pygame.mixer.stop()
    death_sound.set_volume(volume_default)
    death_sound.play()


def levelSelectionDraw():  # Fonction qui re-dessine levelselection
    screen.blit(levelselection_bg, (0, 0))
    Coord = [0, 1, 2, 3]
    for x in Coord:
        screen.blit(levelselection_list[x], levelSelection_Stages_Coord[x])


def doubleImage(image, mario):
    if mario:
        imagex2 = pygame.transform.scale(image, (29, 50))
    else:
        imagex2 = pygame.transform.scale2x(image)  # Double la taille du Mario
    return imagex2


def choixMenu(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_DOWN and pos < 2:  # On peut descendre qu'en étant en haut
            pos += 1
        if event.key == K_UP and pos > 0:  # Et inversement
            pos -= 1
    return pos


def menuTo(pos):
    valeurs = [0, 0, 1]
    valeurs[pos] = abs(valeurs[pos] - 1)  # si c'est à 0 -> 1, si c'est à 1->0
    return valeurs  # [levelSelection, optionsOn, continuer]


def choixLevel(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_DOWN and pos < 3:
            pos = (pos + 2) % 4
        if event.key == K_UP and pos > 0:
            pos = (pos - 2) % 4
        if event.key == K_LEFT:
            pos = (pos - 1) % 4
        if event.key == K_RIGHT:
            pos = (pos + 1) % 4
    return pos


def nomarioMovement(monstres_list):
    for monstres in monstres_list:
        if monstres.direct == 1: #si direct = 1 le monstre va à droite
            monstres.goRight()
        if monstres.direct == 0: #si direct = 0 le monstre ira à gauche
            monstres.goLeft()
        if monstres.direct == 2:
            monstres.stop()


def jeuFonct(event, mario):
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            mario.goRight()
        if event.key == K_LEFT:
            mario.goLeft()
        if event.key == K_UP or event.key == K_SPACE:
            mario.jump()
        if event.key == K_DOWN:
            mario.duckOn = 1
    if event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            mario.stop()
        if event.key == K_DOWN:
            mario.duckOn = 0


def niveauFonct(niveau, choix, screen, fonct):
    if fonct == 0:
        niveau.generer()
    else:
        screen.blit(bg, (0, 0))
        niveau.afficher(screen)