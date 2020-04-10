# -*- coding: utf-8 -*-
import sys
from os import path

# package qui permet la coloration du texte

sys.path.append(path.abspath('../'))
from ext_res.test_partie1 import *
from ext_res.test_partie2 import *
from ext_res.test_partie3 import *


def test_fonctions():
    fonctions = [ 
            "fonctions_1", 
            "B = BAS, INUTILISABLE",
            "fonctions_2", 
            "fonctions_3", 
            "quitter"]

    while 1:
        clear_screen()

        phrase = ("Choix Fonction\n"
                  "(A) fonctions_1\n"
                  "(C) fonctions_2\n"
                  "(D) fonctions_3\n"
                  "\n"
                  "(F) Fermer")

        values = ["A", "C", "D", "F"]

        user_choice = get_user_custom(values, phrase, indic=" -> ")

        if user_choice == "F":
            return False

        else:
            clear_screen()
            exec("test_" + fonctions[ord(user_choice) - 65] + "()")


def test_quitter():
    sys.exit()
