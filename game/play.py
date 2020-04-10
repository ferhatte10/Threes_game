# -*- coding: utf-8 -*-
import sys
from os import path

sys.path.append(path.abspath('../'))
from tiles.tiles_moves import *
from ui.user_entries import *


# QUESTION 1.1
def init_play(size):
    """ 
    Retourne unu plateau vide correspondant à une nouvelle partie 	
    """

    # On return le dictionnaire du plateau
    return {"n": size, \
            "nb_empty_rooms": size ** 2, \
            "tiles": [0] * (size ** 2) \
            }

# QUESTION 3.1
def create_new_play(size=-1):
    """
    Créer et retourne une nouvelle partie
    """
    # Possible d'utiliser get_score mais le score est toujours égal à 3 (cellule 2 et cellule 1 : 2+1 = 3)
    # Possible d'utiliser get_nb_empty_rooms mais il est topujours égal à n*n-2
    if size == -1:
        sizes = {"T": 2, "P": 3, "M": 4, "G": 5, "E": 6}
        user_input = get_user_custom(["T", "P", "M", "G", "E", "R"],
                                     "Tailles\n(T) Très petit (2x2)\n(P) Petit (3x3)\n(M) Moyen (4x4)\n(G) Grand (5x5)\n(E) Enorme (6x6)\n\n(R) Retour",
                                     " -> ")
        if user_input in sizes.keys():
            if user_input == "R":
                return False
            else:
                size = sizes[user_input]
                game = {"board": put_next_tiles(init_play(size), get_next_alea_tiles(init_play(size), "init")),
                        "next_tile": get_next_alea_tiles(init_play(size), "progress"),
                        "score": 3,
                        "time": 0
                        }
                game["board"]["nb_empty_rooms"] -= 2
                return game
    else:
        game = {"board": put_next_tiles(init_play(size), get_next_alea_tiles(init_play(size), "init")),
                "next_tile": get_next_alea_tiles(init_play(size), "progress"),
                "score": 3,
                "time": 0
                }
        game["board"]["nb_empty_rooms"] -= 2
        return game
