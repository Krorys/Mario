__author__ = 'Chèvre'

taille_sprite = 29 # A METTRE DANS CONST (TAILLE DES SPRITES DU DECOR)


niveau = Niveau(choix) # A METTRE DANS LE MAIN (APPLICATION DE LA CLASS DE CREATION DE NIVEAU)
            niveau.generer()
            niveau.afficher(screen)

class Niveau: # A METTRE DANS CLASSES_FONCTS
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0


	def generer(self):
		with open("n1.txt", "r") as fichier:
			structure_niveau = []
			for ligne in fichier:
				ligne_niveau = []
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau


	def afficher(self, screen):
		"""Méthode permettant d'afficher le niveau en fonction
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
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
				if sprite == 'b':		   #m = Mur
					screen.blit(bloc, (x,y))
				elif sprite == 'm':		   #d = Départ
					screen.blit(mushroom, (x,y))
				elif sprite == 'f':		   #a = Arrivée
					screen.blit(flag, (x,y))
				num_case += 1
			num_ligne += 1
