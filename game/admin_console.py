# -*- coding: utf-8 -*-
import sys
from os import path, name


from game.scores import *
from game.statistics import *
from life_cycle.play import *
from ui.play_display import *
from ext_res.test_partie1 import *
from ext_res.test_partie2 import *
from ext_res.test_partie3 import *
from ext_res.tests import *


def console(game=None):
    print("Tapez \"help\" pour afficher les commandes")
    console = True
    while console:

        user_choice = input("Console:\n").lower().split(" ")
        commands = {"help h": "help h",
                    "test":"test_fonctions()",
                    "testp1": "test_fonctions_1()",
                    "testp2": "test_fonctions_2()",
                    "testp3": "test_fonctions_3()",
                    "delsaves": "delete_saves()",
                    "delscores": "delete_scores()",
                    "delstats": "delete_stats()",
                    "delall": "delall",
                    "setval": "setval",
                    "settiles": "settiles",
                    "csn": "csn",
                    "back": "back",
                    "exit": "exit"}

        if user_choice[0] in list(commands.keys()) or user_choice[0] in ["h", "help"]:
            if user_choice[0] in ["help", "h"]:
                help(commands)
            elif user_choice[0] == "back":
                console = False
            elif user_choice[0] == "exit":
                sys.exit()

            # On détruit : sauvegaardes, scores et statistiques
            elif user_choice[0] == "delall":
                delete_saves()
                delete_scores()
                delete_stats()

            # set valeur
            elif user_choice[0] == "setval":
                if game["board"] is None:
                    print("Aucune partie commencée")
                else:
                    try:
                        game["board"] = set_value(game["board"], int(user_choice[1]), int(user_choice[2]),
                                                  int(user_choice[3]))
                    except:
                        print("Paramètres invalide")

            # Défini un plateau entier
            elif user_choice[0] == "settiles":
                if game is None:
                    print("Aucune partie commencée")
                else:
                    try:
                        if game["board"]["n"] ** 2 == len(list(map(int, user_choice[1].split(",")))):
                            game["board"]["tiles"] = list(map(int, user_choice[1].split(",")))
                        else:
                            print("Paramètres invalide")
                    except:
                        print("Paramètres invalide")

                        # Change le nom d'un scroe
            elif user_choice[0] == "csn":
                try:
                    change_score_name(int(user_choice[1]), int(user_choice[2]), user_choice[3])
                except:
                    print("Commande invalide. Syntaxe : csn [taille n] [position] [nouveau nom]")

            # Pas de commande speciale
            else:
                exec(commands[user_choice[0]])
        else:
            print("Commande \"" + user_choice[0] + "\" introuvable, tapez \"help\" pour afficher les commandes")


def help(commands):
    commandsHelp = {
        "help h": "Affiche les commandes et leur fonctionnement",
        "test" : "Lance le programme général des test",
        "testp1": "Affiche les fonction test de la partie 1",
        "testp2": "Affiche les fonction test de la partie 2",
        "testp3": "Affiche les fonction test de la partie 3",
        "delsaves": "Détruit toutes les sauvegardes (irreversible)",
        "delscores": "Détruit tous les scores (irreversible)",
        "setval": "paramètres : [ligne] [colonne] [valeur]. Permet de placer une tuile personalisée pendant le jeu",
        "csn": "paramètres : [plateau] [position] [nom]. Permet de modifier le nom d'un score (tricheur)",
        "settiles": "paramètres : [plateau]. Permet de définir le plateau de jeu",
        "back": "Ferme la console",
        "exit": "Ferme le jeu"
    }
    for i in range(len(commands)):
        try:
            print(list(commands)[i].ljust(10) + " : " + commandsHelp[list(commands)[i]])
        except:
            print(list(commands)[i].ljust(10) + " : aucune aide disponible pour cette commande")
