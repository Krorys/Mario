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
        screen.blit(volume_bar, (404, 159))
        for x in range(0, volume):
            coordX = 406 + 7 * x
            screen.blit(volume_redsquare, (coordX, 161))


def music_levels(levelCurrent):
    pygame.mixer.stop()
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
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
def fireball_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    fireball_sound.set_volume(volume_default)
    fireball_sound.play()
def death_sound_play():
    pygame.mixer.stop()
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    death_sound.set_volume(volume_default)
    death_sound.play()
def chainsaw_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    chainsaw_sound.set_volume(volume_default)
    chainsaw_sound.play()
def mario_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    mario_sound.set_volume(volume_default)
    mario_sound.play()
def boomerang_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    boomerang_sound.set_volume(volume_default)
    boomerang_sound.play()
def boomerang_return_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    boomerang_return_sound.set_volume(volume_default)
    boomerang_return_sound.play()
def wall_sound_play():
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    wall_sound.set_volume(volume_default)
    wall_sound.play()


def levelSelectionDraw():
    screen.blit(levelselection_bg, (0, 0))
    for x in range (0,4):
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
        if event.key == K_DOWN and pos < 2: pos += 1  # On peut descendre qu'en étant en haut
        if event.key == K_UP and pos > 0: pos -= 1    # Et inversement
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

def itemUpdate():
    for item in item_list:

        #Pièce
        if item in coin_list:
            if item.time > 0:
                item.time -= 1
            if item.time == 0:
                active_sprite_list.remove(item)
                item_list.remove(item)

        #FireBall
        if item in fireball_list:
            if item.time > 0:
                item.time -= 1
            if item.time == 0:
                fireball_list.remove(item)
                active_sprite_list.remove(item)
                item_list.remove(item)

        #Ghost Razorblade
        if item.isShuriken and item.isGhost:
                if item.time > 0:
                    item.time -= 1

                if item.time < 15:
                    if item.direct == 1: item.changeX -= 3
                    else: item.changeX += 3
                elif item.time < 5:
                    if item.direct == 1: item.changeX -= 3
                    else: item.changeX += 3

                if item.time == 0: #Fin de l'aller
                    boomerang_return_sound_play()
                    item.time = 130
                    if item.direct == 1: item.direct = 0
                    elif item.direct == 0: item.direct = 1

                if item.time == 50: #Fin du retour
                    active_sprite_list.remove(item)
                    item_list.remove(item)
                    shuriken_list.remove(item)

def nomarioMovement(monstres_list, item_list):

    #Déplacements monstres
    for monstres in monstres_list:
        if monstres.direct == 1: #direct = 1 -> droite
            monstres.goRight()
        if monstres.direct == 0: #direct = 0 -> gauche
            monstres.goLeft()
        if monstres.direct == 2:
            monstres.stop()

    #Déplacements items
    for item in item_list:
        if item not in coin_list:
            if item.direct == 1:
                item.goRight()
            if item.direct == 0:
                item.goLeft()
            if item.direct == 2:
                item.stop()


def jeuFonct(event, mario, SpriteImage, FireBall, Shuriken):
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            mario.goRight()
        if event.key == K_LEFT:
            mario.goLeft()
        if (event.key == K_UP or event.key == K_SPACE) and mario.time == 210:
            mario.jump()
        if event.key == K_DOWN:
            mario.duckOn = 1

        #FireBall
        if event.key == K_e and mario.onFire == 1:
            fireball_sound_play()
            itemSheet = SpriteImage("images/item sheet.png", blancFond, 0)
            fireball = FireBall(itemSheet.get_imageXY(104, 84, 111, 91))
            fireball.rect.x = mario.rect.x + 10
            fireball.rect.y = mario.rect.y
            if mario.lookat == 'right':
                fireball.direct = 1
            else:
                fireball.direct = 0
            active_sprite_list.add(fireball)

        #Ghost Razorblade
        if event.key == K_r and mario.time == 210 and (len(shuriken_list) == 0):
            mario_sound_play(), boomerang_sound_play()
            spriteSheet = SpriteImage("images/Shuriken.png", blancFond, 0)
            shuriken = Shuriken(spriteSheet.get_imageXY(32, 172, 49, 189))
            shuriken_list.add(shuriken)
            active_sprite_list.add(shuriken)
            shuriken.rect.y = mario.rect.y - 1
            shuriken.isGhost = 1
            if mario.lookat == 'right':
                shuriken.direct = 1
                shuriken.rect.x = mario.rect.x + 30
            else:
                shuriken.direct = 0
                shuriken.rect.x = mario.rect.x - 49

        #Razorblade
        if event.key == K_t and mario.time == 210 and (len(shuriken_list2) != 3 and mario.recharge > 0):
            mario.recharge -= 1
            mario_sound_play(), boomerang_sound_play()
            spriteSheet = SpriteImage("images/Shuriken.png", blancFond, 0)
            shuriken = Shuriken(spriteSheet.get_imageXY(32, 131, 49, 148))
            shuriken_list2.add(shuriken)
            active_sprite_list.add(shuriken)
            shuriken.walk_l = [(spriteSheet.get_imageXY(92, 131, 109, 148)), (spriteSheet.get_imageXY(72, 131, 89, 148)),
                               (spriteSheet.get_imageXY(53, 131, 69, 148)), (spriteSheet.get_imageXY(32, 131, 49, 148))]
            shuriken.walk_r = [(spriteSheet.get_imageXY(32, 153, 49, 170)), (spriteSheet.get_imageXY(53, 153, 69, 170)),
                               (spriteSheet.get_imageXY(72, 153, 88, 170)), (spriteSheet.get_imageXY(92, 153, 109, 170))]
            shuriken.isBlade = 1
            shuriken.rect.y = mario.rect.y - 1
            if mario.lookat == 'right':
                shuriken.rect.x = mario.rect.x + 30
                shuriken.direct = 1
            else:
                shuriken.rect.x = mario.rect.x - 50
                shuriken.direct = 0

        #
        #if event.key == K_y and mario.time == 210:

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