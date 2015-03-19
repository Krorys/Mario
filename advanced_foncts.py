from classes import *

def boucle_jeu(levelCurrent):
    screen.blit(bg_list[levelCurrent], (0, 0))
    block_list.update()
    block_list.draw(screen)
    flag_list.draw(screen)
    active_sprite_list.draw(screen)
    nomarioMovement(monstres_list, item_list)
    itemDisparition()
    active_sprite_list.update()

def mort(niveau, levelCurrent):
    screen.blit(bg_list[levelCurrent], (0, 0))
    block_list.draw(screen)
    flag_list.draw(screen)
    active_sprite_list.draw(screen)
    niveau.mario.death()

def generation(choix, levelCurrent):
    pygame.key.set_repeat(0, 0)
    music_levels(levelCurrent)
    niveau = Niveau(choix)
    niveau.generer()
    niveau.afficher()
    return niveau
