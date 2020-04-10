# -*- coding: utf-8 -*-
import json
import sys
from os import path

import time

sys.path.append(path.abspath('../'))
from game.play import *
from ui.user_entries import *


# AJOUTS : 5 espaces de sauvgaer
# QUESTION 3.6 :
def save_game(game, slot=-1):
    """
    Sauvegarde la partie passée en paramètre (partie), demande à l'utilisateur sur quel espace il veut sauvegarder la partie et l'enregistre
    """

    # Si la partie est vide, on affiche qu'un message
    if game is None:
        printc("Aucune partie commencée, impossible d'enregistrer")
    else:
        # On lit le fichier des sauvgardes
        games = get_games()

        if slot == -1:

            # On demande à l'utilisateur sur quel espace il veut sauvgarder la partie
            user_save = get_user_custom(["1", "2", "3", "4", "5", "r", "R"],
                                        "Sauvgarder partie\n(1) Espace 1\n(2) Espace 2\n(3) Espace 3\n(4) Espace 4\n(5) Espace 5\n\n(R) Retour",
                                        " -> ", beforeMessage=display_saves(games))
            if user_save == "R":
                return game

            if games[int(user_save) - 1] != {}:

                confirmation = get_user_custom(["O", "N"], "Confirmer\n(O) Oui\n(N) Non", " -> ",
                                               beforeMessage="Une partie existe déjà sur cet espace, voulez-vous réécrire dessus ?")
                if confirmation == "N":
                    print("La partie n'a pas été enregistrée")
                    return game

            # Les parties sont affiches de 1 à 5 mais sont enregistrées de 0 à 4, on fait donc int(user_save)-1
            games[int(user_save) - 1] = game
        else:
            games[slot] = game
        # Une fois les parties modifiées, on réécrit le fichier des sauvagrdes
        printc("Partie enregistrée sur l'emplacement " + str(user_save))
        json.dump(games, open('game/game_saved.json', 'w'))
        return game


# QUESTION 3.7 :
def restore_game(slot=-1):
    """
    On demande à l'utilisateur quel partie il veut sauvegarder
    """
    while 1:
        # On récupère les sauvegardes
        games = get_games()

        if slot == -1:
            # On demande sur quel espance il veut restaurer la partie
            user_save = get_user_custom(["1", "2", "3", "4", "5", "r", "R"],
                                        "Charger partie\n(1) Espace 1\n(2) Espace 2\n(3) Espace 3\n(4) Espace 4\n(5) Espace 5\n\n(R) Retour",
                                        " -> ", 1, display_saves(games))
            if user_save == "R":
                return 0

            game = games[int(user_save) - 1]
        else:
            game = games[slot]

        # Si la partie est vide, on affiche un message
        if game == {}:
            printc("----- /!\\ Sauvegarde vide /!\\ -----\n Création d'une partie\n")
            return create_new_play()

        # Sinon on restaure la partie
        else:
            printc("Partie" + str(user_save) + " restaurée")
            return game


# QUESTION BONUS
def delete_save(slot=-1):
    """
    Fonction qui supprime une partie enregistrée
    """
    while 1:
        # On récupère les sauvegardes
        games = get_games()

        if slot == -1:
            # On demande quelle sauvegarde il veut supprimer
            user_save = get_user_custom(["1", "2", "3", "4", "5", "r", "R"],
                                        "Supprimer partie\n(1) Espace 1\n(2) Espace 2\n(3) Espace 3\n(4) Espace 4\n(5) Espace 5\n\n(R) Retour",
                                        " -> ", 1, display_saves(games))
            if user_save == "R":
                return 0

            game = games[int(user_save) - 1]
            # Si la partie est vide, on le dit
            if game == {}:
                printc("----- /!\\ Sauvegarde vide /!\\ -----\n Selectionnez un autre emplacement\n")
            else:
                # On demande confirmation de suppresion pour éviter les erreurs
                beforeMessage = "Confirmez-vous la suppression de la sauvagrde " + user_save + " ? Il sera impossible de la récuperer"
                confirmation = get_user_custom(["O", "N"], "Confirmer\n(O) Oui\n(N) Non", " -> ",
                                               beforeMessage=beforeMessage)

                # Si il change d'avis
                if confirmation == "N":
                    printc("La partie n'a pas été supprimée")
                else:
                    # On réécrit la partie vide sur la variable
                    games[int(user_save) - 1] = {}

                    # On réécrit le fichier
                    printc("Sauvegarde détruite sur l'emplacement " + str(user_save))
                    json.dump(games, open('game/game_saved.json', 'w'))
        else:
            # On réécrit la partie vide sur la variable
            games[slot] = {}
            print("Sauvegarde " + str(slot) + " supprimée")
            json.dump(games, open('game/game_saved.json', 'w'))
            return


def delete_saves():
    for i in range(5):
        delete_save(i)


def get_games():
    file = open("game/game_saved.json", "r")
    games = json.load(file)
    file.close()
    return games


# QUESTION BONUS
def display_saves(games):
    """
    Fonction qui affiche les sauvegardes enregistrées
    """
    lines = ""
    for i in range(len(games)):
        # Si il n'y à pas d'erreur, la sauvegarde existe
        try:
            # Permet à aligner sur la gauche
            newLine = "\033[4mEspace " + str(i + 1) + " :\033[0m Taille : " + str(
                games[i]["board"]["n"]) + ", score : " + str(games[i]["score"])
            while len(newLine) < 45:
                newLine += " "
            lines += newLine + "\n"
        except:
            lines += "\033[4mEspace " + str(i + 1) + " :\033[0m Emplacement vide          \n"
    return lines
