# -*- coding: utf-8 -*-
import sys
from os import path
import time
import json
import math

sys.path.append(path.abspath('../'))
from ext_res.termcolor import *
from ext_res.getkey import *
from ui.play_display import clear_screen


def new_tiles(tiles):
    """
    Prend en paramètres la tuile genere aleatoirement et l'ajoute au fichier
    """
    stats = get_stats()

    stats["general"]["aleaTiles"][str(tiles["0"]["val"])] += 1
    try:
        stats["general"]["aleaTiles"][str(tiles["1"]["val"])] += 1
        stats["general"]["aleaTiles"]["starter1"] += 1
        stats["general"]["aleaTiles"]["starter2"] += 1
    except:
        pass

    json.dump(stats, open('game/statistics.json', 'w'), indent=4)


def get_best_tile(game):
    """
    retourne la meilleure tuile d'un palteau
    """

    return max(game["board"]["tiles"])

     


def get_stats():
    """
    Retourne les statistiques
    """
    fi = open("game/statistics.json", "r")
    stats = json.load(fi)
    fi.close()
    return stats


def new_stats(game):
    """
    Ajoute aux statistiques au
    """
    stats = get_stats()
    currentGameStats = stats["game"][game["board"]["n"] - 2]

    # Nombre de parties
    currentGameStats["nbGame"] += 1

    # Meilleur score
    if game["score"] > currentGameStats["bScore"]:
        currentGameStats["bScore"] = game["score"]

    # Score total
    currentGameStats["tScore"] += game["score"]

    # Score moyen
    if math.isclose(currentGameStats["mScore"], 0):
        currentGameStats["mScore"] = game["score"]
    else:
        currentGameStats["mScore"] += game["score"]
        currentGameStats["mScore"] = currentGameStats["mScore"] // 2

    # Temps total
    currentGameStats["tTime"] += game["time"]

    # Meilleure tuile
    if get_best_tile(game) > currentGameStats["bTile"]:
        currentGameStats["bTile"] = get_best_tile(game)

    json.dump(stats, open('game/statistics.json', 'w'), indent=4)


def statistics():
    """
    Met à jour les statistiques et les affiche
    """ 
    update_stats()
    display_stats()
    print("\n\nAppuyez pour continuer...")
    getkey()
    clear_screen()


def update_stats():
    """
    Calcul les sommes totales et les moyennes
    """
    stats = get_stats()
    nbGame = 0
    tScore = 0
    playingTime = 0

    for i in range(len(stats["game"])):
        nbGame += stats["game"][i]["nbGame"]
        tScore += stats["game"][i]["tScore"]
        playingTime += stats["game"][i]["tTime"]

    stats["general"]["nbGame"] = nbGame
    stats["general"]["tScore"] = tScore
    stats["general"]["playingTime"] = round(playingTime, 2)

    aleaTiles = stats["general"]["aleaTiles"]
    stats["general"]["tTiles"] = aleaTiles["1"] + aleaTiles["2"] + aleaTiles["3"] + aleaTiles["6"] + aleaTiles["12"]

    json.dump(stats, open('game/statistics.json', 'w'), indent=4)


