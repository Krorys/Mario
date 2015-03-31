from const import *

def ecran_menu_blit(x):
    screen.blit(menu_fond, (0, 0))
    screen.blit(images_menu_list[x], (0, 0))

def choixMenu(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_DOWN and pos < 3: pos += 1  # On peut descendre qu'en étant en haut
        if event.key == K_UP and pos > 0: pos -= 1    # Et inversement
    return pos

def choixControls(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_RIGHT and pos < 3: pos += 1
        if event.key == K_LEFT and pos > 0: pos -= 1
    return pos

def controlsBlit(pos):
    for x in range (0,4):
        if pos == x:
            screen.blit(description_skills[x], (60, 210))

def menuTo(pos):
    valeurs = [0, 0, 0, 1]
    valeurs[pos] = abs(valeurs[pos] - 1)  # si c'est à 0 -> 1, si c'est à 1->0
    return valeurs  # [levelSelection, optionsOn, continuer]


def volume_down(volume_default, volume):
    if volume_default > 0.05 and volume_default < 1.05:
        volume_default -= 0.1
    if volume > 0 and volume < 11:
        volume -= 1
    return (volume_default, volume)
def volume_up(volume_default, volume):
    if volume_default > -0.5 and volume_default < 0.95:
        volume_default += 0.1
    if volume > -1 and volume < 10:
        volume += 1
    return (volume_default, volume)
def affichage_volume(volume):
    if volume > -1 and volume < 11:
        screen.blit(volume_bar, (329, 174))
        for x in range(0, volume):
            coordX = 331 + 7 * x
            screen.blit(volume_redsquare, (coordX, 176))
def volumeApply(volume_default, volume):
    screen.blit(menu_fond, (0, 0))
    screen.blit(images_menu_list[1], (0, 0))
    affichage_volume(volume)
    menu_music.set_volume(volume_default)


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
def sound_play(x):
    volume_default = pygame.mixer.Sound.get_volume(menu_music)
    sound_list[x].set_volume(volume_default)
    sound_list[x].play()


def levelSelectionDraw():
    ecran_menu_blit(3)
    for x in range (0,4):
        screen.blit(levelselection_list[x], levelSelection_Stages_Coord[x])
def levelSelectionBlit(levelCurseurPos):
    levelSelectionDraw()
    screen.blit(menuCurseurImage, levelSelection_Curseur_Coord[levelCurseurPos])
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


def MarioActualSheet(self, SpriteImage, x):
    if x == 0: #Mario de base
        Sheet = SpriteImage("images/mario sheet.png", vertFond, 1)
        self.stand_r = [Sheet.get_imageXY(72, 5, 87, 31), Sheet.get_imageXY(104, 4, 119, 31), Sheet.get_imageXY(136, 3, 151, 31),
                        Sheet.get_imageXY(168, 4, 183, 31), Sheet.get_imageXY(200, 5, 215, 31)]
        self.walk_r = [Sheet.get_imageXY(72, 37, 87, 63), Sheet.get_imageXY(104, 36, 120, 62),
                       Sheet.get_imageXY(136, 37, 151, 63), Sheet.get_imageXY(168, 37, 183, 63)]
        self.jump_r = [Sheet.get_imageXY(72, 99, 89, 126), Sheet.get_imageXY(104, 100, 121, 126)]
        self.duck_r = Sheet.get_imageXY(73, 165, 88, 191)
        self.dead = Sheet.get_imageXY(67, 242, 92, 271)
        self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.stand_l = [pygame.transform.flip(x, True, False) for x in self.stand_r]
        self.jump_l = [pygame.transform.flip(x, True, False) for x in self.jump_r]
        self.duck_l = pygame.transform.flip(self.duck_r, True, False)
        self.image = Sheet.get_imageXY(72, 5, 87, 31)
    elif x == 1: #Mario de feu
        Sheet = SpriteImage("images/mario sheet.png", vertFond, 1)
        self.stand_r = [Sheet.get_imageXY(316, 6, 331, 32), Sheet.get_imageXY(348, 5, 363, 32), Sheet.get_imageXY(380, 4, 395, 32),
                        Sheet.get_imageXY(412, 5, 427, 32), Sheet.get_imageXY(444, 6, 459, 32)]
        self.walk_r = [Sheet.get_imageXY(317, 43, 332, 69), Sheet.get_imageXY(349, 42, 365, 68),
                       Sheet.get_imageXY(381, 43, 396, 69), Sheet.get_imageXY(413, 43, 428, 69)]
        self.jump_r = [Sheet.get_imageXY(317, 78, 334, 105), Sheet.get_imageXY(349, 79, 366, 105)]
        self.duck_r = Sheet.get_imageXY(318, 114, 333, 140)
        self.stand_l = [pygame.transform.flip(x, True, False) for x in self.stand_r]
        self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.jump_l = [pygame.transform.flip(x, True, False) for x in self.jump_r]
        self.duck_l = pygame.transform.flip(self.duck_r, True, False)
        self.image = Sheet.get_imageXY(316, 6, 331, 32)
    elif x == 2: #Mario tornade
        Sheet = SpriteImage("images/tornado_sheet.png", kakiFond, 0)
        self.walk_r = [Sheet.get_imageXY(9, 15, 50, 56),
                       Sheet.get_imageXY(77, 15, 122, 56),
                       Sheet.get_imageXY(144, 15, 186, 56),
                       Sheet.get_imageXY(210, 15, 248, 56)]
        self.jump_r = self.walk_r
        self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.jump_l = [pygame.transform.flip(x, True, False) for x in self.jump_r]
        self.image = Sheet.get_imageXY(9, 15, 50, 56)
def doubleImage(image, perso):
    if perso == -1:
        return image
    if perso == 1:
        imagex2 = pygame.transform.scale(image, (27, 48))
    elif perso == 2:
        imagex2 = pygame.transform.scale(image, (33, 27))
    elif perso == 3:
        imagex2 = pygame.transform.scale(image, (27, 27))
    else:
        imagex2 = pygame.transform.scale2x(image)  # Double la taille du truc
    return imagex2


def itemUpdate(SpriteImage, FireBall, mario):
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

    #Shuriken-boomerang
        if item.isShuriken and item.isBoomerang:
                if item.time > 0:
                    item.time -= 1

                if item.time < 15:
                    if item.direct == 1: item.changeX -= 3
                    else: item.changeX += 3
                elif item.time < 5:
                    if item.direct == 1: item.changeX -= 3
                    else: item.changeX += 3

                if item.time == 0: #Fin de l'aller
                    sound_play(12)
                    item.time = 130
                    if item.direct == 1: item.direct = 0
                    elif item.direct == 0: item.direct = 1

                if item.time == 50: #Fin du retour
                    active_sprite_list.remove(item)
                    item_list.remove(item)
                    shuriken_list.remove(item)

    #Phoenix dance
    if mario.time_tornado > 0:
        x, y = mario.rect.x, mario.rect.y
        mario.time_tornado -= 1
        if mario.lookat == "right": mario.changeX = 1
        elif mario.lookat == 'left': mario.changeX = -1

    if mario.time_tornado % 30 == 0 and mario.time_tornado > 0:
        Sheet = SpriteImage("images/item sheet.png", blancFond, 0)
        fireball1, fireball2 = FireBall(Sheet.get_imageXY(104, 84, 111, 91)), FireBall(Sheet.get_imageXY(104, 84, 111, 91))
        fireball1.rect.x, fireball2.rect.x = mario.rect.x + 40, mario.rect.x + 35
        fireball1.rect.y, fireball2.rect.y = mario.rect.y + 30, mario.rect.y + 30
        fireball1.changeY, fireball2.changeY = -5, -5
        fireball1.direct, fireball2.direct = 1, 0
        active_sprite_list.add(fireball1, fireball2)

    if mario.time_tornado == 0:
        mario.stop()
        Sheet = SpriteImage("images/mario sheet.png", vertFond, 1)
        mario.image = Sheet.get_imageXY(72, 5, 87, 31)
        mario.rect = mario.image.get_rect()
        if mario.lookat == "right": mario.rect.x = x - 20
        elif mario.lookat == 'left': mario.rect.x = x + 20
        mario.time_tornado, mario.onFire, mario.rect.y, mario.isTornado, mario.frameSpeed = -1, 1, 0, 0, 30
def nomarioMovement(monstres_list, item_list, mario):

    #Déplacements monstres
    for monstres in monstres_list:
        if monstres.direct == 1:
            monstres.goRight()
        if monstres.direct == 0:
            monstres.goLeft()
        if monstres.direct == 2:
            monstres.stop()
        if monstres.rect.x > mario.rect.x - mario.niveauScroll -300 and monstres.seen == 0:
            monstres.stop()
        if not monstres.rect.x > mario.rect.x - mario.niveauScroll -300:
            monstres.seen = 1

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
    if mario.isTornado == 0:
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
            if event.key == K_q and mario.onFire == 1:
                sound_play(9)
                Sheet = SpriteImage("images/item sheet.png", blancFond, 0)
                fireball = FireBall(Sheet.get_imageXY(104, 84, 111, 91))
                fireball.rect.x = mario.rect.x + 10
                fireball.rect.y = mario.rect.y
                active_sprite_list.add(fireball)
                if mario.lookat == 'right': fireball.direct = 1
                elif mario.lookat == 'left': fireball.direct = 0

            #Shuriken-boomerang
            if event.key == K_e and mario.time == 210 and (len(shuriken_list) == 0):
                sound_play(10), sound_play(11)
                Sheet = SpriteImage("images/Shuriken.png", blancFond, -1)
                shuriken = Shuriken(Sheet.get_imageXY(32, 172, 49, 189))
                shuriken_list.add(shuriken)
                active_sprite_list.add(shuriken)
                shuriken.rect.y = mario.rect.y + 15
                shuriken.isBoomerang = 1
                #mario.rage += 5
                if mario.lookat == 'right':
                    shuriken.direct = 1
                    shuriken.rect.x = mario.rect.x + 30
                elif mario.lookat == 'left':
                    shuriken.direct = 0
                    shuriken.rect.x = mario.rect.x - 25

            #Shuriken
            if event.key == K_w and mario.time == 210 and mario.recharge > 0:
                mario.recharge -= 1
                sound_play(10), sound_play(11)
                Sheet = SpriteImage("images/Shuriken.png", blancFond, -1)
                shuriken = Shuriken(Sheet.get_imageXY(32, 131, 49, 148))
                shuriken_list2.add(shuriken)
                active_sprite_list.add(shuriken)
                shuriken.walk_l = [(Sheet.get_imageXY(92, 131, 109, 148)), (Sheet.get_imageXY(73, 131, 89, 148)),
                                   (Sheet.get_imageXY(52, 131, 69, 148)), (Sheet.get_imageXY(32, 131, 49, 148))]
                shuriken.walk_r = [(Sheet.get_imageXY(32, 153, 49, 170)), (Sheet.get_imageXY(53, 153, 69, 170)),
                                   (Sheet.get_imageXY(72, 153, 88, 170)), (Sheet.get_imageXY(92, 153, 109, 170))]
                shuriken.isBlade = 1
                shuriken.rect.y = mario.rect.y + 13
                if mario.lookat == 'right':
                    shuriken.rect.x = mario.rect.x + 30
                    shuriken.direct = 1
                else:
                    shuriken.rect.x = mario.rect.x - 21
                    shuriken.direct = 0



        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                mario.stop()
            if event.key == K_DOWN:
                mario.duckOn = 0

    #Phoenix dance
    if (event.type == KEYDOWN and event.key == K_r) and mario.time == 210 and mario.isTornado == 0 and mario.rage > 9:
        x,y = mario.rect.x, mario.rect.y
        mario.rect = mario.image.get_rect()
        if mario.lookat == 'right': mario.rect.x = x
        elif mario.lookat == 'left': mario.rect.x = x -10
        mario.rect.y = y - 35
        mario.time_tornado = 241
        sound_play(15), sound_play(16)
        mario.frameSpeed, mario.onFire, mario.upgraded, mario.isTornado = 4, 2, 1, 1
        mario.rage -= 10
        #mario.stop()
def niveauFonct(niveau, choix, screen, fonct):
    if fonct == 0:
        niveau.generer()
    else:
        screen.blit(bg, (0, 0))
        niveau.afficher(screen)
