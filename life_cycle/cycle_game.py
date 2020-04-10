# -*- coding: utf-8 -*-
import sys
from os import path
import time
import copy

sys.path.append(path.abspath('../'))
from ui.play_display import *
from tiles.tiles_moves import *
from game.play import *
from game.scores import *
from ui.user_entries import *
from game.admin_console import *
from game.statistics import *


# QUESTION 1.8
def is_game_over(board):
    """
    Retourne true si il n'y à plus aucune cellule vide dans le plateau passé en paramètres (plateau), False sinon
    """

    # On créer une copie pour vérifier si il reste des mouvements
    oldBoard = copy.deepcopy(board)

    # On défini les mouvements pososibles (dans les 4 directions)
    moves = ["h", "b", "g", "d"]

    # On Fais tous les mouvements sur la copie du plateau
    for i in range(len(moves)):
        oldBoard = play_move(oldBoard, moves[i])

    # Si les 2 plateaux sont identiques, il ne reste pas de mouvements
    if oldBoard == board:
        # C'est la fin de partie si les deux plateaux sont identiques et si il n'y à plus de cellules libre
        return True and get_nb_empty_rooms(board) == 0
    return False


# QUESTION 1.9
def get_score(board):
    """
    Retourne la somme de toutes les cellules dans le plateau passé en paramètre (plateau)
    """
    return sum(board["tiles"])


# QUESTION 3.3 :
def cycle_play(game):
    # On défini une variable pour là clarete :

    board = game["board"]
    startTime = time.time()

    # On affiche le plateau
    full_display(board)

    while not is_game_over(board):

        # On choisi la couleur de la cellule en fonction de la valeur :

        # On defini les couleurs en fonciton de la valeur
        colors = [["white", "on_blue"], ["white", "on_red"], ["grey", "on_white"]]

        # On tire une nouvelle tuile et on l'affiche
        try:
            user_move

            # On tire une nouvelle tuile seulement si le plateau a changé
            if board != beforeBoard:
                nextTile = get_next_alea_tiles(board, "encours")
        except:
            nextTile = game["next_tile"]

        valNextTile = nextTile["0"]["val"]

        if valNextTile > 3:
            color = 2
        else:
            color = valNextTile - 1

        beforeBoard = copy.deepcopy(board)

        print("\nTuile suivante : ", colored("  " + str(valNextTile) + "  ", colors[color][0], colors[color][1]),
              "score:", game["score"])
        # On récupère le mouvement du joueur
        user_move = get_user_move()

        # SI le joueur veut ouvrir le menu
        if user_move == "m":
            game["time"] += round(time.time() - startTime, 2)
            return False

        elif user_move == "console":
            tmp = console(game)
            if tmp is not None:
                game = tmp
            user_move = None

            
    

        # (Sinon) On joue le mouvement du joueur
        board = play_move(board, user_move, True)

        # On vérifie si la partie est finie:
        if is_game_over(board):
            break

        # On rééaffiche le plateau après le mouvement du joueur
        full_display(board)

        # Si la position de la tuile aléatoire a été recouvertte et si il reste des cases vides on retire une t uile
        while (not is_room_empty(board, nextTile["0"]["lig"], nextTile["0"]["col"])) and (
                get_nb_empty_rooms(board) != 0):
            # On enregister la valeur de la tuile
            tmpVal = nextTile["0"]["val"]
            # On reture une tuile
            nextTile = get_next_alea_tiles(board, "progress")
            # On lui rééaffecte la valeur
            tmpVal = nextTile["0"]["val"] = tmpVal

        # Si il reste des tuiles vides, on set la tuile
        if get_nb_empty_rooms(board) != 0 and user_move is not None:
            board = put_next_tiles(board, nextTile)
            new_tiles(nextTile)

        # On calcule le score
        game["score"] = get_score(board)

        # On attend 0.2s avant de rééaficher le plateau pour correctemetn voir ou à été place la tiule
        time.sleep(0.2)
        # On clear l'écran pour voir correctmeent
        clear_screen()
        # On rééaffiche le plateau
        full_display(board)

    # On attend que je joueur confirme pour finir la partie
    game["time"] += round(time.time() - startTime, 2)
    print("Plus aucun mouvement possible, fin de partie.\nScore final : " + str(
        game["score"]) + ". Temps total : " + secondsConv(game["time"]) + ".\n\n\nAppuyer pour continuer...")
    getkey()

    # On gère le score et les statistiques

    new_stats(game)
    add_score_local(game, get_score(board))
    return True


def leave(game):
    if game is not None:
        new_stats(game)
    printc("A bientôt !")
    sys.exit()
