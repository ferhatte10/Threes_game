# -*- coding: utf-8 -*-
import sys
from os import path
# from termcolor import colored, cprint
import time

sys.path.append(path.abspath('../../'))
from ext_res.termcolor import *
from ui.play_display import clear_screen

# On défini les lettres, les chiffres, espace, ? et !
caracters = {
    "a": [[" *** "], ["*   *"], ["*****"], ["*   *"], ["*   *"]],
    "b": [["**** "], ["*   *"], ["**** "], ["*   *"], ["**** "]],
    "c": [["*****"], ["*    "], ["*    "], ["*    "], ["*****"]],
    "d": [["**** "], ["*   *"], ["*   *"], ["*   *"], ["**** "]],
    "e": [["*****"], ["*    "], ["***  "], ["*    "], ["*****"]],
    "f": [["*****"], ["*    "], ["***  "], ["*    "], ["*    "]],
    "g": [["*****"], ["*    "], ["* ***"], ["*   *"], ["*****"]],
    "h": [["*   *"], ["*   *"], ["*****"], ["*   *"], ["*   *"]],
    "i": [["*****"], ["  *  "], ["  *  "], ["  *  "], ["*****"]],
    "j": [["*****"], ["   * "], ["   * "], ["*  * "], ["**** "]],
    "k": [["*   *"], ["** * "], ["***  "], ["*  * "], ["*   *"]],
    "l": [["*    "], ["*    "], ["*    "], ["*    "], ["*****"]],
    "m": [["*   *"], ["** **"], ["* * *"], ["*   *"], ["*   *"]],
    "n": [["*   *"], ["**  *"], ["* * *"], ["*  **"], ["*   *"]],
    "o": [["*****"], ["*   *"], ["*   *"], ["*   *"], ["*****"]],
    "p": [["*****"], ["*   *"], ["*****"], ["*    "], ["*    "]],
    "q": [["*****"], ["*   *"], ["*   *"], ["*  * "], ["*** *"]],
    "r": [["*****"], ["*   *"], ["*****"], ["*  * "], ["*   *"]],
    "s": [[" ****"], ["*    "], [" *** "], ["    *"], ["**** "]],
    "t": [["*****"], ["  *  "], ["  *  "], ["  *  "], ["  *  "]],
    "u": [["*   *"], ["*   *"], ["*   *"], ["*   *"], ["*****"]],
    "v": [["*   *"], ["*   *"], ["*   *"], [" * * "], ["  *  "]],
    "w": [["*   *"], ["*   *"], ["* * *"], ["** **"], ["*   *"]],
    "x": [["*   *"], [" * * "], ["  *  "], [" * * "], ["*   *"]],
    "y": [["*   *"], [" * * "], ["  *  "], ["  *  "], ["  *  "]],
    "z": [["*****"], ["   * "], ["  *  "], [" *   "], ["*****"]],
    "1": [["  *  "], [" **  "], ["  *  "], ["  *  "], ["  *  "]],
    "2": [[" *** "], ["*   *"], ["  ** "], [" *   "], ["*****"]],
    "3": [[" *** "], ["*   *"], ["  ** "], ["*   *"], [" *** "]],
    "4": [["  ** "], [" * * "], ["*  * "], ["*****"], ["   * "]],
    "5": [["*****"], ["*    "], ["**** "], ["    *"], ["**** "]],
    "6": [[" *** "], ["*    "], ["**** "], ["*   *"], [" *** "]],
    "7": [["*****"], ["    *"], ["   * "], ["  *  "], ["  *  "]],
    "8": [[" *** "], ["*   *"], [" *** "], ["*   *"], [" *** "]],
    "9": [[" *** "], ["*   *"], [" ****"], ["    *"], [" *** "]],
    "0": [[" *** "], ["*   *"], ["*   *"], ["*   *"], [" *** "]],
    " ": [["     "], ["     "], ["     "], ["     "], ["     "]],
    "!": [["  *  "], ["  *  "], ["  *  "], ["     "], ["  *  "]],
    "?": [[" **  "], ["   * "], ["  *  "], ["     "], ["  *  "]],
    ">": [[" *   "], ["  *  "], ["   * "], ["  *  "], [" *   "]],

}


def makeTall(phrase, txtColor=None, bgColor=None):
    """
    Fonction qui affiche en caracteres de 5*5 une phrase passées passée en paramètre (phrase)
    en couleur (txtColor) et une couleur de fond (bgColor)
    """

    line = ""

    # On défini l'étoile qui va composer les lettres
    etoile = colored("*", txtColor, "on_" + txtColor)

    # Si la couleur de fond est vide, on créer un caractère vide, sinon on lui applique la couleur passée en paramètre
    if bgColor is None:
        vide = " "
    else:
        vide = colored(" ", bgColor, "on_" + bgColor)

    # Fonctionnement : On parcours le premier tableau de chaque lettre, ensuite on va à la linge et on parcours
    # le deuxieme tableau de chaque lettre etc jusqu'au dernier tableau (5 au total)
    # On parcours les 5 tableaux qui composent chaque lettre.
    # La compléxité est de O(n^3), mais comme les messages affichés sont pas très grand (quelques caractères), aucun problème de temps d'execusion
    for i in range(5):

        # On parcours chaque lettre de la phrase en paramètre
        for j in range(len(phrase)):

            # Variable qui correspond au premier caractère de chaque tableau qui compose le grand tableau de chaque lettre
            demiline = caracters[phrase[j].lower()][i][0]

            # On parcours le tableau, si c'est une etoile, on ajoute le caractère etoile, sinon le caractere vide (pour pouvoir appliquer la couleur)
            for k in range(len(demiline)):
                if demiline[k] == "*":
                    line += etoile
                else:
                    line += vide

            # On ajoute un carcatère vide en fin de chaque ligne pour faire des espaces entre chaque lettre
            line += vide

        # A la fin de chaque ligne, on va à la ligne
        line += "\n"

    # On retourne "line" moins les deux derners caracteres pour enlever le dernier "\n"
    return line.rstrip()


def tallchars(phrase, colors, bgColor=None, clignCd=1, clignRepeats=1):
    """
    Fonction qui permet de faire clignoter un texte ecrit en grand (lettres en 5*5)
    """
    # On créers une variable vide qui va contenir la phrase écrite avec toutes les couleurs
    textes = []

    # On parcours chaque couleur du tableau, et on ajoute le texte coloré au tableau textes
    for i in range(len(colors)):
        textes.append(makeTall(phrase, colors[i], bgColor))

    # Pour le nombre de répétition passé en paramètre:
    for j in range(clignRepeats):

        # On parcours le tableau des textes, on affiche le texte, on attend x secondes (paramétre passé en paramètre) et on efface l'ecran
        for k in range(len(textes)):
            print(textes[k])
            time.sleep(clignCd)
            clear_screen()
