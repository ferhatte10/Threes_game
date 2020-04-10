# -*- coding: utf-8 -*-
import sys
from os import path
import json
import time

sys.path.append(path.abspath('../'))
from ext_res.termcolor import *
from ui.play_display import *
from ui.user_entries import *
from tiles.tiles_moves import *
from game.play import *


def test_fonctions_2():
    """
    Fonction principale qui permet de tester toutes les autres fonctions
    """
    fonctions = [ 
        "get_next_alea_tiles", 
        "B = BAS, INUTILISABLE",
        "put_next_tiles", 
        "line_pack",
        "column_pack", 
        "F = FERMER, INUTILISABLE",
        "line_move", 
        "H = HAUT, INUTILISABLE",
        "column_move", 
        "lines_move", 
        "columns_move"]

    while 1:
        clear_screen()

        phrase = ("Choix Fonction P2\n"
                  "(A) get_next_alea_tiles\n"
                  "(C) put_next_tiles\n"
                  "(D) line_pack\n"
                  "(E) column_pack\n"
                  "(G) line_move\n"
                  "(I) column_move\n"
                  "(J) lines_move\n"
                  "(K) columns_move\n"
                  "\n"
                  "(F) Fermer")

        values = ["a", "A", "c", "C", "d", "D", "e", "E", "g", "G", "i", "I", "j", "J", "k", "K", "f", "F"]

        user_choice = get_user_custom(values, phrase, indic=" -> ")

        if user_choice == "F":
            return False
        else:
            clear_screen()
            exec("test_" + fonctions[ord(user_choice) - 65] + "()")


def test_get_next_alea_tiles():
    plateau = {"n": 4, "nb_empty_rooms": 7, "tiles": [51, 84, 1, 0, 84, 0, 54, 0, 45, 84, 0, 0, 0, 417, 4, 0]}
    print("\033[4mPlateau :\033[0m")
    print(plateau, "\n")

    print("\033[4mMode init :\033[0m")
    print(json.dumps(get_next_alea_tiles(plateau, "init"), indent=4), "\n")

    print("\033[4mMode encours :\033[0m")
    print(json.dumps(get_next_alea_tiles(plateau, "encours"), indent=4), "\n")

    user_choice = get_user_custom(["o", "O", "n", "N"], "Test concluant ?\n(O) Oui\n(N) Non",
                                  beforeMessage="Vérifier la postion et la valeur des tuiles", indic=" -> ")
    if user_choice == "O":
        succes("get_next_alea_tiles")
    else:
        echec("get_next_alea_tiles")


def test_put_next_tiles():
    plateau = {"n": 4, "nb_empty_rooms": 7, "tiles": [51, 84, 1, 0, 84, 0, 54, 0, 45, 84, 0, 0, 0, 417, 4, 0]}
    print("\033[4mPlateau de Base :\033[0m\n")
    simple_display(plateau)
    try:
        plateau = put_next_tiles(plateau, {'mode': 'init', "0": {'val': 3, 'lig': 0, 'col': 3}, 'check': True})
        assert plateau["tiles"] == [51, 84, 1, 3, 84, 0, 54, 0, 45, 84, 0, 0, 0, 417, 4, 0]
        next("put_next_tiles, tuile (0;3) val 3")
        simple_display(plateau)

        plateau = put_next_tiles(plateau, {'mode': 'init', "0": {'val': 3, 'lig': 1, 'col': 1}, 'check': True})
        assert plateau["tiles"] == [51, 84, 1, 3, 84, 3, 54, 0, 45, 84, 0, 0, 0, 417, 4, 0]
        next("put_next_tiles, tuile (1;1) val 3")
        simple_display(plateau)

        plateau = put_next_tiles(plateau, {'mode': 'encours', "0": {'val': 12, 'lig': 3, 'col': 2},
                                           "1": {'val': 6, 'lig': 2, 'col': 1}, 'check': True})
        assert plateau["tiles"] == [51, 84, 1, 3, 84, 3, 54, 0, 45, 6, 0, 0, 0, 417, 12, 0]
        next("put_next_tiles, tuile (3;2) val 12 ET (2;1) val 6")
        simple_display(plateau)

        succes("put_next_tiles")
    except:
        echec("put_next_tiles")


