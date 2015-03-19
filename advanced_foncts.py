from classes import *

def shurikenblit():
    if len(shuriken_list) == 0:
                screen.blit(shuri_ghost_on, (0, 0))
    else:
                screen.blit(shuri_ghost_off, (0, 0))
    screen.blit(shuri_ghost_off, (49, 0))

    for x in active_sprite_list:
        if x.isMario == 1:
            screen.blit(shuri_list[x.recharge], (49, 0))
def boucle_jeu(levelCurrent):
    screen.blit(bg_list[levelCurrent], (0, 0))
    shurikenblit()
    block_list.update()
    active_sprite_list.draw(screen)
    block_list.draw(screen)
    flag_list.draw(screen)
    nomarioMovement(monstres_list, item_list)
    itemDisparition()
    shuriken()
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
