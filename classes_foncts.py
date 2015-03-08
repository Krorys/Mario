import pygame
from pygame.locals import *

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


def level_selection_cons():  # Fonction qui re-dessine levelselection
    screen.blit(levelselection_bg, (0, 0))
    screen.blit(levelselection_stage_1_1, (110, 100))
    screen.blit(levelselection_stage_1_2, (300, 100))
    screen.blit(levelselection_stage_1_3, (110, 300))
    screen.blit(levelselection_stage_1_4, (300, 300))


def levelSelectionDraw():  # Fonction qui re-dessine levelselection
    screen.blit(levelselection_bg, (0, 0))
    screen.blit(levelselection_stage_1_1, (110, 100))
    screen.blit(levelselection_stage_1_2, (300, 100))
    screen.blit(levelselection_stage_1_3, (110, 300))
    screen.blit(levelselection_stage_1_4, (300, 300))


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


def jeuFonct(event, mario, monstres):
    if monstres.direct == 1: #si direct = 1 le monstre va à droite
        monstres.goRight()
        #monstres.switch()
    if monstres.direct == 0: #si direct = 0 le monstre ira à gauche
        monstres.goLeft()
        #monstres.switch()
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


class SpriteImage():
    sprite_image = None

    def __init__(self, file_name, couleur, mario):
        self.sprite_image = pygame.image.load(file_name)
        self.couleur = couleur
        self.mario = mario

    def get_imageXY(self, x, y, x2, y2):
        largeur, hauteur = 1 + x2 - x, 1 + y2 - y
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(self.couleur)
        imagex2 = doubleImage(image, self.mario)
        return imagex2


class Mario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        spriteSheet = SpriteImage("images/mario sheet.png", vertFond, 1)
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

    def update(self):
        self.direction()
        if self.duckOn == 1: self.duck()
        self.grav()

        self.rect.x += self.changeX

        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeX > 0:
                self.rect.right = block.rect.left
            elif self.changeX < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.changeY

        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in block_hit_list:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                pygame.key.set_repeat(0, 0)  # Empeche de s'accrocher au mur si on maintient la touche de saut
                self.rect.top = block.rect.bottom

            self.changeY = 0

        if self.rect.y >= screenY:  # Si on tombe on meurt
            self.death()

    def grav(self):
        if self.changeY == 0:  # Si il est au sol
            self.changeY = 1
        else:
            if self.changeY <= 10:  # Pour cap la vitesse maximale en tombant
                self.changeY += 0.35

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
                    frame = (self.stand // 18) % len(self.stand_r)
                    self.image = self.stand_r[frame]
                    self.stand += 1
                else:  #Si il marche
                    frame = (self.rect.x // 30) % len(self.walk_r)
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
            # volume_default = pygame.mixer.Sound.get_volume(menu_music)
            #jump_sound_play(volume_default)

    def death(self):
        self.image = self.dead
        gameOverSprite = SpriteImage("images/game over.png", noirFond, 0)
        gameOver = gameOverSprite.get_imageXY(93, 111, 172, 126)
        GOrect = gameOver.get_rect()
        centerX = int((screenX / 2) - GOrect.centerx)
        centerY = int((screenY / 2) - GOrect.centery)
        volume_default = pygame.mixer.Sound.get_volume(menu_music)
        screen.blit(gameOver, (centerX, centerY))
        if self.time == 210: death_sound_play(volume_default)
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.reset = 1

    def kill(self, monster):
        pass


class Monstres(Mario):
    def __init__(self, image):
        super().__init__(image)
        spriteSheet = SpriteImage("images/goomba sheet.png", blancFond, 1)
        self.walk_r = [spriteSheet.get_imageXY(1, 41, 17, 60),
                       spriteSheet.get_imageXY(41, 41, 58, 59),
                       spriteSheet.get_imageXY(80, 42, 99, 59),
                       spriteSheet.get_imageXY(121, 41, 138, 59)]
        self.walkHold_r = [spriteSheet.get_imageXY(72, 69, 88, 95),
                           spriteSheet.get_imageXY(103, 68, 120, 94),
                           spriteSheet.get_imageXY(136, 69, 152, 95),
                           spriteSheet.get_imageXY(168, 69, 184, 95)]
        self.jump_r = [spriteSheet.get_imageXY(1, 41, 17, 60),
                       spriteSheet.get_imageXY(1, 41, 17, 60)]
        #self.walk_l = [pygame.transform.flip(x, True, False) for x in self.walk_r]
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.lookat = "right"
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.timetime = 0
        self.test = self.rect.x
        self.direct = 1

    def goRight(self):
        self.changeX = 1
        self.lookat = "right"
        self.duckOn = 0

    def goLeft(self):
        self.changeX = -3
        self.lookat = "left"
        self.duckOn = 0

    def switch(self): #Fonction sensée faire changer de direction (via direct) le goomba lors d'une collision mais ça marche pas
        if pygame.sprite.collide_rect(monstres, block_list) and self.lookat == "right":
            self.direct = 0
            print("a")
        if pygame.sprite.collide_rect(monstres, block_list) and self.lookat == "left":
            self.direct = 1
            print("b")





    def death(self):
        pass



class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.changeX = 0
        self.changeY = 0


class Sol(Block):
    def __init__(self, image, x, y):
        Block.__init__(self, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

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


    def afficher(self, screen):
        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite

                if sprite == 'b':
                    mur = Sol("images/bloc.jpg", x, y)
                    block_list.add(mur)

                elif sprite == 'm':
                    mush = Sol("images/mushroom.jpg", x, y)
                    block_list.add(mush)
                elif sprite == 'f':
                    flag = Sol("images/flag.jpg", x, y)
                    block_list.add(flag)

                num_case += 1
            num_ligne += 1