# -*- coding: utf-8 -*-
import sys
from os import path, name
import json
import time
import shutil


from ext_res.termcolor import *
from ext_res.tallchars import *
from ext_res.getkey import *
from ui.user_entries import *
from life_cycle.play import *
from ui.play_display import *

def getOptions():
    file = open("game/options.json","r")
    options = json.load(file)
    file.close()

    return options

def writeOptions(new_options):
    file = open("game/options.json","w")
    json.dump(new_options, file)
    file.close()
    return 0

def isSound():
    return getOptions()["isSound"]


#QUESTION BONUS 1 :
def options():
    """
    Fonction principale de navigation des menus
    """
    from life_cycle.play import delete_save
    while 1:
        #Récupère le mouvement du joueur et appelle la fonction en fonction du mouvement
        values = ["D","P","C","F","E","R"]
        menu = ("Options\n"
                "(D) Détruire sauvgarde\n"
                "(P) Plateau (couleur des bordures)\n"
                "(C) Crédits\n"
                "(F) Fast Mode\n"
                "(E) Effets Audio\n"
                "\n"
                "(R) Retour")
        user_move = get_user_custom(values, menu," -> ")
        if user_move == "C":
            credits()
        elif user_move == "P":
            color_display()
        elif user_move == "D":
            delete_save()
        elif user_move == "F":
            active_desactive("fast_mode","Fast mode")
        elif user_move == "E":
            active_desactive("isSound","Son")
        elif user_move == "R":
            return 0

def active_desactive(fromFile, param):
    """
    Fonction qui désactive le mode rapide ou le son, après des test
    """

    #On récupère le fichieur configuration
    options = getOptions()


    #Si le Fast Mode est activé: on proprse de le désactiver
    if options[fromFile]:
        user_input = get_user_custom(["D","R"], param +" activé\n(D) Désaciver\n(R) Retour"," -> ")
        if user_input ==  "D":
            printc("Vous venez de désactiver le " + param)
            options[fromFile] = False
        else:
            printc("Le "+ param +" est resté activé")
    #Si le Fast Mode est désactivé: on proprse de l'activer
    else:
        user_input = get_user_custom(["A","R"], param +" désactivé\n(A) Activer\n(R) Retour"," -> ")
        if user_input == "A":
            printc("Vous venez d'activer le " + param)
            options[fromFile] = True
        else:
            printc("Le "+ param +" est resté désactivé")

    #Après avoir réécrit la variable option, on réécrit le fichier
    writeOptions(options)

    return 0



def credits():
    """
    Affiche les crédits
    """
    print(makeTall(" CREDITS", "white"))
    time.sleep(1)
    clear_screen()

    credits=[
    "",
    "Jeu réalisé par :",
    "        \033[4mAZZ Ilian(572)\033[0m",
    "        \033[4mSAIDOUN Ferhat\033[0m",
    "",
    "dans le cadre",
    "du projet tutoré",
    "a l'IUT Paris 13",
    "Villetaneuse",
    "",
    "Sujet écrit par B. LEMAIRE",
    "Reproduction Interdite",
    "",
    "Contenu fortement enrichi",
    "20/20 svp",
    "Pour le travail",
    "",
    "© 2019 - 2020 AZZOUZ Ilian (Twitter : @ilian572) - SAIDOUN Ferhat",
    "",
    "        \033[4mMerci d'avoir joué !\033[0m"
    ]

    #Affiche les lignes 1 par une en attendant entre chaque
    for i in range(len(credits)):
        time.sleep(0.6)
        printc(credits[i])

    print("\n\nAppuyez pour continuer...")
    getkey()
    clear_screen()


def color_display():
    """
    Affiche les couleurs pour modifier la couleur des bordures
    """

    colorsBefore = ("\033[0;37;42m          Vert            \033[0;00;00m\n"
                    "\033[0;37;43m          Jaune           \033[0;00;00m\n"
                    "\033[0;37;45m          Violet          \033[0;00;00m\n"
                    "\033[0;37;46m          Bleu            \033[0;00;00m\n"
                    "\033[0;37;47m          Gris            \033[0;00;00m\n")

    #On défini le menu, les valeurs possibles
    menu = "Couleurs\n(1) Vert\n(2) Jaune\n(3) Violet\n(4) Bleu\n(5) Gris\n\n(R) Retour"
    values = ["1","&","2","é","3","\"","4","\'","5","(","R","r"]

    #On récupère la saisie de l'utuilisateur
    user_choice = coloredMenu(menu.split("\n"),values," -> ",beforeMessage=colorsBefore)

    #Retour
    if user_choice == "R":
        return 0
    #On défini les couleurs (texte et bg)
    colors = [["green","on_green"], \
              ["yellow","on_yellow"], \
              ["magenta","on_magenta"], \
              ["cyan","on_cyan"], \
              ["grey","on_grey"]]

    #On lis le fichier,
    file = open("game/options.json","r")
    options = json.load(file)
    file.close()

    #On édite le fichier,
    options["bordercolor"] = colors[int(user_choice)-1]

    #On écris le fichier,
    writeOptions(options)
    return 0

