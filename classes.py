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


class Perso(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.imageR = image
        self.imageL = pygame.transform.flip(self.image, True, False)
        self.lookat = "right"
        self.rect = self.image.get_rect()
        self.niveauScroll = 0
        self.frameSpeed = 30
        self.isScrolling = 0
        self.speed = 3
        self.direct = 1
        self.isShuriken = 0
        self.gmush = 0
        self.mush = 0
        self.isFlower = 0
        self.isMario = 0
        self.stand = 0

    def update(self):
        self.direction()

        self.grav()

        self.rect.x += self.changeX
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeX > 0:
                self.rect.right = block.rect.left
                self.direct = 0
            elif self.changeX < 0:
                self.rect.left = block.rect.right
                self.direct = 1

        self.rect.y += self.changeY
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                self.rect.top = block.rect.bottom

            self.changeY = 0


    def grav(self):
        if self.changeY == 0:  #Si il ne tombe pas
            self.changeY = 1
        else:
            if self.changeY <= 10:  # Pour cap la vitesse maximale en tombant
                self.changeY += 0.40

    def goLeft(self):
        self.changeX = abs(self.speed)*-1
        self.lookat = "left"

    def goRight(self):
        self.changeX = abs(self.speed)
        self.lookat = "right"

    def stop(self):
        self.changeX = 0

    def direction(self):
        if self.lookat == "right":  # Si il regardre à droite
            self.image = self.imageR
        else:  # Si il regarde à gauche
            self.image = self.imageL

    def jump(self):
        if self.changeY == 0:
            self.rect.y -= 5
            self.changeY = -10

class Mario(Perso):
    def __init__(self, image):
        super().__init__(image)
        self.itemSheet = SpriteImage("images/item sheet.png", blancFond, 3)
        self.stand = 0
        self.changeX = 0
        self.changeY = 0
        self.lookat = "right"
        self.duckOn = 0
        self.reset = 0
        self.time_tornado = -1
        self.time = 210
        self.hp = 3
        self.recharge = 3
        self.willDie = 0
        self.pick = 0
        self.mush = 0
        self.killed = None
        self.deadOn = 0
        self.upgraded = 0
        self.isMario = 1
        self.niveauScroll = 0
        self.isScrolling = 0
        self.isCoin = 0
        self.onFire = 0
        self.canBreak = 0
        self.antiSuperposable = 2
        self.isTornado = 0
        self.frameSpeed = 30
        self.rage = 0

    def update(self):
        if self.deadOn == 0:
            if (self.rect.x < screenX/2-25 and self.changeX < 0) or (self.rect.x > 25+screenX-screenX/2 and self.changeX > 0):
                self.scroll(-self.changeX)
                self.isScrolling = 1
            else:
                self.isScrolling = 0
            if self.duckOn == 1: self.duck()
            if self.onFire == 1:
                MarioActualSheet(self, SpriteImage, 1)
            elif self.onFire == 0:
                MarioActualSheet(self, SpriteImage, 0)
            elif self.isTornado == 1:
                MarioActualSheet(self, SpriteImage, 2)

            self.direction()
            self.grav()

            self.rect.x += self.changeX
            block_hit_list = pygame.sprite.spritecollide(self, block_list, False)                    #Collisions X blocs
            for block in block_hit_list:
                if self.isTornado == 0:
                    if self.changeX > 0:
                        self.rect.right = block.rect.left
                    elif self.changeX < 0:
                        self.rect.left = block.rect.right

            self.rect.y += self.changeY
            block_hit_list = pygame.sprite.spritecollide(self, block_list, False)                    #Collisions Y blocs
            for block in block_hit_list:
                if self.changeY > 0 or (self.isTornado == 1 and not block.isTraversable):
                    self.rect.bottom = block.rect.top
                    if block.deadly == 1:
                        self.death()

                elif self.changeY < 0 and self.isTornado == 0:
                    self.rect.top = block.rect.bottom
                    if block.isBreakable == 1 and (self.upgraded == 1 or self.onFire == 1):
                        block_list.remove(block), sound_play(2)
                    elif block.mushroom_activation == 1:                                                #Champigon rouge
                        if self.upgraded == 0:
                            Sheet = self.itemSheet.get_imageXY(146, 43, 161, 58)
                            mushroom = Item(Sheet)
                            mushroom.mush = 1
                            mushroom.rect.y = block.rect.y - 30
                            mushroom.rect.x = block.rect.x
                            active_sprite_list.add(mushroom), sound_play(3)
                            block.image = pygame.image.load("images/usedBlock.jpg")
                            block.mushroom_activation, block.used = 0, 1
                        elif self.upgraded > 0:                                                                   #Fleur
                            Sheet = self.itemSheet.get_imageXY(214, 43, 227, 58)
                            flower = Item(Sheet)
                            flower.isFlower, flower.direct = 1, 2
                            flower.rect.y = block.rect.y - 30
                            flower.rect.x = block.rect.x
                            active_sprite_list.add(flower), sound_play(3)
                            block.image = pygame.image.load("images/usedBlock.jpg")
                            block.mushroom_activation, block.used = 0, 1
                    elif block.gmushroom_activation == 1:                                               #Champignon vert
                        Sheet = self.itemSheet.get_imageXY(197, 43, 212, 58)
                        gmushroom = Item(Sheet)
                        gmushroom.gmush = 1
                        gmushroom.rect.y = block.rect.y - 30
                        gmushroom.rect.x = block.rect.x
                        active_sprite_list.add(gmushroom), sound_play(3)
                        block.image = pygame.image.load("images/usedBlock.jpg")
                        block.gmushroom_activation, block.used = 0, 1
                    elif block.giveCoin == 1:                                                                     #Pièce
                        self.recharge += 1
                        Sheet = self.itemSheet.get_imageXY(69, 172, 82, 187)
                        coin = Item(Sheet)
                        coin_list.add(coin), item_list.add(coin)
                        coin.rect.y = block.rect.y - 30
                        coin.rect.x = block.rect.x
                        active_sprite_list.add(coin), sound_play(7)
                        block.image = pygame.image.load("images/usedBlock.jpg")
                        block.giveCoin, block.used = 0, 1
                self.changeY = 0

            MarioFlag_hit_list = pygame.sprite.spritecollide(self, flag_list, False)
            for flag in MarioFlag_hit_list:
                #print(flag.flag, flag.pos, flag.fin)
                if flag.fin != len(MarioFlag_hit_list):
                    self.lastCheckpoint = flag.pos
                else:
                    self.reset = 1

            MarioItem_hit_list = pygame.sprite.spritecollide(self, active_sprite_list, False)          #Collisions items
            for item in MarioItem_hit_list:
                if self.isTornado == 0:
                    if item.mush == 1:
                        item_list.remove(item)
                        active_sprite_list.remove(item)
                        sound_play(5)
                        self.upgraded = 1
                    if item.gmush == 1:
                        item_list.remove(item)
                        active_sprite_list.remove(item)
                        sound_play(6)
                        #faire gagner une vie
                    if item.isFlower == 1:
                        item_list.remove(item)
                        active_sprite_list.remove(item)
                        sound_play(5)
                        self.upgraded = 1
                        self.onFire = 1
                    if item.isShuriken == 1:
                        sound_list[12].stop()
                        item_list.remove(item)
                        active_sprite_list.remove(item)
                        shuriken_list.remove(item)

            MarioMonstres_hit_list = pygame.sprite.spritecollide(self, monstres_list, False)             #Collisions monstres
            for monstre in MarioMonstres_hit_list:
                if self.isTornado == 0:
                    if self.changeY > 0: #Si il arrive par le dessus
                        self.rect.y -= 5
                        if self.rage < 19: self.rage += 1
                        self.antiSuperposable = 1
                        sound_play(4)
                        monstres_list.remove(monstre)
                        active_sprite_list.remove(monstre)
                    else:
                        if self.rage < 16: self.rage += 3
                        else: self.rage = 19
                        if self.onFire == 1:
                            sound_play(8)
                            monstres_list.remove(monstre)
                            active_sprite_list.remove(monstre)
                            self.onFire = 0
                        else:
                            if self.upgraded == 1:
                                sound_play(8)
                                monstres_list.remove(monstre)
                                active_sprite_list.remove(monstre)
                                self.upgraded = 0
                            else:
                                self.death()
            if self.antiSuperposable == 1: self.antiSuperposable -= 1
            if self.antiSuperposable == 0: self.changeY, self.antiSuperposable = -5, 2

            if self.rect.y >= screenY:
                self.death()


    def grav(self):
        if self.isTornado == 0:
            if self.changeY == 0:  # Si il est au sol
                self.changeY = 1
            else:
                if self.changeY <= 10:  # Pour cap la vitesse maximale en tombant
                    self.changeY += 0.40
        elif self.isTornado == 1:
            self.changeY = 0

    def goLeft(self):
        super().goLeft()
        self.duckOn = 0

    def goRight(self):
        super().goRight()
        self.duckOn = 0

    def duck(self):
        if self.changeY == 0:
            self.changeX = 0
            if self.lookat == "right": self.image = self.duck_r
            elif self.lookat == "left": self.image = self.duck_l

    def stop(self):
        self.changeX = 0
        self.stand = 0

    def direction(self):
        if self.lookat == "right":  # Si il regardre à droite
            if self.changeY == 0:  #Si il est au sol
                if self.changeX == 0:  #et si il ne bouge pas
                    frame = (self.stand // 18) % len(self.stand_r)
                    self.image = self.stand_r[frame]
                    self.stand += 1
                else:  #Si il marche
                    if self.isScrolling == 1:
                        frame = (self.rect.x + self.niveauScroll // self.frameSpeed) % len(self.walk_r)
                    else:
                        frame = (self.rect.x  // self.frameSpeed) % len(self.walk_r)
                    self.image = self.walk_r[frame]
            else:  #Si il est en l'air
                if self.changeY >= 5:  #Si Mario tombe
                    self.image = self.jump_r[1]
                else:  #Si il saute
                    self.image = self.jump_r[0]
        else:  # Si il regarde à gauche
            if self.changeY == 0:  #Si il est au sol
                if self.changeX == 0:  #et si il ne bouge pas
                    frame = (self.stand // 18) % len(self.stand_l)
                    self.image = self.stand_l[frame]
                    self.stand += 1
                else:  #Si il marche
                    if self.isScrolling == 1:
                        frame = (self.rect.x + self.niveauScroll // self.frameSpeed) % len(self.walk_l)
                    else:
                        frame = (self.rect.x // self.frameSpeed) % len(self.walk_l)
                    self.image = self.walk_l[frame]
            else:  #Si il est en l'air
                if self.changeY >= 5:  #Si Mario tombe
                    self.image = self.jump_l[1]
                else:  #Si il saute
                    self.image = self.jump_l[0]

    def jump(self):
        if self.changeY == 0:
            self.rect.y -= 5
            self.changeY = -10
            sound_play(0)

    def death(self):
        self.image = self.dead
        self.deadOn = 1
        if self.lookat == "right": self.rect.x -= 4
        else: self.rect.x += 4
        self.rect.y -= 5
        self.isTornado = 1
        Sheet = SpriteImage("images/game over.png", noirFond, 0)
        gameOver = Sheet.get_imageXY(93, 111, 172, 126)
        GOrect = gameOver.get_rect()
        centerX = int((screenX / 2) - GOrect.centerx)
        centerY = int((screenY / 2) - GOrect.centery)
        screen.blit(gameOver, (centerX, centerY))
        for monstre in monstres_list:
            monstre.direct = 2
        if self.time == 210: pygame.mixer.stop(), sound_play(1)
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.reset = 1

        """#self.niveauScroll -= Flag.flag[self.lastCheckpoint].rect.x
        self.rect.x = Flag.flag[self.lastCheckpoint].rect.x
        self.rect.y = Flag.flag[self.lastCheckpoint].rect.y"""

    def scroll(self, sens):
        for x in block_list:
            x.rect.x += sens
        for x in flag_list:
            x.rect.x += sens
        for x in active_sprite_list:
            x.rect.x += sens
            x.niveauScroll += sens

class Monstres(Perso):
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
        self.speed = 1
        self.frameSpeed = 20
        self.coin = 0
        self.seen = 0
        self.direct = 1
        self.isFireBall = 0

    def direction(self):
        if self.lookat == "right":  # Si il regardre à droite
            frame = (self.stand // self.frameSpeed) % len(self.walk_r)
            self.image = self.walk_r[frame]
            self.stand += 1
        else:  # Si il regarde à gauche
            frame = (self.stand // self.frameSpeed) % len(self.walk_l)
            self.image = self.walk_l[frame]
            self.stand += 1

class Item(Perso):
    def __init__(self, image):
        super().__init__(image)
        self.speed = 1
        self.mush = 0
        self.gmush = 0
        self.coin = 0
        self.isCoin = 0
        self.isFlower = 0
        self.time = 15
        self.isFireBall = 0
        item_list.add(self)

    def grav(self):
            if self not in coin_list:
                if self.changeY == 0:  # Si il est au sol
                    self.changeY = 1
                else:
                    if self.changeY <= 10:  # Pour cap la vitesse maximale en tombant
                        self.changeY += 0.40
            else:
                if self.changeY <= 10:
                        self.changeY -= 0.35

class FireBall(Item):
    def __init__(self, image):
        super().__init__(image)
        spriteSheet = SpriteImage("images/item sheet.png", blancFond, 0)
        self.walk_r = spriteSheet.get_imageXY(69, 77, 82, 92)
        self.jump_r = self.walk_r
        self.direct = 1
        self.speed = 5
        self.time = 180
        self.isRight = 0
        self.isLeft = 0
        self.isTrigger = 0 #Pour les skills
        fireball_list.add(self)
        item_list.add(self)

    def update(self):
        self.direction()

        self.grav()

        self.rect.x += self.changeX
        #Collisions X blocs
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if block.isTraversable == 1:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                    self.direct = 0
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    self.direct = 1

        self.rect.y += self.changeY
        #Collisions Y blocs
        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if block.isTraversable == 1:
                if self.changeY > 0:
                    self.rect.bottom = block.rect.top
                    self.rect.y -= 15
                    self.changeY = -1
                    if block.deadly == 1:
                        self.death()
                elif self.changeY < 0:
                    self.rect.top = block.rect.bottom

            self.changeY = 0

        hit_list = pygame.sprite.spritecollide(self, monstres_list, False)
        for item in hit_list:
            if self.changeX > 0 or self.changeX < 0 or self.changeY > 0 or self.changeY < 0:
                active_sprite_list.remove(item)
                monstres_list.remove(item)
                fireball_list.remove(self)
                active_sprite_list.remove(self)
                item_list.remove(self)
                sound_play(4)
class Shuriken(Item):
    def __init__(self, image):
        super().__init__(image)
        Sheet = SpriteImage("images/Shuriken.png", blancFond, -1)
        self.walk_l = [(Sheet.get_imageXY(92, 172, 109, 189)), (Sheet.get_imageXY(73, 172, 89, 189)),
                       (Sheet.get_imageXY(52, 172, 69, 189)), (Sheet.get_imageXY(32, 172, 49, 189))]
        self.walk_r = [(Sheet.get_imageXY(32, 194, 49, 211)), (Sheet.get_imageXY(53, 194, 69, 211)),
                       (Sheet.get_imageXY(72, 194, 88, 211)), (Sheet.get_imageXY(92, 194, 109, 211))]
        #self.direct = 1
        #self.nodirection = 1
        self.time = 30
        self.speed = 6
        self.UpdateOn = 1
        self.isBoomerang = 0
        self.isBlade = 0
        self.isShuriken = 1
        item_list.add(self)

    def direction(self):
        if self.lookat == "right":
            if self.isScrolling == 1:
                frame = (self.rect.x + self.niveauScroll // 10) % len(self.walk_r)
            else:
                frame = (self.rect.x // 10) % len(self.walk_r)
            self.image = self.walk_r[frame]
        elif self.lookat == 'left':
            if self.isScrolling == 1:
                frame = (self.rect.x + self.niveauScroll // 10) % len(self.walk_l)
            else:
                frame = (self.rect.x // 10) % len(self.walk_l)
            self.image = self.walk_l[frame]

    def update(self):
        if self.UpdateOn == 1:
            self.direction()

            if self.isBlade == 1:
                block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
                for block in block_hit_list:
                    if block.isTraversable == 1:
                        if block.isShuriken == 0:
                            if self.changeX > 0:
                                self.rect.right, self.UpdateOn = block.rect.left, 0
                                item_list.remove(self), shuriken_list2.remove(self), sound_play(14)
                                plateforme = Sol("images/shuri.jpg", self.rect.x+3, self.rect.y)
                                plateforme.isShuriken = 1
                                block_list.add(plateforme)
                                active_sprite_list.remove(self)
                            elif self.changeX < 0:
                                self.rect.left, self.UpdateOn = block.rect.right, 0
                                item_list.remove(self), shuriken_list2.remove(self), sound_play(14)
                                plateforme = Sol("images/shuri.jpg", self.rect.x-3, self.rect.y)
                                plateforme.isShuriken = 1
                                block_list.add(plateforme)
                                active_sprite_list.remove(self)
            self.rect.x += self.changeX

            shuriken_hit_list = pygame.sprite.spritecollide(self, monstres_list, False)
            for monstre in shuriken_hit_list:
                if self.changeX > 0 or self.changeX < 0 or self.changeY > 0 or self.changeY < 0:
                    sound_play(13)
                    active_sprite_list.remove(monstre)
                    monstres_list.remove(monstre)
                    if self.isBlade == 1:
                        active_sprite_list.remove(self)
                        shuriken_list2.remove(self)
                        item_list.remove(self)


class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.changeX = 0
        self.changeY = 0
        self.mushroom_activation = 0
        self.used = 0
        self.deadly = 0
        self.giveCoin = 0
        self.isBreakable = 0
        self.isTraversable = 1
        self.gmushroom_activation = 0
        self.isShuriken = 0
        self.isFramed = 0
        self.stand = 0


class Sol(Block):
    def __init__(self, image, x, y):
        Block.__init__(self, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        spriteSheet = SpriteImage("images/item sheet.png", blancFond, 4)
        self.standFrame = [spriteSheet.get_imageXY(69, 104, 84, 119),
                               spriteSheet.get_imageXY(86, 104, 101, 119),
                               spriteSheet.get_imageXY(103, 104, 118, 119),
                               spriteSheet.get_imageXY(120, 104, 135, 119)]

    def update(self):
        if self.isFramed == 1 and self.used == 0:
            frame = (self.stand // 10) % len(self.standFrame)
            self.image = self.standFrame[frame]
            self.stand += 1

class Flag(Block):
    flag = []
    def __init__(self, image, x, y):
        Block.__init__(self, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = len(self.flag)
        self.flag.append(self)
        self.fin = 0


class Niveau():
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        self.goombaSheet = SpriteImage("images/goomba sheet.png", blancFond, 2)
        self.marioSheet = SpriteImage("images/mario sheet.png", vertFond, 1)
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
                    Block.isBreakable = 1
                    if y > 406:
                        Block.isTraversable = 0
                    block_list.add(Block)

                elif sprite == 'B':
                    Block = Sol("images/Block2.jpg", x, y)
                    block_list.add(Block)

                elif sprite == 'x':
                    xBlock = Sol("images/xBlock.jpg", x, y)
                    block_list.add(xBlock)

                elif sprite == 'X':
                    invisibleBlock = Sol("images/invisibleBlock.png", x, y)
                    invisibleBlock.isTraversable = 0
                    block_list.add(invisibleBlock)

                elif sprite == 'p':
                    pipeBlock = Sol("images/pipe_bot.png", x, y)
                    block_list.add(pipeBlock)

                elif sprite == 'P':
                    pipeBlock = Sol("images/pipe_top.png", x, y)
                    block_list.add(pipeBlock)

                elif sprite == 'i':
                    itemBlock = Sol("images/itemBlock.jpg", x, y)
                    itemBlock.mushroom_activation = 1
                    itemBlock.isFramed = 1
                    block_list.add(itemBlock)

                elif sprite == 'I':
                    gmushBlock = Sol("images/itemBlock.jpg", x, y)
                    gmushBlock.gmushroom_activation = 1
                    gmushBlock.isFramed = 1
                    block_list.add(gmushBlock)

                elif sprite == 'c':
                    coinBlock = Sol("images/itemBlock.jpg", x, y)
                    coinBlock.giveCoin = 1
                    coinBlock.isFramed = 1
                    block_list.add(coinBlock)

                elif sprite == 'l':
                    lavaBlock = Sol("images/lavaBlock.png", x, y)
                    lavaBlock.deadly = 1
                    block_list.add(lavaBlock)

                elif sprite == 'g':
                    goombaStand = self.goombaSheet.get_imageXY(1, 41, 17, 59)
                    goomba = Monstres(goombaStand)
                    goomba.rect.x = x
                    goomba.rect.y = y - 9
                    goomba.direct = 0
                    monstres_list.add(goomba)
                    active_sprite_list.add(goomba)

                elif sprite == 'm':
                    self.mario.isMario = 1
                    self.mario.rect.x = x
                    self.mario.rect.y = y
                    marioGroup.add(self.mario)
                    active_sprite_list.add(self.mario)

                elif sprite == 'f':
                    flag = Flag("images/itemBlock.jpg", x, y)
                    flag_list.add(flag)

                elif sprite == 'F':
                    flag = Flag("images/flagBlock.png", x, y)
                    flag.fin = 1
                    flag_list.add(flag)

                num_case += 1
            num_ligne += 1

    def reset(self, levelCurseurPos):
        Flag.flag = []
        flag_list.empty(), block_list.empty(), monstres_list.empty(), item_list.empty(), active_sprite_list.empty()
        shuriken_list.empty(), shuriken_list2.empty()
        levelSelectionDraw()
        screen.blit(menuCurseurImage, levelSelection_Curseur_Coord[levelCurseurPos])
        music_menu()
        jeu, levelSelectionOn, levelCurrent, generation_level = 0, 1, -1, 1
        self.mario.reset, self.mario.time = 0, 210
        return jeu, levelSelectionOn, levelCurrent, generation_level
