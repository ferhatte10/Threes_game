# -*- coding: utf-8 -*-
import sys
from os import path
import json
import datetime
import re

sys.path.append(path.abspath('../'))
from ext_res.termcolor import *
from ext_res.tallchars import *
from ext_res.getkey import *
from ui.play_display import *
from ui.user_entries import *



# QUESTION BONUS 4.1
def get_game_score(game, indice):
    """
    Retourne une partie donnée à l'indice passé en paramètres
    """
    return game[indice]["score"]


# QUESTION BONUS 4.2
def set_game(games, new_game, indice):
    """
    Prend une nouvelle partie en paramètres et la met dans le tableea partie à l'indice en paramèrtes
    """
    games[indice] = new_game
    return games


# QUESTION BONUS 4.3
def move_games(games, indice):
    """
    Déplace les parties vers la droite jusqu'à un indice donné. La derniere partie est donc supprimée
    """
    for i in range(len(games) - 1, indice, -1):
        games = set_game(games, games[i - 1], i)
    return games


# QUESTION BONUS 4.4
def get_best_score(games, new_game):
    """
    Retourne l'indice de la première partie ayant le score inferieur à celle passée en paramètres
    """
    indice = -1
    score = new_game["score"]

    for i in range(len(games) - 1, 0, -1):
        if games[i] == {}:
            indice = i
        else:
            if score >= get_game_score(games, i):
                indice = i
    return indice

def get_local_scores():
    fi = open("game/scores.json", "r")
    scoresTable = json.load(fi)
    fi.close()
    return scoresTable

def get_online_scores():
    import urllib.request
    link = "http://facultatifmdr.000webhostapp.com/python/scores.txt"


    with urllib.request.urlopen(link) as url:
        scoresTable = json.loads(url.read())

    return scoresTable


# QUESTION BONUS 4.
def add_score_local(game, score):
    """
    Vérifie si la partie est un nouveau score et l'ajoute au tableau des scores si oui
    """
    clear_screen()
    print(("Votre score : " + str(score)).center(43))

    scoresTable = get_local_scores()
    games = scoresTable[game["board"]["n"] - 2]

    
    # Création du dictionnaire "nouvelle partie"
    new_game = {"date": 0, "name": 0, "score": score}

    # On prend l'indice de la première partie ayant le score inferieur de la nouvelle partie
    indice = get_best_score(games, new_game)

    # Si l'indice != 0 (=top 5 score) on l'ajoute au tableau
    if indice > 0:
        games = move_games(games, indice)

        # Affiche grace à la fonction tallchars la place du nouveau score
        places = ["PREMIERE PLACE !", "DEUXIEME PLACE !", "TROISIEME PLACE !", "QUATRIEME PLACE !", "CINQUIEME PLACE !"]
        tallchars(places[indice - 1], ["blue", "red"], clignCd=0.2, clignRepeats=5)

        # Saisie du pseudo entre 3 et 18 caractères
        name = input("Entrez votre nom : \n")
        name = re.sub('[^A-Za-z0-9 ]+', '', name)
        while len(name) > 16:
            name = input("Beaucoup trop long : \n")
            name = re.sub('[^A-Za-z0-9 ]+', '', name)
        while len(name) < 3:
            name = input("Soyez un peu plus précis : \n")
            name = re.sub('[^A-Za-z0-9 ]+', '', name)

        # On écris le nom
        new_game["name"] = name

        # On récupère la date du jour et on modifie la partie en y mettant le pseudo et la date
        now = datetime.datetime.now()
        new_game["date"] = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

        # On fais les changements de partie si la partie est un top 10 meilleur score
        games = set_game(games, new_game, indice)

    # On réécrit le fichier contenant les scores

    scoresTable[game["board"]["n"] - 2] = games

    file = open("game/scores.json", "w")
    json.dump(scoresTable, file, indent=4)
    file.close()

    add_score_online(new_game,game["board"]["n"])

    display_scores(get_local_scores(), game["board"]["n"] - 2,0, new_game)

    print("\n\nAppuyez pour continuer...")
    getkey()
    clear_screen()

def add_score_online(game, taille):
    import os

    try:
        print("Chargement des scores...")
        games = get_online_scores()[taille-2]

        indice = get_best_score(games, game)

        if indice > 0:
            games = move_games(games, indice)
            games = set_game(games, game, indice)

        # On réécrit le fichier contenant les scores
        

        online_games = get_online_scores()
        online_games[taille-2] = games
    
    
        import ftplib
        session = ftplib.FTP('files.000webhost.com','facultatifmdr','facultatifpython')

        file = open("temp.txt","w")
        file.write(json.dumps(online_games))
        file.close()

        file = open('temp.txt','rb')   
        output = session.storbinary('STOR public_html/python/scores.txt', file)
        file.close() 
        os.remove("temp.txt")
        session.quit()
    except:
        print("Aucune connexion, aucun score enregistré sur le serveur")
    clear_screen()
    return 0