def test_line_pack():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        palteau = line_pack(plateau, 1, 0, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_pack. Nouveau plateau move (1,0,1)")
        simple_display(plateau)

        palteau = line_pack(plateau, 1, 2, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_pack. Nouveau plateau move (1,2,1)")
        simple_display(plateau)

        palteau = line_pack(plateau, 1, 0, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_pack. Nouveau plateau move (1,0,0)")
        simple_display(plateau)

        palteau = line_pack(plateau, 1, 1, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_pack. Nouveau plateau move (1,1,0)")
        simple_display(plateau)

        succes("line_pack")
    except:
        echec("line_pack")


def test_column_pack():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        column_pack(plateau, 1, 0, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 3, 3, 0, 0, 2, 0, 0, 0, 0, 0]
        next("column_pack. Nouveau plateau move (1,0,1)")
        simple_display(plateau)

        column_pack(plateau, 1, 2, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 3, 3, 0, 0, 2, 0, 0, 0, 0, 0]
        next("column_pack. Nouveau plateau move (1,2,1)")
        simple_display(plateau)

        column_pack(plateau, 1, 0, 0)
        assert plateau["tiles"] == [0, 0, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        next("column_pack. Nouveau plateau move (1,0,0)")
        simple_display(plateau)

        column_pack(plateau, 1, 1, 0)
        assert plateau["tiles"] == [0, 0, 0, 0, 0, 0, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        next("column_pack. Nouveau plateau move (1,1,0)")
        simple_display(plateau)

        succes("column_pack")
    except:
        echec("column_pack")


def test_line_move():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        line_move(plateau, 1, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 3, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_move. Nouveau plateau move (1,1)")
        simple_display(plateau)

        line_move(plateau, 1, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0]
        next("line_move. Nouveau plateau move (1,1)")
        simple_display(plateau)

        line_move(plateau, 2, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
        next("line_move. Nouveau plateau move (2,0)")
        simple_display(plateau)
        line_move(plateau, 2, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 2, 6, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
        next("line_move. Nouveau plateau move (2,0)")
        simple_display(plateau)

        succes("line_move")
    except:
        echec("line_move")


def test_column_move():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        column_move(plateau, 1, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        next("column_move. Nouveau plateau move (1,1)")
        simple_display(plateau)

        column_move(plateau, 1, 1)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
        next("column_move. Nouveau plateau move (1,1)")
        simple_display(plateau)

        column_move(plateau, 2, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 0, 3, 0, 2, 3, 0, 0, 0, 2, 0]
        next("column_move. Nouveau plateau move (2,0)")
        simple_display(plateau)

        column_move(plateau, 2, 0)
        assert plateau["tiles"] == [0, 2, 0, 0, 0, 2, 0, 3, 0, 2, 3, 0, 0, 0, 2, 0]
        next("column_move. Nouveau plateau move (2,0)")
        simple_display(plateau)

        succes("column_move")
    except:
        echec("column_move")


def test_lines_move():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 6, 6, 0, 2, 1, 1, 2, 1, 1, 0, 0, 3, 3, 1, 2]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        lines_move(plateau, 0)
        assert plateau["tiles"] == [0, 0, 6, 6, 0, 2, 1, 3, 0, 1, 1, 0, 0, 3, 3, 3]
        next("lines_move. Nouveau plateau move (0)")
        simple_display(plateau)

        lines_move(plateau, 0)
        assert plateau["tiles"] == [0, 0, 0, 12, 0, 0, 3, 3, 0, 0, 1, 1, 0, 0, 3, 6]
        next("lines_move. Nouveau plateau move (0)")
        simple_display(plateau)

        lines_move(plateau, 0)
        assert plateau["tiles"] == [0, 0, 0, 12, 0, 0, 0, 6, 0, 0, 1, 1, 0, 0, 3, 6]
        next("lines_move. Nouveau plateau move (0)")
        simple_display(plateau)

        lines_move(plateau, 0)
        assert plateau["tiles"] == [0, 0, 0, 12, 0, 0, 0, 6, 0, 0, 1, 1, 0, 0, 3, 6]
        next("lines_move. Nouveau plateau move (0)")
        simple_display(plateau)

        succes("lines_move")
    except:
        echec("lines_move")


def test_columns_move():
    try:
        plateau = init_play(4)
        plateau["tiles"] = [0, 6, 6, 0, 2, 2, 0, 2, 1, 1, 0, 0, 3, 3, 1, 2]
        print("\033[4mPlateau de Base :\033[0m\n")
        simple_display(plateau)

        columns_move(plateau, 1)
        assert plateau["tiles"] == [2, 6, 6, 2, 1, 3, 0, 0, 3, 3, 1, 2, 0, 0, 0, 0]
        next("columns_move. Nouveau plateau move (1)")
        simple_display(plateau)

        columns_move(plateau, 1)
        assert plateau["tiles"] == [3, 6, 6, 2, 3, 6, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        next("columns_move. Nouveau plateau move (1)")
        simple_display(plateau)

        columns_move(plateau, 1)
        assert plateau["tiles"] == [6, 12, 6, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        next("columns_move. Nouveau plateau move (1)")
        simple_display(plateau)
        columns_move(plateau, 1)

        assert plateau["tiles"] == [6, 12, 6, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        next("columns_move. Nouveau plateau move (1)")
        simple_display(plateau)

        succes("columns_move")
    except:
        echec("columns_move")


def test_play_move():
    try:
        echec("ok")

    except:
        echec("ok")


def next(nom_fonction):
    """
    Affiche la réussite d'un assert
    """
    time.sleep(0.5)
    print("Test fonction " + nom_fonction + " réussite")


def succes(nom_fonction):
    """
    Affiche le message de succes en vert
    """
    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " SUCCES"), "blue", "on_green"))


def echec(nom_fonction):
    """
    Affiche le message d'échec en rouge
    """
    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " FAILED"), "white", "on_red"))


def clear_screen():
    # Pour windows
    if name == "nt":
        system("cls")

        # Pour mac et Linux
    else:
        system("clear")
