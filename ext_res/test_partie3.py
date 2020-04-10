# -*- coding: utf-8 -*-
import sys
from os import path
import json
from time import *

sys.path.append(path.abspath('../'))
from ext_res.termcolor import *
from ui.play_display import *
from ui.user_entries import *
from tiles.tiles_moves import *
from game.play import *
from life_cycle.cycle_game import *


def test_fonctions_3():
    """
    Fonction principale qui permet de tester toutes les autres fonctions
    """     
    fonctions = [ 
        "create_new_play",
        "B = BAS, INUTILISABLE",
        "get_user_move",
        "cycle_play",
        "get_user_menu",
        "F = FERMER, INUTILISABLE",
        "save_game",
        "H = HAUT, INUTILISABLE",
        "restore_game"]

    while 1:
        clear_screen()

        phrase = ("Choix Fonction P3\n"
                  "(A) create_new_play\n"
                  "(C) get_user_move\n"
                  "(D) cycle_play\n"
                  "(E) get_user_menu\n"
                  "(G) save_game\n"
                  "(I) restore_game\n"
                  "\n"
                  "(F) Fermer")

        values = ["A", "C", "D", "E", "G", "I", "F"]

        user_choice = get_user_custom(values, phrase, indic=" -> ")

        if user_choice == "F":
            return False

        else:
            clear_screen()
            exec("test_" + fonctions[ord(user_choice) - 65] + "()")


