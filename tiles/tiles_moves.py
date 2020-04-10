# -*- coding: utf-8 -*-
from random import *
import sys
from os import path, name

sys.path.append('../')
from tiles.tiles_acces import *
from game.statistics import *
from ext_res.secrets import * 
from game.options import isSound

if name == "nt":
    import winsound


# QUESTION 1.7 :
def get_nb_empty_rooms(board):
    """
    Retourne le nombre de cellules vide d'un board passé en paramètres (board) et met à jour le tableau
    """
    # On renvoie le nombre de zero dans board["tiles"]
    return board["tiles"].count(0)


# QUESTION 2.1 :
def get_next_alea_tiles(board, mode):
    """
    Tire une ou deux tuiles de valeur et position aléatoires en fonction du mode passé en paramètre (mode) et la/les retourne(s)
    """
    


    # Tirage de 2 tuiles en initialisation de jeu
    if mode == "init":

        # Correspond à n (pour la prise en charge des tailles)
        nBoard = board["n"] - 1

        # tile0 et tile1 sous la forme [ligne, colonne]
        tile0 = [randint(0, nBoard), randint(0, nBoard)]

        tile1 = tile0
        # Pour eviter que tile 0 et tile 1 soient sur la meme tile, on retire tile1 tant que tile0 = tile1
        while tile1 == tile0:
            tile1 = [randint(0, nBoard), randint(0, nBoard)]

        # On renvoie la tuile0 sous forme tuile0[0] (pour la ligne) et tuile0[1] (pour la colonne)
        tiles = {"mode": "init",
                 "0": {"val": 1, "lig": tile0[0], "col": tile0[1]},
                 "1": {"val": 2, "lig": tile1[0], "col": tile1[1]},
                 "check": True
                 }

        new_tiles(tiles)

    # Tirage d'une tuile quand le jeu est en cours
    else:
        # Si il y à aucune cellule libre on retourne une tuile aléatoire dont seul là valeur sera conservée
        if get_nb_empty_rooms(board) == 0:  
            return {"mode": "progress",
                    "0": {"val": randbelow(2)+1, "lig": 0, "col": 0},
                    "check": True
                    }

            # On tire un nombre aléatoire entre 1 et le nombre de zéro.
        aleaEmpty = randint(1, get_nb_empty_rooms(board))

        # On compte l'indice (variable i) du zéro qui sera remplacé
        i = 0
        while aleaEmpty != 0:
            if board["tiles"][i] == 0:
                aleaEmpty -= 1
            i += 1
        i -= 1

        # Définition de la valeur max en foncion de la taille du plateau
        maxVal = {0:1, 1: 2, 2: 3, 3: 3, 4: 3, 5: 6, 6: 12}

        

        # i//n correspond à l'entier, donc à la ligne et i%n correspond au reste donc à la colonne
        tiles = {"mode": "progress",
                 "0": {"val": maxVal[randint(0,board["n"])], "lig": i // board["n"], "col": i % board["n"]},
                 "check": True
                 }

    return tiles


# QUESTION 2.2 :
def put_next_tiles(board, tiles):
    """
    Insère la/les tuiles saisie(s) en paramètre (tiles) dans le board saisi en paramètre (board)
    """
    board = set_value(board, tiles["0"]["lig"], tiles["0"]["col"], tiles["0"]["val"])
    try:
        board = set_value(board, tiles["1"]["lig"], tiles["1"]["col"], tiles["1"]["val"])
    except:
        pass
    return board

    # On place la tuile 0 qui existe dans tout les cas


"""
Pour line_pack et column_pack, foncitons logiquement identiques:
Balise 1: On distinge les deux sens
Balise 2: on fait une boucle for qui pars de la première celle à déplacer et qui vas jusqa la fin de ligne
Balise 3: tile(i) prend valeur de tile(i+1)
Balise 4: On met à 0 la derniere tuile (tile(n-1)) pour finir le déplacement
"""


# QUESTION 2.3 :
def line_pack(board, num_ligne, starter, way):
    """
    Bouge toute une ligne du board en paramètre (board) en fonction de son numéro de ligne saisie en paramètres (num_ligne) 
    avec un sens défini en paramètres (sens) (Vers la droite (0) ou la gauche(1))
    """
    # 1
    if way == 0:  # Vers la droite
        # 2
        for i in range((board["n"] - 1) - starter, 0, -1):
            # 3
            board = set_value(board, num_ligne, i, get_value(board, num_ligne, i - 1))
        # 4
        board = set_value(board, num_ligne, i - 1, 0)
    else:  # Vers la gauche
        # 2
        for i in range(starter, board["n"] - 1):
            # 3
            board = set_value(board, num_ligne, i, get_value(board, num_ligne, i + 1))
        # 4
        board = set_value(board, num_ligne, i + 1, 0)
    return board


# QUESTION 2.4 :
def column_pack(board, num_col, starter, way):
    """
    Bouge toute une colonne du board en paramètre (board) en fonction de son numéro de colonne saisie en paramètres (num_col) 
    avec un sens défini en paramètres (sens) (Vers la bas (0) ou la haut (1))
    """
    # 1
    if way == 0:  # Vers le bas
        # 2
        for i in range((board["n"] - 1) - starter, 0, -1):
            # 3
            board = set_value(board, i, num_col, get_value(board, i - 1, num_col))
            # 4
        board = set_value(board, i - 1, num_col, 0)
    else:  # Vers le haut
        i = board["n"] - 2
        # 2
        for i in range(starter, board["n"] - 1):
            # 3
            board = set_value(board, i, num_col, get_value(board, i + 1, num_col))
        # 4
        board = set_value(board, i + 1, num_col, 0)
    return board


"""
Pour line_move et column_move, foncitons logiquement identiques:
Balise 1: On distinge les deux sens
Balise 2: on fait une boucle for qui pars du début juesqu'a la fin de la ligne ou colonne
Balise 3: On défini tile1 à tile(i) et tile2 à tile(+1)
Balise 4: Si la cellule active =0 (cellule vide),
Balise 5: On décale toute la ligne ou colonne à partir de cette case (i) et on retourne board pour interrompre les mouvements
Balise 6: Sinon, on appliques les conditions de fusion du jeu. si tile1 = x et tile2 = y, on à :
"La somme des tuils doit etre un multiple de 3": (x+y)%3 ==0
"Les tuiles 1 et deux fusinent pour donner 3" :  x in [1,2] : 
- si x est 1 et (x+y)%=0, alors y = 2 
- si x est 2 et (x+y)%=0, alors y = 1 
Balise 7: Si les condition de fusions sont remplies :
- On défini la somme à tile1 + tile2
- On dépalce là ligne ou colonne comme si que tile1 =0
- On set la valeur de tile 0 à somme (pas à tile1*2 car ne marcherait pas pour 1+2 ) 
-On retourne board pour interrompre les mouvements
"""


# QUESTION 2.5 :
def line_move(board, num_lig, way):
    """
    Déplace une ligne en respectant les règles : Mouvement possible quand :
    - le déplacement fait se rencontrer une cellule 1 et 2
    - le déplacement fait se rencontrer deux cellules égales multiples de 3 (ex : 3 et 3, 12 et 12)
    """
    # 1
    if way == 0:  # Vers la droite:
        # 2
        for i in range(board["n"] - 1):
            # 3
            tile1 = get_value(board, num_lig, (board["n"] - 1) - i)
            tile2 = get_value(board, num_lig,
                              (board["n"] - 1) - i - 1)  # == n-2-i. Mit sous l'autre forme pour la comprehension
            # 4
            if tile1 == 0:
                # 5
                board = line_pack(board, num_lig, i, way)
                return board
            # 6
            elif (tile1 + tile2) % 3 == 0 and (tile1 == tile2 or tile1 in [1, 2]):
                # 7
                somme = tile1 + tile2
                board = line_pack(board, num_lig, i, way)
                board = set_value(board, num_lig, (board["n"] - 1) - i, somme)
                return board
    else:  # Vers la gauche
        # 2
        for i in range(board["n"] - 1):
            # 3
            tile1 = get_value(board, num_lig, i)
            tile2 = get_value(board, num_lig, i + 1)
            # 4
            if tile1 == 0:
                # 5
                board = line_pack(board, num_lig, i, way)
                return board
            # 6
            elif (tile1 + tile2) % 3 == 0 and (tile1 == tile2 or tile1 in [1, 2]):
                # 7
                somme = tile1 + tile2
                board = line_pack(board, num_lig, i, way)
                board = set_value(board, num_lig, i, somme)
                return board
    return board


# QUESTION 2.6 :
def column_move(board, num_col, way):
    """
    Déplace une colonne en respectant les règles : Mouvement possible quand :
    - le déplacement fait se rencontrer une cellule 1 et 2
    - le déplacement fait se rencontrer deux cellules égales multiples de 3 (ex : 3 et 3, 12 et 12)
    """
    # 1
    if way == 0:  # Vers le bas
        # 2
        for i in range(board["n"] - 1):
            # 3
            tile1 = get_value(board, (board["n"] - 1) - i, num_col)
            tile2 = get_value(board, (board["n"] - 1) - i - 1,
                              num_col)  # == n-2-i. Mit sous l'autre forme pour la comprehension
            # 4
            if tile1 == 0:
                # 5
                board = column_pack(board, num_col, i, way)
                return board
            # 6
            elif (tile1 + tile2) % 3 == 0 and (tile1 == tile2 or tile1 in [1, 2]):
                # 7
                somme = tile1 + tile2
                board = column_pack(board, num_col, i, way)
                board = set_value(board, (board["n"] - 1) - i, num_col, somme)
                return board

    else:  # vers le haut
        # 2
        for i in range(board["n"] - 1):
            # 3
            tile1 = get_value(board, i, num_col)
            tile2 = get_value(board, i + 1, num_col)
            # 4
            if tile1 == 0:
                # 5
                board = column_pack(board, num_col, i, way)
                return board
            # 6
            elif (tile1 + tile2) % 3 == 0 and (tile1 == tile2 or tile1 in [1, 2]):
                # 7
                somme = tile1 + tile2
                board = column_pack(board, num_col, i + 1, way)
                board = set_value(board, i, num_col, somme)

    return board


"""
On déplace les de la premre à la dernire lignes (pareil pour le colonnes)
"""


# QUESTION 2.7 :
def lines_move(board, way):
    """
    Déplace toutes les tuiles de chaque ligne du board (board) en fonction du sens passé en paramètres (sens)
    """
    for i in range(board["n"]):
        board = line_move(board, i, way)
    return board


# QUESTION 2.8 :
def columns_move(board, way):
    """
    Déplace toutes les tuiles de chaque colonne du board (board) en fonction du sens passé en paramètres (sens)
    """
    for i in range(board["n"]):
        board = column_move(board, i, way)
    return board


# QUESTION 2.9 :
def play_move(board, way, isPlayer = False):
    """
    Déplace tout le board en fonction du sens passé en paramètrters (sens)
    """
    # Cette fonctiuon récupère un sens (h/b/g/d) et doit utiliser un sens en 0 ou 1
    if isPlayer and name =="nt" and isSound():
        winsound.PlaySound("./sounds/tile_move"+ str(randint(1,5)) +".wav", winsound.SND_ASYNC | winsound.SND_FILENAME | winsound.SND_NOSTOP)
        

    # liste pour la line et colonne
    line = {"d": 0, "g": 1}
    column = {"b": 0, "h": 1}

    


    # Si le way est une clé des lignes :
    if way in list(line.keys()):
        # On fait le movement avec la valeur correspondant à la clé du dico ligne
        board = lines_move(board, line[way])

    # Si le way est une clé des colonne :
    elif way in list(column.keys()):
        # On fait le movement avec la valeur correspondant à la clé du dico colonne
        board = columns_move(board, column[way])
    return board
