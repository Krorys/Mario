import pygame, sys
from pygame.locals import *
from const import *


def level_selection_cons():  # Fonction qui re-dessine levelselection
    screen.blit(levelselection_bg, (0, 0))
    screen.blit(levelselection_stage_1_1, (110, 100))
    screen.blit(levelselection_stage_1_2, (300, 100))
    screen.blit(levelselection_stage_1_3, (110, 300))
    screen.blit(levelselection_stage_1_4, (300, 300))


def level1_cons():
    screen.blit(bg, (0, 0))


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
    def __init__(self, sprite):
        self.x = 100
        self.y = 100
        self.changeX = 0
        self.changeY = 3
        #self.sprite = pygame.image.load(sprite).convert()
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.hp = 3
        super().__init__()

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
        screen.blit(self.sprite, (self.x, self.y))

    def move(self):
        self.x += self.changeX
        if self.rect.collidelist(sols):
            self.y += self.changeY

    def jump(self):
        pass

    def death(self):
        pass

    def kill(self, monster):
        pass


class Monstres(Mario):
    pass

class Block(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.x = 0
        self.y = 0
        self.changeX = 0
        self.changeY = 0
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
        sols.append(self.rect)
    def draw(self):
        self.update()
        screen.blit(self.sprite, (self.x, self.y))


class Sol(Block):
    def __init__(self, sprite):
        Block.__init__(self, sprite)
        #sol_list.add(self)

bloc1 = Sol("bloc.jpg")
bloc1.x = 100
bloc1.y = 250

class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0


    def generer(self):
        with open("n1.txt", "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    # On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                # On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            # On sauvegarde cette structure
            self.structure = structure_niveau


    def afficher(self, screen):
        """Méthode permettant d'afficher le niveau en fonction
		de la liste de structure renvoyée par generer()"""
        # Chargement des images (seule celle d'arrivée contient de la transparence)
        bloc = pygame.image.load("bloc.jpg")
        mushroom = pygame.image.load("mushroom.jpg")
        flag = pygame.image.load("flag.jpg")

        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'b':  #m = Mur
                    #screen.blit(bloc, (x, y))
                    mur = Sol("bloc.jpg")
                    mur.x = x
                    mur.y = y
                    mur.draw()
                elif sprite == 'm':  #d = Départ
                    screen.blit(mushroom, (x, y))
                elif sprite == 'f':  #a = Arrivée
                    screen.blit(flag, (x, y))
                num_case += 1
            num_ligne += 1
