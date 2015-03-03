__author__ = 'Chèvre'

taille_sprite = 29 # A METTRE DANS CONST (TAILLE DES SPRITES DU DECOR)


niveau = Niveau(choix) # A METTRE DANS LE MAIN (APPLICATION DE LA CLASS DE CREATION DE NIVEAU)
            niveau.generer()
            niveau.afficher(screen)