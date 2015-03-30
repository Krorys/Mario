from classes import *

def itemBlit():
    #Ghost Razorblade
    if len(shuriken_list) == 0: screen.blit(shuri_ghost_on, (0, 0))
    else: screen.blit(item_off, (0, 0))

    #Razorblade
    screen.blit(item_off, (49, 0))
    for x in active_sprite_list:
        if x.isMario == 1:
            screen.blit(pygame.image.load("images/shuri_on.png"), (49, 0))
            text = font.render(str(x.recharge), True, (0,0,0))
            screen.blit(text, (49+40, 38))

    #Rage
    for x in active_sprite_list:
        if x.isMario == 1:
            if x.rage < 10: screen.blit(rage_bar_off, (98, 0))
            else: screen.blit(rage_bar_on, (98, 0))
            for y in range (0, x.rage):
                coordX = 98 + 7 * y
                coordY = 0
                screen.blit(volume_redsquare, (coordX, coordY))

def boucle_jeu(levelCurrent, niveau):
    screen.blit(bg_list[levelCurrent], (0, 0))
    itemBlit()
    block_list.update()
    active_sprite_list.draw(screen)
    block_list.draw(screen)
    flag_list.draw(screen)
    nomarioMovement(monstres_list, item_list, niveau.mario)
    itemUpdate(SpriteImage, FireBall, niveau.mario)
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