def display_stats():
    """
    Affiche les stats
    """
    stats = get_stats()

    # STATISTIQUES DE GENERAUX DES JEUX
    print("\033[4mStatistiques généraux de jeu : Temps et parties :\033[0m")
    print("Parties totales terminées : ", stats["general"]["nbGame"])
    print("Temps de jeu total :", secondsConv(stats["general"]["playingTime"]))
    print("Score total :", valueConv(stats["general"]["tScore"]))

    aleaTiles = stats["general"]["aleaTiles"]
    aleaTilesTable = [aleaTiles["1"], aleaTiles["2"], aleaTiles["3"], aleaTiles["6"], aleaTiles["12"]]

    if sum(aleaTilesTable) == 0:
        aleaTilesPourcent = [str(0)] * 5
    else:
        sumPercent = sum(aleaTilesTable)
        aleaTilesPourcent = []

        for i in range(len(aleaTilesTable)):
            aleaTilesPourcent.append(str(round(aleaTilesTable[i] / sumPercent * 100, 2)))



    # STATISTIQUES DE GENERAUX DES TUILES
    print("\n\033[4mStatistiques généraux de jeu : tuiles tirées :\033[0m")
    print("Nomrbe total de tuiles tirées :", stats["general"]["tTiles"], "dont ", aleaTiles["starter1"] + aleaTiles["starter2"], "en initialisation")
    tileColor = {0:"on_blue", 1:"on_red"}
    tileValue = {0:1, 1:2, 2:3, 3:6, 4:12}

    for i in range(5):

        try:
            print("Nombre de " + colored(str(tileValue[i]).center(5), "white", tileColor[i]) + " tirées au hasard :", str(aleaTilesTable[i]).rjust(6) + " (" + aleaTilesPourcent[i] + "%) Dont", aleaTiles["starter" + str(i+1)], "en initialisation")
        except:
            print("Nombre de " + colored(str(tileValue[i]).center(5), "grey", "on_white") + " tirées au hasard :",str(aleaTilesTable[i]).rjust(6) + " (" + aleaTilesPourcent[i] + "%)")

    # STATISTIQUES DE PARTIE
    print("\n\033[4mStatistiques de partie :\033[0m")
    center = 10

    columnsL1 = ["",
                 "Nb de",
                 "Best",
                 "Score",
                 "Score",
                 "Temps",
                 "Temps",
                 "Best",
                 " "]
    columnsL2 = ["Tailles",
                 "parties",
                 "score",
                 "cumulé",
                 "moyen",
                 "cumulé",
                 "moyen",
                 "tuile",
                 " "]

    line1 = ""
    line2 = ""
    for i in range(len(columnsL1)):
        line1 += (columnsL1[i].center(center))
        line2 += (columnsL2[i].center(center))


    print(line1 + "\n" + line2 + "\n---------+" + "-" * 85)
    for j in range(len(stats["game"])):
        currentGame = stats["game"][j]

        line = (str(j + 2).center(center-1) + "|" +
                str(currentGame["nbGame"]).center(center) +
                str(currentGame["bScore"]).center(center) +
                valueConv(currentGame["tScore"]).center(center) +
                str(currentGame["mScore"]).center(center) +
                (str(secondsConv(currentGame["tTime"]))).center(center))

        if currentGame["nbGame"] == 0:
            line += "0s".center(center)
        else:
            line += str(secondsConv(round(currentGame["tTime"] / currentGame["nbGame"], 2))).center(center)

        if currentGame["bTile"] == 0:
            line += "0".center(center)
        else:
            line += str(currentGame["bTile"]).center(center)
            line += " (" + str(int(2 / 3 * currentGame["bTile"] - 1)) + " fusions)"
        print(line)

    return 0


def delete_stats():
    stats = {"general": {
        "nbGame": 0,
        "tScore": 0,
        "playingTime": 0.0,
        "tTiles": 0,
        "aleaTiles": {
            "1": 0,
            "starter1": 0,
            "2": 0,
            "starter2": 0,
            "3": 0,
            "6": 0,
            "12": 0
        }},
        "game": [
                    {
                        "nbGame": 0,
                        "bScore": 0,
                        "tScore": 0,
                        "mScore": 0,
                        "tTime": 0.0,
                        "mTime": 0.0,
                        "bTile": 0
                    }] * 5}

    print("Statistiques supprimés")
    json.dump(stats, open('game/statistics.json', 'w'), indent=4)


def secondsConv(time):
    """
    Prend un temps en seconde et retoure le temps convertie en fonction de sa taille
    """
    if time / 3600 > 1:       
        return str(int(time // 3600)) + "h" + str(int((time/3600-time // 3600)*60))[:2]
    elif time / 60 > 1:
        return str(int(time // 60)) + "mn" + str(int((time/60-time // 60)*60))[:2] +"s"
    else:
        return (str(round(time)) + "s")


def valueConv(val):
    if val / 1000000000 > 1:
        return (str(round(val / 1000000000, 2)) + "M")
    elif val / 1000000 > 1:
        return (str(round(val / 1000000, 2)) + "M")
    elif val / 1000 > 1:
        return (str(round(val / 1000, 2)) + "k")
    else:
        return (str(round(val, 2)))
#273