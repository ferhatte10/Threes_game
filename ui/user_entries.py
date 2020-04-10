# -*- coding: utf-8 -*-
import sys
from os import path
from ui.play_display import clear_screen
import json

sys.path.append("../")
from ext_res.getkey import getkey
from ext_res.coloredMenu import *


def get_fast_mode():
    """
    Retourne True si le mode rapide est activé, false sinon
    """
    return json.load(open("game/options.json", "r"))["fast_mode"]


# QUESTION 3.2
def get_user_move():
    """
    Saisie controlée et renvoie en minuscule le mouvement du joueur

    """
    # On récupère le mode de jeu
    fast_mode_option = get_fast_mode()

    values = ["CONSOLE", "H", "B", "G", "D", "M"]
    menu = "/!\\ Fast mode désactivez : dépalcez-vous uniquement avec h/b/g/d. \"m\" pour afficher le menu :"

    menuFast = "Dépalcez-vous avec h/b/g/d, z/q/s/d ou ←/↑/↓/→. \"m\" ou ECHAP pour afficher le menu :"

    # Check si fast_mode est activé
    if not fast_mode_option:
        # Saisie controllee
        user_move = ""
        while user_move not in values:
            user_move = input(menu + "\n").upper()
        clear_screen()
        return user_move.lower()

    else:
        print(menuFast)
        user_move = ""

        while user_move not in values:
            user_move = getkey().upper()
        if user_move != "CONSOLE":
            clear_screen()
        return user_move.lower()


# QUESTION 3.5
def get_user_menu():
    """
    Saisie controlée pour naviguer dans le menu principal
    """
    # On récupère le mode de jeu
    fast_mode_option = get_fast_mode()

    values = ["CONSOLE", "J", "N", "L", "E", "C", "P", "T", "O", "F"]
    phrase = ("Menu Principal\n"
              "(N) Nouvelle partie\n"
              "(L) Charger partie\n"
              "(E) Enregistrer partie\n"
              "(C) Continuer partie\n"
              "\n"
              "(T) Tableau des scores\n"
              "(P) Statistiques\n"
              "(J) Comment jouer \n"
              "(O) Options\n"
              "\n"
              "(F) Fermer")

    if not fast_mode_option:
        user_move = ""
        while user_move not in values:
            user_move = input(phrase + "\n").upper()
        clear_screen()
        return user_move.upper()

    else:
        return coloredMenu(phrase.split("\n"), values, " -> ")


# QUESTION BONUS 3
def get_user_custom(values, phrase, indic="", indice=1, beforeMessage=None):
    """
    Affiche un menu avec sausie controllées :
    values : tableau - valeurs possible pour saisie controlee
    phrase : Phrase affichée
    EN MODE RAPIDE :
    phrase : Lignes affichées à l'écran, séparées par un "\\ n"
    indic : indicateur qui montrera la ligne active ("->" par exemple)
    indice : indice du caractere de la ligne qui sera retourné, exemple : si indice 1 et ligne "(F) Fermer", 
    il sera retourné "F" si la ligne a été choissie car ligne[1] = "F""  
    beforeMessage : Si besoin, message affiché en haut du menu
    """

    # A noter que pour les fonctions, il aurait été possible d'utiliser seulement celle-la,
    # mais pour respecter le sujet, nous avons écris 4 presques identiques
    # On récupère le mode de jeu
    fast_mode_option = get_fast_mode()

    if not fast_mode_option:
        user_move = ""
        while user_move.upper() not in values:
            if beforeMessage is not None:
                print(beforeMessage)
            user_move = input(phrase + "\n").upper()
        clear_screen()
        return user_move.upper()

    else:
        aDel = coloredMenu(phrase.split("\n"), values, indic, indice, beforeMessage).upper()
        return aDel
