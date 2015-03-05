import pygame
from pygame.locals import *
from const import *

def music_levels(levelCurrent):
    pygame.mixer.stop()
    levels_music[levelCurrent].set_volume(volume_default)
    levels_music[levelCurrent].play()

def music_menu():
    pygame.mixer.stop()
    menu_music.set_volume(volume_default)
    menu_music.play()

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
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    mario.lookat = "right"
        if event.key == K_LEFT:
            mario.changeX = -5
            if mario.lookat == "right":
                mario.image = pygame.transform.flip(mario.image, True, False)
                mario.lookat = "left"
        if event.key == K_UP or event.key == K_SPACE:
                mario.jump()
    if event.type == KEYUP:
        if event.key == K_RIGHT:
            mario.changeX = 0
        if event.key == K_LEFT:
            mario.changeX = -0

def niveauFonct(niveau, choix, screen, fonct):
    if fonct == 0:
        niveau.generer()
    else:
        screen.blit(bg, (0,0))
        niveau.afficher(screen)

class SpriteImage():
    sprite_image = None

    def __init__(self, file_name):
        self.sprite_image = pygame.image.load(file_name)

    def get_image(self, x, y, largeur, hauteur):
        image = pygame.Surface([largeur, hauteur])
        image.blit(self.sprite_image, (0, 0), (x, y, largeur, hauteur))
        image.set_colorkey(orange)
        return image

class Mario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.changeX = 0
        self.changeY = 0
        self.image = image
        self.lookat = "right"
        self.rect = self.image.get_rect()
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
                self.rect.top = block.rect.bottom

            self.changeY = 0

    def grav(self):
        if self.changeY == 0:
            self.changeY = 1
        else:
            self.changeY += 0.35

    def jump(self):
        if len(block_list) == 0 or self.changeY == 0:
            self.rect.y -= 5
            self.changeY = -10

    def death(self):
        pass

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