# QUESTION BONUS 4.5
def display_scores(scoresTable, size, source, game=None):
    """
    Affiche les meilleurs scores avec de la couleur 
    """

    # Couleur des bordures
    f = open("game/options.json", "r")
    options = json.load(f)
    f.close()

    colorTxt = options["bordercolor"][0]
    colorBackgorund = options["bordercolor"][1]

    # Couleur du texte vide :
    txtColor = "grey"
    backgroundTktColor = "on_white"

    scores = scoresTable[size]


    # Grand "SCORE" + source + affichage taille du plateau
    if source == 0:
        sourceTxt = "Locaux"
    else:
        sourceTxt = "En ligne"

    print(colored(" " * 48, colorTxt, colorBackgorund))
    print(makeTall(" SCORES ", "white", colorBackgorund[3:]))
    print(colored(sourceTxt.center(48), "white", colorBackgorund))
    print(colored(" " * 48, colorTxt, colorBackgorund))
    print(colored(("Scores des plateaux de taille : " + str(size + 2)).center(48), "white", colorBackgorund))

    # On défini nos lignes : Etoile, vide, caractères pour faciliter la suite
    borderCar = colored("*", colorTxt, colorBackgorund)
    borderLine = borderCar * 48

    emptyCar = colored(" ", txtColor, backgroundTktColor)
    emptyLine = borderCar + emptyCar * 5 + borderCar + emptyCar * 12 + borderCar + emptyCar * 18 + borderCar + emptyCar * 8 + borderCar

    print(borderLine)

    # On parcours le tableau des meilleurs scores
    i = 0
    for i in range(len(scores)):
        # On fait des choses seulement si le dictionnaire contient une partie non vide
        if len(scores[i]) != 0:
            # La première ligne (POS, DATE, PSEUDO, SCORE) est comme une partie
            if i == 0:
                pos = "POS"
            else:
                pos = str(i)

            if game == scores[i]:
                txtColor = "white"
                backgroundTktColor = "on_red"
            else:
                txtColor = "grey"
                backgroundTktColor = "on_white"
            pos = colored(pos.center(5), txtColor, backgroundTktColor)
            date = colored(str(scores[i]["date"]).center(12), txtColor, backgroundTktColor)
            name = colored(str(scores[i]["name"]).center(18), txtColor, backgroundTktColor)
            score = colored(str(scores[i]["score"]).center(8), txtColor, backgroundTktColor)

            print(emptyLine + "\n" + borderCar + pos + borderCar + date + borderCar + name + borderCar + score + borderCar + "\n" + emptyLine + "\n" + borderLine)
    return 0


def choose_score():
     #Récupère le mouvement du joueur et appelle la fonction en fonction du mouvement
    while 1:
        values = ["L","O","R","R"]
        menu = ("Choix\n"
            "(L) Scores locaux\n"
            "(O) Scores en ligne\n"
            "\n"
            "(R) Retour")


        user_move = get_user_custom(values, menu," -> ")

        if user_move == "L":

            # On recupere le fichier des scores
            scoresTable = get_local_scores()   
            navigate_scores(scoresTable, 0,0)     
        elif user_move == "O":
            print("Chargement des scores...")
            try:
                scoresTable = get_online_scores()
                clear_screen()
                navigate_scores(scoresTable, 0,1)
            except:
                print("Aucune connexion internet, impossible de charger les scores en ligne\nAppuyez pour continuer...")
                getkey()
        elif user_move == "R":
            return 0


    
        


def navigate_scores(scoresTable, i,source):
    """
    Permet de naviguer entre les différents tableaux de score : un tableau par taille de grille
    """

    display_scores(scoresTable,i, source)
    val = ""
    while val not in ["ENTER", "m", "r"]:
        if source == 0:
            print("Utilisez les flèches ou (h/b) pour naviguer entre les menus.\nEntrer \"R\" pour efface les score ou appuyez sur \"entrer\" pour continuer\n")
        else:
            print("Utilisez les flèches ou (h/b) pour naviguer entre les menus.\nAppuyez sur \"entrer\" pour continuer\n")
           

        val = getkey()
        clear_screen()

        if val == "b" and i == 0:
            i = 4
        elif val == "b":
            i -= 1
        elif val == "h" and i == 4:
            i = 0
        elif val == "h":
            i += 1
        elif val == "r" and source == 0:
            reset_scores(i)
        elif val == "r" and source == 1:
            val = ""

        display_scores(scoresTable,i, source)

    clear_screen()
    
    return 0


# QUESTION BONUS 4.7
def reset_scores(indice):
    """
    Créer un nouveau tableau contetnant 10 parties vide et l'écrit dans le fichier score.json : remise à 0 des scores
    """
    scoresTable = get_local_scores()
    scoresTable[indice] = [{"date": "DATE", "name": "PSEUDO", "score": "POINTS"}] + [{}] * 5

    json.dump(scoresTable, open("game/scores.json", "w"), indent=4)
    navigate_scores(scoresTable, indice,0)
    return 0


def delete_scores():
    fi = open("game/scores.json", "r")
    scoresTable = json.load(fi)
    fi.close()

    for i in range(5):
        scoresTable[i] = [{"date": "DATE", "name": "PSEUDO", "score": "POINTS"}] + [{}] * 5
        print("Score tableau " + str(i + 2) + " supprimé")
    json.dump(scoresTable, open("game/scores.json", "w"), indent=4)


def change_score_name(n, pos, name):
    fi = open("game/scores.json", "r")
    scoresTable = json.load(fi)
    fi.close()

    scoresTable[n - 2][pos]["name"] = name
    json.dump(scoresTable, open('game/scores.json', 'w'), indent=4)
    return 0
