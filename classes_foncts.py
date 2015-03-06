import pygame
from pygame.locals import *
from const import *

<<<<<<< HEAD

def affichage_volume(volume):
    if volume > -1 and volume < 11:
        screen.blit(volume_images[volume], (210,250))

"""def volume_down(volume_default):
    if volume_default > 0.05 and volume_default < 1.05:
        volume_default -= 0.1"""


=======
>>>>>>> origin/master
def music_levels(levelCurrent, volume_default):
    pygame.mixer.stop()
    print(volume_default)
    levels_music[levelCurrent].set_volume(volume_default)
    levels_music[levelCurrent].play()

def music_menu(volume_default):
    pygame.mixer.stop()
    menu_music.set_volume(volume_default)
    menu_music.play()

<<<<<<< HEAD
def jump_sound_play(volume_default):
    jump_sound.set_volume(volume_default)
    jump_sound.play()
=======
"""def jump_sound_play(volume_default):
    pygame.mixer.pause()
    jump_sound.set_volume(volume_default)
    jump_sound.play()
    pygame.mixer.unpause"""
>>>>>>> origin/master

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
    if mario: imagex2 = pygame.transform.scale(image, (28, 50))
    else: imagex2 = pygame.transform.scale2x(image) #Double la taille du Mario
    return imagex2

def choixMenu(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_DOWN and pos < 2: #On peut descendre qu'en étant en haut
            pos += 1
        if event.key == K_UP and pos > 0: #Et inversement
            pos -= 1
    return pos

def menuTo(pos):
    valeurs = [0, 0, 1]
    valeurs[pos] = abs(valeurs[pos]-1) #si c'est à 0 -> 1, si c'est à 1->0
    return valeurs #[levelSelection, optionsOn, continuer]

def choixLevel(event, pos):
    if event.type == KEYDOWN:
        if event.key == K_DOWN and pos < 3:
            pos = (pos+2)%4
        if event.key == K_UP and pos > 0:
            pos = (pos-2)%4
        if event.key == K_LEFT:
            pos = (pos-1)%4
        if event.key == K_RIGHT:
            pos = (pos+1)%4
    return pos

def jeuFonct(event, mario):
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            mario.changeX = 5
            if mario.lookat == "left":
                mario.lookat = "right"
        if event.key == K_LEFT:
            mario.changeX = -5
            if mario.lookat == "right":
                mario.lookat = "left"
        if event.key == K_UP or event.key == K_SPACE:
                mario.jump()
    if event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            mario.changeX = 0

def niveauFonct(niveau, choix, screen, fonct):
    if fonct == 0:
        niveau.generer()
    else:
        screen.blit(bg, (0,0))
        niveau.afficher(screen)

class SpriteImage():
    sprite_image = None

    def __init__(self, file_name, couleur, mario):
        self.sprite_image = pygame.image.load(file_name)
        self.couleur = couleur
        self.mario = mario

    def get_imageXY(self, x, y, x2, y2):
        largeur, hauteur = 1+x2-x, 1+y2-y
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(self.couleur)
        imagex2 = doubleImage(image, self.mario)
        return imagex2

class Mario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.sprite = SpriteImage("images/mario sheet.png", vertFond, 1)
        self.standright = self.sprite.get_imageXY(72, 5, 87, 31)
        self.standleft = pygame.transform.flip(self.standright, True, False)
        self.jumpright = self.sprite.get_imageXY(72, 99, 89, 126)
        self.jumpleft = pygame.transform.flip(self.jumpright, True, False)
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.lookat = "right"
        self.rect = self.image.get_rect()
        self.reset = 0
<<<<<<< HEAD
        self.time = 210
=======
        self.time = 180
>>>>>>> origin/master
        self.hp = 3

    def update(self):
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
                pygame.key.set_repeat(0, 0)
                self.rect.top = block.rect.bottom

            self.changeY = 0

        if self.rect.y >= 435: #Si on tombe on meurt
            gameOverSprite = SpriteImage("images/game over.png", noirFond, 0)
            gameOver = gameOverSprite.get_imageXY(93, 111, 172, 126)
            GOrect = gameOver.get_rect()
            centerX = int((screenX/2)-GOrect.centerx)
            centerY = int((screenY/2)-GOrect.centery)
            volume_default = pygame.mixer.Sound.get_volume(menu_music)
<<<<<<< HEAD
            if self.time == 210: death_sound_play(volume_default)
=======
            if self.time == 180: death_sound_play(volume_default)
>>>>>>> origin/master
            screen.blit(gameOver, (centerX, centerY))
            if self.time > 0: self.time -= 1
            else: self.reset = 1

    def grav(self):
        if self.changeY == 0:
            if self.lookat == "right": self.image = self.standright
            else: self.image = self.standleft
            self.changeY = 1
        else:
            if self.lookat == "right": self.image = self.jumpright
            else: self.image = self.jumpleft
            self.changeY += 0.35

    def jump(self):
        if len(block_list) == 0 or self.changeY == 0:
            self.rect.y -= 5
            self.changeY = -10
            #volume_default = pygame.mixer.Sound.get_volume(menu_music)
            #jump_sound_play(volume_default)

    def death(self):
        if self.rect.y >= 435:
            self.rect.y = 200

    def kill(self, monster):
        pass

class Monstres(Mario):
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
                    screen.blit(mushroom, (x, y))
                elif sprite == 'f':
                    screen.blit(flag, (x, y))

                num_case += 1
            num_ligne += 1