def test_create_new_play():
    """
    Function to test create_new_play() ;
    Instuctions : - We affect a random tiles to a game
                  - We create a new game with the function create_new_play
                  - Test if the game was created and crushed the previous game
    """
    import life_cycle.cycle_game

    try:
        print("\n==> Here is our  tiles for the moment of size '2x2' :\n")
        sleep(0.5)
        plateau = {"n": 2, "nb_empty_rooms": 0, "tiles": [6, 2, 3, 2]}
        print("==> Plateau = ", plateau)
        sleep(0.5)
        print("\n==> And now we gonna create a new game (new tiles) of size '2x2' ")
        sleep(0.5)
        p = life_cycle.cycle_game.create_new_play(2)
        print("\n==> Here is the new game(tiles): Plateau = ", p)
        sleep(0.5)
        print(
            "\n==> Now we gonna lunch the necessary tests to prove that the function works, we must have the tile value '1' and '2' in the game(tiles), the score of the game is '3', the size '2x2'  \n")
        sleep(0.5)
        assert 1 in p["board"]["tiles"] and 2 in p["board"]["tiles"]
        print("\n==> Here we check if the value '1' and '2' does exist in the tiles\n")
        sleep(0.5)
        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
        assert life_cycle.cycle_game.get_nb_empty_rooms(p["board"]) == 2
        print("\n==> Here we check if the the number of epty rooms is '2' \n")
        sleep(0.5)
        nextS("create_new_play , paramètre taille " + str(plateau["n"]))

        assert life_cycle.cycle_game.get_score(p["board"]) == 3
        print("\n==> Here we check if the score is '3' \n")
        sleep(0.5)
        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
        assert p["board"]["n"] == 2
        print("\n==> Here we check if the size of the game is '2x2' \n")
        sleep(0.5)
        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
        try:

            printc("*" * 50)
            print("\n\n==> Here is our  tiles for the moment of size '3x3' :\n")
            sleep(0.5)
            plateau = {"n": 3, "nb_empty_rooms": 2, "tiles": [6, 2, 3, 2, 0, 2, 6, 2, 0]}
            print("==> Plateau = ", plateau)
            sleep(0.5)
            print("\n==> And now we gonna create a new game (new tiles) of size '3x3' ")
            sleep(0.5)
            p = life_cycle.cycle_game.create_new_play(3)
            print("\n==> Here is the new game(tiles): Plateau = ", p)
            sleep(0.5)
            print(
                "\n==> Now we gonna lunch the necessary tests to prove that the function works, we must have the tile value '1' and '2' in the game(tiles), the score of the game is '3', the size '3x3'  \n")
            sleep(0.5)
            assert 1 in p["board"]["tiles"] and 2 in p["board"]["tiles"]
            print("\n==> Here we check if the value '1' and '2' does exist in the tiles\n")
            sleep(0.5)
            nextS("create_new_play , paramètre taille " + str(plateau["n"]))
            assert life_cycle.cycle_game.get_nb_empty_rooms(p["board"]) == 7
            print("\n==> Here we check if the the number of epty rooms is '7' \n")
            sleep(0.5)
            nextS("create_new_play , paramètre taille " + str(plateau["n"]))
            assert life_cycle.cycle_game.get_score(p["board"]) == 3 and p["score"] == 3
            print("\n==> Here we check if the score is '3' \n")
            sleep(0.5)
            nextS("create_new_play , paramètre taille " + str(plateau["n"]))
            assert p["board"]["n"] == 3
            print("\n==> Here we check if the size of the game is '3x3' \n")
            sleep(0.5)
            nextS("create_new_play , paramètre taille " + str(plateau["n"]))
            try:
                printc("*" * 50)
                print("\n\n==> Here is our  tiles for the moment of size '4x4' :\n")
                sleep(0.5)
                plateau = {"n": 4, "nb_empty_rooms": 6, "tiles": [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}
                print("==> Plateau = ", plateau)
                sleep(0.5)
                print("\n==> And now we gonna create a new game(new tiles) of size '4x4' ")
                sleep(0.5)
                p = life_cycle.cycle_game.create_new_play(4)
                print("\n==> Here is the new game(tiles): Plateau = ", p)
                sleep(0.5)
                print(
                    "\n==> Now we gonna lunch the necessary tests to prove that the function works, we must have the tile value '1' and '2' in the game(tiles), the score of the game is '3', the size '4x4'  \n")
                life_cycle.cycle_game.sleep(0.5)
                assert 1 in p["board"]["tiles"] and 2 in p["board"]["tiles"]
                print("\n==> Here we check if the value '1' and '2' does exist in the tiles\n")
                sleep(0.5)
                nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                assert life_cycle.cycle_game.get_nb_empty_rooms(p["board"]) == 14
                print("\n==> Here we check if the the number of epty rooms is '14' \n")
                sleep(0.5)
                nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                assert life_cycle.cycle_game.get_score(p["board"]) == 3 and p["score"] == 3
                print("\n==> Here we check if the score is '3' \n")
                sleep(0.5)
                nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                assert p["board"]["n"] == 4
                print("\n==> Here we check if the size of the game is '4x4' \n")
                sleep(0.5)
                nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                try:
                    printc("*" * 50)
                    print("\n\n==> Here is our  tiles for the moment of size '5x5' :\n")
                    sleep(1)
                    plateau = {"n": 5, "nb_empty_rooms": 10,
                               "tiles": [0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0]}
                    print("==> Plateau = ", plateau)
                    sleep(0.5)
                    print("\n==> And now we gonna create a new game(new tiles) of size '5x5' ")
                    sleep(0.5)
                    p = life_cycle.cycle_game.create_new_play(5)
                    print("\n==> Here is the new game(tiles): Plateau = ", p)
                    sleep(0.5)
                    print(
                        "\n==> Now we gonna lunch the necessary tests to prove that the function works, we must have the tile value '1' and '2' in the game(tiles), the score of the game is '3', the size '5x5'  \n")
                    sleep(0.5)
                    assert 1 in p["board"]["tiles"] and 2 in p["board"]["tiles"]
                    print("\n==> Here we check if the value '1' and '2' does exist in the tiles\n")
                    sleep(0.5)
                    nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                    assert life_cycle.cycle_game.get_nb_empty_rooms(p["board"]) == 23
                    print("\n==> Here we check if the the number of epty rooms is '23' \n")
                    sleep(0.5)
                    nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                    assert life_cycle.cycle_game.get_score(p["board"]) == 3 and p["score"] == 3
                    print("\n==> Here we check if the score is '3' \n")
                    sleep(0.5)
                    nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                    assert p["board"]["n"] == 5
                    print("\n==> Here we check if the size of the game is '5x5' \n")
                    sleep(0.5)
                    nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                    try:
                        printc("*" * 50)
                        print("\n\n==> Here is our  tiles for the moment of size '6x6' :\n")
                        sleep(0.5)
                        plateau = {"n": 6, "nb_empty_rooms": 2,
                                   "tiles": [0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0, 0, 2, 6, 2, 0,
                                             0, 2, 6, 2, 0, 1, 0, 2, 6, 2, 0]}
                        print("==> Plateau = ", plateau)
                        sleep(0.5)
                        print("\n==> And now we gonna create a new game(new tiles) of size '6x6' ")
                        sleep(0.5)
                        p = life_cycle.cycle_game.create_new_play(6)
                        print("\n==> Here is the new game(tiles): Plateau = ", p)
                        sleep(0.5)
                        print(
                            "\n==> Now we gonna lunch the necessary tests to prove that the function works, we must have the tile value '1' and '2' in the game(tiles), the score of the game is '3', the size '6x6'  \n")
                        sleep(0.5)
                        assert 1 in p["board"]["tiles"] and 2 in p["board"]["tiles"]
                        print("\n==> Here we check if the value '1' and '2' does exist in the tiles\n")
                        sleep(0.5)
                        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                        assert life_cycle.cycle_game.get_nb_empty_rooms(p["board"]) == 34
                        print("\n==> Here we check if the the number of epty rooms is '34' \n")
                        sleep(0.5)
                        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                        assert life_cycle.cycle_game.get_score(p["board"]) == 3 and p["score"] == 3
                        print("\n==> Here we check if the score is '3' \n")
                        sleep(0.5)
                        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                        assert p["board"]["n"] == 6
                        print("\n==> Here we check if the size of the game is '6x6' \n")
                        sleep(0.5)
                        nextS("create_new_play , paramètre taille " + str(plateau["n"]))
                        succes("create_new_play")
                    except:

                        echec("create_new_game")
                except:

                    echec("create_new_game")
            except:

                echec("create_new_game")
        except:

            echec("create_new_game")

    except:

        echec("create_new_play")


def test_get_user_move():
    """
    Function to test user_game() ;
    Instuctions : - Show the keys which we play with
                  - Let the user click on the keybord
                  - Test if the key clicked is correct (correspond to the rules of the game)
    """
    try:
        print("\n==> The function will give you what to do to test if it works or not just bolow ")
        print("\n                                ↓↓↓↓↓↓↓↓↓↓↓↓↓                                     ")
        print(
            "\n==> So you can click on any key on the keybord but to get the correct user move you must follow the instruction bellow, if the function works so you are allowed to click only the right keys , else the function doesn't work \n")
        print("\n                                ↓↓↓↓↓↓↓↓↓↓↓↓↓                                     \n")

        assert get_user_move() in ["h", "g", "b", "d", "m"]
        print("\n==> The function worked !\n")
        nextS("get_user_move")
        succes("get_user_move")
    except:

        echec("get_user_move")


def test_cycle_play():
    """
    Function to test cycle_game() ;
    Instuctions : - Create a game
                  - Let the user play for a while to test
                  - Test if the user clicked on 'm' or he finised the game
    """
    from life_cycle.cycle_game import cycle_play
    try:

        print("\n==> Now we gonna create a new game with a size of your choose to start our test\n")
        sleep(0.5)
        print(
            "==> Please choose the size by typing  2 for '2x2' , 3 for '3x3', 4 for '4x4', 5 for '5x5', 6 for '6x6' :")
        n = 1
        while n not in ["2", "3", "4", "5", "6"]:
            n = getkey()

        p = create_new_play(int(n))
        print("\n==> Now we gonna let you test the game and play for a while, you can move down up left right \n")
        sleep(1)
        print(
            "\n==> If you click 'm' or 'echap' it suppose to get the menu but the function will return False and we will print it to see it as part of test ")
        sleep(0.5)
        print(
            "\n==> If the game is over the function will return True and we will print it to see it as part of test\n ")
        sleep(0.5)
        print("==> When you finish(game over) enter your name to save the score (if you are in the top 10 of course)")
        sleep(1)
        try:
            assert cycle_play(p)
            print(colored("Out[182]:", "white", "on_red") + "  True\n")
            sleep(0.5)
            print("==> The function returned True so it worked  \n")
            sleep(0.5)
            nextS("cycle_play")
            succes("cycle_play")
        except:
            assert not cycle_play(p)
            print(colored("Out[182]:", "white", "on_red") + "  False\n")
            sleep(0.5)
            print("==> The function returned False so it worked  \n")
            sleep(0.5)
            nextS("cycle_play")
            succes("cycle_play")


    except:

        echec("cycle_play")


def test_get_user_menu():
    """
    Function to test save_game() ;
    Instuctions : - Show the menu
                  - Request the user to choose an option from the menu
                  - Test if the choice of the user  correspond to a correct option
    """
    try:
        print(
            "\n==> This function will show you the menu and you must choose an option , you are allowed to choose only the right options and wich exsits ")
        print(
            "\n==> You need to click on the right keys or swiping up and down and choosing with enter, the function doesn't allow you to click on any key but only the right one\n ")
        print(
            "\n                                                             ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓                                        ")
        print(
            "                                                             ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓                                     \n\n\n\n")
        assert get_user_menu() in ["CONSOLE", "j", "J", "n", "N", "l", "L", "e", "E", "c", "C", "t", "T", "o", "O", "f",
                                   "F"]
        print("\n==> The function worked !\n")
        nextS("get_user_menu")
        succes("get_user_menu")
    except:

        echec("get_user_menu")


def test_save_game():
    """
    Function to test save_game() ;
    Instuctions : - Create a game
                  - Save the game
                  - Test if the game saved does exist in the json save file
    """
    from life_cycle.play import save_game
    try:
        print("\n==> Here is a game (tiles) of size '2x2' \n")
        sleep(0.5)
        game = create_new_play(2)
        print("==> Partie = ", game, "\n")
        sleep(0.5)
        print(
            "\n==> Now the function will request you to choose a spot where do you want to save your game and confirm the save \n")
        sleep(0.5)
        print("==> Please choose a slot where do you want to save the game \n")
        sleep(0.5)
        save_game(game, slot=-1)

        print("\n", colored("Game saved", "white", "on_green"))
        sleep(0.5)
        print(
            "\n==> now we will check if the it really saved with browsing the json file where our saved are and it returns True if the function work ")
        save = json.load(open("game/game_saved.json", "r"))
        for i in range(len(save)):
            if save[i] == game:
                print("\n" + colored("True", "white", "on_green"))
                sleep(0.5)
        print("\n==> The function worked !\n")
        sleep(0.5)
        nextS("save_game")
        succes("save_game")
    except:
        echec("save_game")


def test_restore_game():
    """
    Function to test restore_game() ;
    Instuctions : - Create a game
                  - Save the game
                  - Restore the game
                  - Test if the game restored it correct(the same game created)
    """
    from life_cycle.play import save_game, restore_game
    try:
        print("\n==> Here is a game (tiles) of size '2x2' \n")
        sleep(0.5)
        game = create_new_play(3)
        print("==> Partie = ", game)
        sleep(0.5)
        print(
            "\n==> Now the function will request you to choose a spot where do you want to save your game and confirm the save \n")
        sleep(0.5)
        print("==> Please choose a slot where do you want to save the game \n")
        sleep(0.5)
        save_game(game, slot=-1)
        print("\n", colored("Game saved", "white", "on_green"))
        sleep(0.5)
        print(
            "\nNow the function will request you to choose a game to restore , (as part of test choose the game you saved before in the slot that you choosed) ")
        sleep(0.5)
        print("\n==> We will verify if the game restored it the same the game that we saved  and il returns True\n")
        sleep(0.5)
        assert restore_game(slot=-1) == game or restore_game(slot=-1)["score"] == 3
        print(colored("True", "white", "on_green"))
        sleep(0.5)
        print("\n==> The function worked\n")
        sleep(0.5)
        nextS("restore_game")
        succes("restore_game")

    except:
        echec("save_game")


def nextS(nom_fonction):
    """
    Affiche la réussite d'un assert
    """
    print("Test fonction " + nom_fonction + " réussite\n\n")
    sleep(0.7)


def succes(nom_fonction):
    """
    Affiche le message de succes en vert
    """
    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " SUCCES"), "white", "on_green"))


def echec(nom_fonction):
    """
    Affiche le message d'échec en rouge
    """
    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " FAILED"), "white", "on_red"))
    sys.exit()


def clear_screen():
    # Pour windows
    if name == "nt":
        system("cls")

        # Pour mac et Linux
    else:
        system("clear")
