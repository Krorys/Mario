from const import *

def volume_down(volume_default, volume):
    pygame.mixer.pause()
    if volume_default > 0.05 and volume_default < 1.05:
        volume_default -= 0.1
    if volume > 0 and volume < 11:
        volume -= 1
    return (volume_default, volume)


def volume_up(volume_default, volume):
    pygame.mixer.pause()
    if volume_default > -0.5 and volume_default < 0.95:
        volume_default += 0.1
    if volume > -1 and volume < 10:
        volume += 1
    return (volume_default, volume)


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


def music_menu():
    pygame.mixer.stop()
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    menu_music.set_volume(volume_default)
    menu_music.play()


def jump_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    jump_sound.set_volume(volume_default)
    jump_sound.play()


def upgrade_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    upgrade_sound.set_volume(volume_default)
    upgrade_sound.play()

def deUpgrade_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    deUpgrade_sound.set_volume(volume_default)
    deUpgrade_sound.play()

def liveUp_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    liveUp_sound.set_volume(volume_default)
    liveUp_sound.play()


def coin_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    coin_sound.set_volume(volume_default)
    coin_sound.play()

def goomba_stomp_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    goomba_stomp_sound.set_volume(volume_default)
    goomba_stomp_sound.play()


def item_block_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    bloc_item_sound.set_volume(volume_default)
    bloc_item_sound.play()


def death_sound_play(volume_default):
    pygame.mixer.stop()
    death_sound.set_volume(volume_default)
    death_sound.play()


def levelSelectionDraw():
    screen.blit(levelselection_bg, (0, 0))
    Coord = [0, 1, 2, 3]
    for x in Coord:
        screen.blit(levelselection_list[x], levelSelection_Stages_Coord[x])


def doubleImage(image, perso):
    if perso == 1:
        imagex2 = pygame.transform.scale(image, (27, 48))
    elif perso == 2:
        imagex2 = pygame.transform.scale(image, (33, 27))
    elif perso == 3:
        imagex2 = pygame.transform.scale(image, (27, 27))
    else:
        imagex2 = pygame.transform.scale2x(image)  # Double la taille du truc
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


def nomarioMovement(monstres_list, item_list):
    for monstres in monstres_list:
        if monstres.direct == 1: #direct = 1 -> droite
            monstres.goRight()
        if monstres.direct == 0: #direct = 0 -> gauche
            monstres.goLeft()
        if monstres.direct == 2:
            monstres.stop()
    for item in item_list:
        if item.isCoin == 0:
            if item.direct == 1:
                item.goRight()
            if item.direct == 0:
                item.goLeft()
            if item.direct == 2:
                item.stop()


def coinDisparition():
    for coin in item_list:
        if coin.isCoin == 1:
            if coin.time > 0:
                coin.time -= 1
            if coin.time == 0:
                active_sprite_list.remove(coin)
                item_list.remove(coin)



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
        if event.key == K_e and mario.onFire == 1:
            print("Boule de feu")
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