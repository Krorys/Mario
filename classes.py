from foncts import *

class SpriteImage():
    sprite_image = None

    def __init__(self, file_name, couleur, perso):
        self.sprite_image = pygame.image.load(file_name)
        self.couleur = couleur
        self.perso = perso

    def get_imageXY(self, x, y, x2, y2):
        largeur, hauteur = 1 + x2 - x, 1 + y2 - y
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(self.couleur)
        imagex2 = doubleImage(image, self.perso)
        return imagex2


class Mario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        spriteSheet = SpriteImage("images/mario sheet.png", vertFond, 1)
        self.itemSheet = SpriteImage("images/item sheet.png", blancFond, 0)
        self.walk_r = [spriteSheet.get_imageXY(72, 37, 87, 63),
                       spriteSheet.get_imageXY(104, 36, 120, 62),
                       spriteSheet.get_imageXY(136, 37, 151, 63),
                       spriteSheet.get_imageXY(168, 37, 183, 63)]
        self.walkHold_r = [spriteSheet.get_imageXY(72, 69, 88, 95),
                           spriteSheet.get_imageXY(103, 68, 120, 94),
                           spriteSheet.get_imageXY(136, 69, 152, 95),
                           spriteSheet.get_imageXY(168, 69, 184, 95)]
        self.stand_r = [spriteSheet.get_imageXY(72, 5, 87, 31),
                        spriteSheet.get_imageXY(104, 4, 119, 31),
                        spriteSheet.get_imageXY(136, 3, 151, 31),
                        spriteSheet.get_imageXY(168, 4, 183, 31),
                        spriteSheet.get_imageXY(200, 5, 215, 31)]
        self.jump_r = [spriteSheet.get_imageXY(72, 99, 89, 126),
                       spriteSheet.get_imageXY(104, 100, 121, 126)]
        self.duck_r = spriteSheet.get_imageXY(73, 165, 88, 191)
        self.dead = spriteSheet.get_imageXY(67, 242, 92, 271)
        self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.stand_l = [pygame.transform.flip(x, True, False) for x in self.stand_r]
        self.jump_l = [pygame.transform.flip(x, True, False) for x in self.jump_r]
        self.duck_l = pygame.transform.flip(self.duck_r, True, False)
        self.stand = 0
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.lookat = "right"
        self.duckOn = 0
        self.rect = self.image.get_rect()
        self.reset = 0
        self.time = 210
        self.hp = 3
        self.killEnnemy = 0
        self.willDie = 0
        self.pick = 0
        self.mush = 0
        self.killed = None
        self.deadOn = 0
        self.upgraded = 0
        self.isMario = 0
        self.niveauScroll = 0
        self.isScrolling = 0

    def update(self):
        if self.deadOn == 0:
            if (self.rect.x < screenX/2-25 and self.changeX < 0) or (self.rect.x > 25+screenX-screenX/2 and self.changeX > 0):
                self.scroll(-self.changeX)
                self.isScrolling = 1
            else:
                self.isScrolling = 0
            self.direction()
            if self.duckOn == 1: self.duck()
            self.grav()



            self.rect.x += self.changeX

            block_hit_list = pygame.sprite.spritecollide(self, block_list, False)                    #Collisions X blocs
            for block in block_hit_list:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                elif self.changeX < 0:
                    self.rect.left = block.rect.right

            self.rect.y += self.changeY

            block_hit_list = pygame.sprite.spritecollide(self, block_list, False)                    #Collisions Y blocs
            for block in block_hit_list:
                if self.changeY > 0:
                    self.rect.bottom = block.rect.top
                    if block.deadly == 1:
                        self.death()
                elif self.changeY < 0:
                    self.rect.top = block.rect.bottom
                    if block.item_activation == 0 and block.used == 0:
                        block_list.remove(block)
                        volume_default = pygame.mixer.Sound.get_volume(menu_music)
                        bloc_break_sound.set_volume(volume_default)
                        bloc_break_sound.play()
                    elif block.item_activation == 1:
                        mushroomStand = self.itemSheet.get_imageXY(163, 43, 178, 58)
                        mushroom = Item(mushroomStand)
                        mushroom.mush = 1
                        active_sprite_list.add(mushroom)
                        mushroom.rect.y = self.rect.y - 80
                        mushroom.rect.x = self.rect.x
                        block.image = pygame.image.load("images/usedBlock.jpg")
                        item_block_play()
                        block.item_activation = 0
                        block.used = 1

                self.changeY = 0
            flag_hit_list = pygame.sprite.spritecollide(self, flag_list, False)
            for flag in flag_hit_list:
                print(flag.flag, flag.pos, flag.fin)
                if flag.fin != len(flag_hit_list):
                    self.lastCheckpoint = flag.pos
                else:
                    self.reset = 1

            item_hit_list = pygame.sprite.spritecollide(self, item_list, False)                        #Collisions items
            for item in item_hit_list:
                if item.mush == 1 and self.upgraded == 1:
                    print("Overdose de champignon!")
                if item.mush == 1:
                    item_list.remove(item)
                    active_sprite_list.remove(item)
                    upgrade_sound_play()
                    self.upgraded = 1


            monstres_hit_list = pygame.sprite.spritecollide(self, monstres_list, False)             #Collisions monstres
            for goomba in monstres_hit_list:
                if self.changeY > 0:
                    self.rect.y -= 5
                    self.changeY = -5
                    goomba_stomp_play()
                    monstres_list.remove(goomba)
                    active_sprite_list.remove(goomba)
                else:
                    self.death()

            if self.rect.y >= screenY:
                self.death()


    def grav(self):
        if self.changeY == 0:  # Si il est au sol
            self.changeY = 1
        else:
            if self.changeY <= 10:  # Pour cap la vitesse maximale en tombant
                self.changeY += 0.40

    def goLeft(self):
        self.changeX = -3
        self.lookat = "left"
        self.duckOn = 0

    def goRight(self):
        self.changeX = 3
        self.lookat = "right"
        self.duckOn = 0

    def duck(self):
        if self.changeY == 0:
            self.changeX = 0
            if self.lookat == "right":
                self.image = self.duck_r
            else:
                self.image = self.duck_l

    def stop(self):
        self.changeX = 0
        self.stand = 0

    def direction(self):
            if self.lookat == "right":  # Si il regardre à droite
                if self.changeY == 0:  #Si il est au sol
                    if self.changeX == 0:  #et si il ne bouge pas
                        if self not in monstres_list:
                            frame = (self.stand // 18) % len(self.stand_r)
                            self.image = self.stand_r[frame]
                            self.stand += 1
                    else:  #Si il marche
                        if self in monstres_list:
                            frame = (self.rect.x // 20) % len(self.walk_r)
                        else:
                            if self.isScrolling == 1:
                                frame = (self.rect.x + self.niveauScroll // 30) % len(self.walk_r)
                            else:
                                frame = (self.rect.x  // 30) % len(self.walk_r)
                        self.image = self.walk_r[frame]
                else:  #Si il est en l'air
                    if self.changeY >= 5:  #Si Mario tombe
                        self.image = self.jump_r[1]
                    else:  #Si il saute
                        self.image = self.jump_r[0]
            else:  # Si il regarde à gauche
                if self.changeY == 0:  #Si il est au sol
                    if self.changeX == 0:  #et si il ne bouge pas
                        if self not in monstres_list:
                            frame = (self.stand // 18) % len(self.stand_l)
                            self.image = self.stand_l[frame]
                            self.stand += 1
                    else:  #Si il marche
                        if self in monstres_list:
                            frame = (self.rect.x // 20) % len(self.walk_l)
                        else:
                            if self.isScrolling == 1:
                                frame = (self.rect.x + self.niveauScroll // 30) % len(self.walk_l)
                            else:
                                frame = (self.rect.x // 30) % len(self.walk_l)
                        self.image = self.walk_l[frame]
                else:  #Si il est en l'air
                    if self.changeY >= 5:  #Si Mario tombe
                        self.image = self.jump_l[1]
                    else:  #Si il saute
                        self.image = self.jump_l[0]

    def jump(self):
        if len(block_list) == 0 or self.changeY == 0:
            self.rect.y -= 5
            self.changeY = -10
            jump_sound_play()

    def death(self):
        self.image = self.dead
        gameOverSprite = SpriteImage("images/game over.png", noirFond, 0)
        gameOver = gameOverSprite.get_imageXY(93, 111, 172, 126)
        GOrect = gameOver.get_rect()
        centerX = int((screenX / 2) - GOrect.centerx)
        centerY = int((screenY / 2) - GOrect.centery)
        volume_default = pygame.mixer.Sound.get_volume(menu_music)
        screen.blit(gameOver, (centerX, centerY))
        for monstre in monstres_list:
            monstre.direct = 2
        self.deadOn = 1
        if self.time == 210: death_sound_play(volume_default)
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.reset = 1

    def scroll(self, sens):
        for x in block_list:
            x.rect.x += sens
        for x in flag_list:
            x.rect.x += sens
        for x in active_sprite_list:
            if x.isMario == 1:
                x.rect.x += sens
                x.niveauScroll += sens
            else:
                x.rect.x += sens


class Monstres(Mario):
    def __init__(self, image):
        super().__init__(image)
        spriteSheet = SpriteImage("images/goomba sheet.png", blancFond, 2)
        self.walk_r = [spriteSheet.get_imageXY(1, 40, 17, 59),
                       spriteSheet.get_imageXY(41, 41, 58, 59),
                       spriteSheet.get_imageXY(80, 41, 99, 59),
                       spriteSheet.get_imageXY(121, 41, 138, 59)]
        self.stand_r = self.walk_r[0]
        self.jump_r = [spriteSheet.get_imageXY(1, 41, 17, 60),
                       spriteSheet.get_imageXY(1, 41, 17, 60)]
        self.stomp = spriteSheet.get_imageXY(157, 87, 182, 94)
        self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.jump_l = [pygame.transform.flip(x, True, False) for x in self.jump_r]
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.lookat = "right"
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.direct = 1
        self.nodirection = 0

    def goRight(self):
        self.changeX = 1
        self.lookat = "right"

    def goLeft(self):
        self.changeX = -1
        self.lookat = "left"

    def update(self):
        if self.nodirection == 0:
            self.direction()
        self.grav()

        self.rect.x += self.changeX
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeX > 0:
                self.direct = 0
                self.rect.right = block.rect.left
            elif self.changeX < 0:
                self.direct = 1
                self.rect.left = block.rect.right

        self.rect.y += self.changeY

        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                self.rect.top = block.rect.bottom

            self.changeY = 0


class Item(Monstres):
    def __init__(self, image):
        super().__init__(image)
        spriteSheet = SpriteImage("images/item sheet.png", blancFond, 0)
        self.walk_r = spriteSheet.get_imageXY(1, 43, 16, 58)
        self.jump_r = self.walk_r
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100
        self.direct = 1
        self.mush = 0
        self.nodirection = 1
        item_list.add(self)


class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.changeX = 0
        self.changeY = 0
        self.item_activation = 0
        self.used = 0
        self.deadly = 0


class Sol(Block):
    def __init__(self, image, x, y):
        Block.__init__(self, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Flag(Block):
    flag = []
    def __init__(self, image, x, y):
        Block.__init__(self, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = len(self.flag)
        self.flag.append(self.pos)
        self.fin = 0


class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        self.goombaSheet = SpriteImage("images/goomba sheet.png", blancFond, 2)
        self.marioSheet = SpriteImage("images/mario sheet.png", vertFond, 1)
        self.itemSheet = SpriteImage("images/item sheet.png", blancFond, 0)
        self.mario = Mario(self.marioSheet.get_imageXY(72, 5, 87, 31))


    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau


    def afficher(self):
        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite

                if sprite == 'b':
                    Block = Sol("images/Block.jpg", x, y)
                    block_list.add(Block)

                elif sprite == 'x':
                    xBlock = Sol("images/xBlock.jpg", x, y)
                    block_list.add(xBlock)

                elif sprite == 'i':
                    itemBlock = Sol("images/itemBlock.jpg", x, y)
                    itemBlock.item_activation = 1
                    block_list.add(itemBlock)

                elif sprite == 'l':
                    lavaBlock = Sol("images/lavaBlock.jpg", x, y)
                    lavaBlock.deadly = 1
                    block_list.add(lavaBlock)

                elif sprite == 'g':
                    goombaStand = self.goombaSheet.get_imageXY(1, 41, 17, 59)
                    goomba = Monstres(goombaStand)
                    goomba.rect.x = x
                    goomba.rect.y = y - 9
                    monstres_list.add(goomba)
                    active_sprite_list.add(goomba)

                elif sprite == 'm':
                    self.mario.isMario = 1
                    self.mario.rect.x = x
                    self.mario.rect.y = y
                    active_sprite_list.add(self.mario)

                elif sprite == 'f':
                    flag = Flag("images/itemBlock.jpg", x, y)
                    flag_list.add(flag)

                elif sprite == 'F':
                    flag = Flag("images/itemBlock.jpg", x, y)
                    flag.fin = 1
                    flag_list.add(flag)

                num_case += 1
            num_ligne += 1

    def reset(self, levelCurseurPos):
        Flag.flag = []
        flag_list.empty()
        block_list.empty()
        monstres_list.empty()
        item_list.empty()
        active_sprite_list.empty()
        levelSelectionDraw()
        screen.blit(menuCurseurImage, levelSelection_Curseur_Coord[levelCurseurPos])
        music_menu()
        jeu, levelSelection, levelCurrent, generation_level = 0, 1, -1, 1
        self.mario.reset, self.mario.time = 0, 210
        for monstres in monstres_list:
            monstres.direct = 1
        return jeu, levelSelection, levelCurrent, generation_level