def how_play():
    print(makeTall("  threes", "white"))
    time.sleep(1)
    clear_screen()

    screenWidth = shutil.get_terminal_size().columns



    howToPlay = [
    "        \033[4mBut du jeu :\033[0m",
    "",
    "Le jeu constite à faire glisser les tuiles sur une grille",
    "et de les combiner pour obtenir une meilleure tuile en suivant les règles de fusion. ",
    "",
    "Le but est d'obtenir le meilleur score possible.",
    "La partie s'arrête quand vous ne pouvez plus faire de mouvements.",
    "wait",
    "        \033[4mRègles de fusion :\033[0m",
    "",
    "2 cas :",
    " - Les tuiles sont de valeur 1 et 2",
    "ou",
    " - Les valeurs des tuiles sont égales et multiples de 3",
    "(3 et 3, 6 et 6 ou 24 et 24 par exemple)",
    "",
    "En dehors de ces règles :",
    "Il vous sera impossible de fusionner",
    "wait",
    "        \033[4mFusion possibles :\033[0m",
    "",
    "exemple1",
    "1 et 2 fusionnent       3 et 3 fusionnent" + " " * (screenWidth-41),
    "  si mouvement            si mouvement   " + " " * (screenWidth-41),
    " vers la gauche           vers la droite " + " " * (screenWidth-41),
    " pour obtenir 3.         pour obtenir 6. " + " " * (screenWidth-41),
    "",
    "        \033[4mFusion impossibles (exemples) :\033[0m",
    "",
    "exemple2",
    "2 et 2 ne suivent       3 et 6 ne suivent" + " " * (screenWidth-41),
    " pas les règles,         pas les règles :" + " " * (screenWidth-41),
    "fusion impossible       3 différent de 6 " + " " * (screenWidth-41),
    "                       fusion impossible" + " " * (screenWidth-41),
    "wait",
    "        \033[4mA chaque tour :\033[0m",
    "",
    "A chaque tour, la tuile suivante vous est annoncée",
    "Elle peut prendre la valeur :",
    "",
    "       MODE             VALEURS POSSIBLES ",
    "   Très petit (2x2)         1, 2 ou 3     ",
    "    Petit (3x3)             1, 2 ou 3     ",
    "    Moyen (4x4)             1, 2 ou 3     ",
    "    Grand (5x5)           1, 2, 3 ou 6    ",
    "    Enorme (6x6)        1, 2, 3, 6 ou 12 ",
    "",
    "Elle sera placée après votre mouvement,",
    "sur un emplacement libre du plateau.",
    "wait",
    "        \033[4mComment jouer\033[0m",
    "",
    "Vous avez 3 méthodes pour vous déplacer :",
    "",
    " - h/b/g/d (Haut, Bas, Gauche, Droite)",
    " - z/q/s/d pour les g@m€rz",
    " - Les flèches du clavier",
    "",
    "/!\\ Si le mode rapide est désactivé, ",
    "il sera impossible d'utiliser les flèches",
    "",
    "        \033[4mBon jeu !\033[0m",
    ]



    #Affiche les lignes 1 par une en attendant entre chaque
    for i in range(len(howToPlay)):
        if howToPlay[i] == "wait":
            print("\n\n\nAppuyez pour continuer...")
            val = getkey()
            if val == "m":
                return 0
            clear_screen()
        elif howToPlay[i] == "exemple1":
            full_display({"n":5,"tiles":[1,2,0,3,3]})
        elif howToPlay[i] == "exemple2":
            full_display({"n":5,"tiles":[2,2,0,6,3]})
        else:
            printc(howToPlay[i])
            time.sleep(0.3)
    print("\n\n\nAppuyez pour terminer...")
    getkey()
    clear_screen()
