# -*- coding: utf-8 -*-
import sys
from os import path, system, name
import json

sys.path.append(path.abspath('../'))
from ext_res.termcolor import colored, cprint


# QUESTION 1.10.1 :
def simple_display(board):
    """
    Affichage simple : affiche seulement les valeurs des tuiles du plateau passé en paramètres (plateau)
    """
    line = ""
    i = 0
    while i < len(board["tiles"]):
        if i % board["n"] == 0:
            print(line)
            line = ""
        line += str(board["tiles"][i]).center(5)
        i += 1
    print(line)


# QUESTION 1.10.2 :
def medium_display(board):
    """
    Affichage moyen : affiche les valeurs des tuiles du plateau passé en paramètres (plateau) avec des borbures de séparation
    """

    # On défini la longueur de la ligne de sépartation
    borderLine = "*" + "*" * 6 * board["n"]

    # On défini une variable vide pour l'incrémenter la variable avec les valeurs et les étoiles
    line = "*"

    print(borderLine)

    # On parcours toutes les valeur du tableau
    for i in range(len(board["tiles"])):

        # Si on arrrive à la fin de la ligne, on affiche la ligne avec les valeur ainsi qu'une ligne de séparation
        if i % board["n"] == 0 and i != 0:
            print(line + "\n" + borderLine)
            line = "*"
        # On ajoute la valeur et une étoile à la ligne
        line += str(board["tiles"][i]).center(5) + ("*")

    # Une fois fini, on affiche la dernère ligne enregistrée et une ligne de séparation
    print(line + "\n" + borderLine)


# QUESTION 1.10.3 :
def full_display(board):
    """
    Affichage complet : affiche les valeurs des tuiles du plateau passé en paramètres (plateau) avec des borbures de séparation et colore les cellules :
    - bleu pour les 1, 
    - rouge pour les 2,
    - blanc pour le reste

    ATTENTION : L'affiche coloré peut ne pas fonctionner sur certains terminaux
    """

    # On défini la couleur des bordures
    file = open("game/options.json", "r")
    parameters = json.load(file)
    colorTxt = parameters["bordercolor"][0]
    colorBackgorund = parameters["bordercolor"][1]
    file.close()

    cell_size = 7

    # même chose que le medium_display mais en mettant une couleur. Syntaxe (module termcolor):
    # color(texte, couleur_texte, couleur_fond)
    lineEtoiles = colored("*" + "*" * (cell_size + 1) * board["n"], colorTxt, colorBackgorund)

    # Lignes qui composent les cellules
    line = colored("*", colorTxt, colorBackgorund)
    emptyLine = colored("*", colorTxt, colorBackgorund)

    # Affichage de la première bordure
    print(lineEtoiles)
    i = 0
    while i < len(board["tiles"]):

        # Si on atteint la fin de la ligne, on imprime la ligne et on la reset
        if i % board["n"] == 0 and i != 0:
            print(emptyLine + "\n" + emptyLine + "\n" + line + "\n" + emptyLine + "\n" + emptyLine + "\n" + lineEtoiles)


            # Reset des lignes
            line = colored("*", colorTxt, colorBackgorund)
            emptyLine = colored("*", colorTxt, colorBackgorund)

        # On choisi la couleur de la cellule en fonction de la valeur :
        val = board["tiles"][i]

        colors = [["white", "on_white"], ["white", "on_blue"], ["white", "on_red"], ["grey", "on_white"]]
        indiceColor = val

        # Si la valeur de la cellule est > 3, elle prend la même couleur que celle de la valeur 3
        if val > 3:
            indiceColor = 3

        line += (colored(str(val).center(cell_size), colors[indiceColor][0], colors[indiceColor][1]) + colored("*",
                                                                                                              colorTxt,
                                                                                                              colorBackgorund))
        emptyLine += colored("".center(cell_size), colors[indiceColor][0], colors[indiceColor][1]) + colored("*",
                                                                                                             colorTxt,
                                                                                                             colorBackgorund)
        i += 1

        # On affiche la dernière ligne enregistrée
    print(emptyLine + "\n" + emptyLine + "\n" + line + "\n" + emptyLine + "\n" + emptyLine + "\n" + lineEtoiles)


# QUESTION BONUS :
def clear_screen():
    # Pour windows
    if name == "nt":
        system("cls")

        # Pour mac et Linux
    else:
        system("clear")


def printc(string):
    import shutil

    columns = shutil.get_terminal_size().columns
    lines = string.split("\n")

    for i in range(len(lines)):
        print(lines[i].center(columns))
