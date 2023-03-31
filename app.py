# © 2019 - 2020 IAZZ - SAIDOUN Ferhat (Github : ferhatte10) 

#  -*- coding: utf-8 -*-
import json
from os import name

from ui.user_entries import *
from ui.play_display import clear_screen, printc
from life_cycle.play import *
from life_cycle.cycle_game import *
from game.options import *
from game.scores import *
from game.admin_console import *
from ext_res.getkey import *
from game.statistics import *

# QUESTION 3.8 :
def threes():
    # game initialisation
    clear_screen()
    game = None
    # showMenu define if we show the menu or not
    showMenu = True

    while 1:

        if showMenu:
            # à Chaque tour d'affichage de menu, on demanande le choix de l'utilisateur 
            user_choice = get_user_menu()

            if user_choice == "CONSOLE":
                console()

            # On créer une partie et on n'affichera pas le menu au prochain tour
            if user_choice == "N":
                game = create_new_play()
                if game is not None:
                    showMenu = False

            # On resrtorre une partie, si la partie retournée est !=0, n'affichera pas le menu au prochain tour
            elif user_choice == "L":
                result = restore_game()
                if result != 0:
                    game = result
                    showMenu = False

                    # On lance lance la fonction de sauvegarde de parrtie (celle en cours)
            elif user_choice == "E":
                save_game(game)

            # On fais rien pour continuer la partie
            elif user_choice == "C":
                if game is None:
                    printc(("Aucune partie commencée, chargez-en une ou commencez-en une nouvelle").upper())
                else:
                    showMenu = False
            # On lance lance la fonction d'affichage des scores
            elif user_choice == "T":
                choose_score()

            # On lance lance la fonction de statistiques
            elif user_choice == "P":
                statistics()

            # On lance lance la fonction d'aide du jeu
            elif user_choice == "J":
                how_play()

            # On lance lance la fonction des options
            elif user_choice == "O":
                options()

            # Pour quitter
            elif user_choice == "F":
                # On demande à l'utilisateur son choix
                user_input = get_user_custom(["E", "F", "R"],
                                             "Quitter\n(E) Enregistrer et Fermer\n(F) Fermer sans Sauvegarder\n\n(R) Retour",
                                             " -> ")

                # Si "save and quit" : On saugegarde la partie en cours et on quit python avec (exit)
                if user_input == "E":
                    save_game(game)
                    leave(game)

                # Si "quitter" : on quitte python avec exit()
                elif user_input == "F":
                    leave(game)
                # si "retour" : on fait rien  pour que le programme reviennene au menu
        else:
            # cycle_play peut renvoyer :
            # False pour afficher le menu : On met à true la variable showMenu
            # "fin" quand la partie est finie : on remet à None la partie (Pour pas qu'elle puisse être continuée) et met à true la variable showMenu
            # Si la fonction renvoie une partie, la variable partie prend le return de cycle_play ( donc une partie)
            tmpGame = cycle_play(game)
            if not tmpGame:
                showMenu = True
            elif tmpGame:
                game = None
                showMenu = True
            else:
                game = tmpGame


threes()

