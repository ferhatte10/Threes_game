# -*- coding: utf-8 -*-
def test_fonctions_1():
    """
    Fonction principale qui permet de tester toutes les autres fonctions
    """
    from ui.play_display import clear_screen
    from ui.user_entries import get_user_custom

    fonctions = [
        "init_play", 
        "B = BAS, INUTILISABLE",
        "check_indice", 
        "check_room", 
        "get_value", 
        "F = FERMER, INUTILISABLE",
        "set_value", 
        "H = HAUT, INUTILISABLE",
        "is_room_empty", 
        "get_nb_empty_rooms", 
        "is_game_over", 
        "get_score",
        "full_display"]

    while 1:
        clear_screen()

        phrase = ("Choix Fonction P1\n"
                "(A) init_play\n"
                "(C) check_indice\n"
                "(D) check_room\n"
                "(E) get_value\n"
                "(G) set_value\n"
                "(I) is_room_empty\n"
                "(J) get_nb_empty_rooms\n"
                "(K) is_game_over\n"
                "(L) get_score\n"
                "(M) full_display\n"
                "\n"
                "(F) Fermer")
    
        values = ["A","C","D","E","G","I","J","K","L","M","F"]

        user_choice = get_user_custom(values, phrase, indic = " -> ")

        if user_choice == "F":
            return False
        elif user_choice == "R":
            clear_screen()
            test_full_display()
        else:
            clear_screen()
            exec("test_" + fonctions[ord(user_choice)-65] + "()")


def test_init_play():
    """
    Test la fonction init_play()
    """  
    from game.play import init_play

    try :
        assert init_play(2) == {"n" : 2 , "nb_empty_rooms" : 4 , "tiles" : [0,0,0,0]}
        print(init_play(2))
        next("init_play, paramètre taille 2")

        assert init_play(3) == {"n" : 3 , "nb_empty_rooms" : 9 , "tiles" : [0,0,0,0,0,0,0,0,0]}
        print(init_play(3))
        next("init_play, paramètre taille 3")

        assert init_play(4) == {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        print(init_play(4))
        next("init_play,paramètre taille 4")

        assert init_play(5) == {"n" : 5 , "nb_empty_rooms" : 25 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        print(init_play(5))
        next("init_play, paramètre taille 5")

        assert init_play(6) == {"n" : 6 , "nb_empty_rooms" : 36 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        print(init_play(6))
        next("init_play, paramètre taille 6")
        
        succes("init_play")
    except:
        echec("init_play")

def test_check_indice():
    """
    Test la fonction check_indice()
    """
    from tiles.tiles_acces import check_indice

    plateau = {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    try:
        assert check_indice(plateau,0)
        next("check_indice, cellule 0 valide :")

        assert check_indice(plateau,3)
        next("check_indice, cellule 3 valide :")

        assert not check_indice(plateau,-10)
        next("check_indice, cellule  -10 invalide :")

        assert not check_indice(plateau,-1)
        next("check_indice, cellule -1 invalide :")

        assert not check_indice(plateau,4)
        next("check_indice, cellule 4 invalide :")

        assert not check_indice(plateau,10)
        next("check_indice, cellule 10 invalide :")
        
        succes("check_indice")
    except:
        echec("check_indice")

def test_check_room():
    """
    Test la fonction check_room()
    """
    from tiles.tiles_acces import check_room

    plateau = {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    try:  
        assert check_room(plateau, 2, 2)
        next("check_room, paramètre cellule (2;2) valide :")

        assert check_room(plateau, 0, 3)
        next("check_room, paramètre cellule (0;3) valide :")

        assert not check_room(plateau, 0, 31)
        next("check_room, paramètre cellule (0;31) invalide :")

        assert not check_room(plateau, 1, -3)
        next("check_room, paramètre cellule (1;-3) invalide :")

        assert not check_room(plateau, 10, 0)
        next("check_room, paramètre cellule (10;0) invalide :")

        assert not check_room(plateau, -1, -3)
        next("check_room, paramètre cellule (-1;-3) invalide :")

        assert not check_room(plateau, 8, 7)
        next("check_room, paramètre cellule (8;7) invalide :")

        succes("check_room")
    except:
        echec("check_room")

def test_get_value():
    """
    Test la fonction get_value()
    """
    from tiles.tiles_acces import get_value
    from ui.play_display import medium_display

    plateau = {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    medium_display(plateau)
    try:
        assert get_value(plateau, 0, 0) == 6
        next("get_value, cellule (0;0) val 6 :")

        assert get_value(plateau, 2, 3) == 0
        next("get_value, cellule (2;3) val 0 :")

        assert get_value(plateau, 1, 3) == 2
        next("get_value, cellule (1;3) val 2 :")

        assert get_value(plateau, 3, 0) == 1
        next("get_value, cellule (3;0) val 1 :")

        try:
            assert get_value(plateau, 18, 3)
            echec("get_value")
        except:
            next("get_value, cellule (18;3) invalide :")
            try:
                assert get_value(plateau, -1, 3)
                echec("get_value")
            except:
                next("get_value, cellule (-1;3) invalide :")
                succes("get_value")
    except:
        echec("get_value")

def test_set_value():
    """
    Test la fonction set_value()
    """
    from tiles.tiles_acces import set_value
    from ui.play_display import medium_display

    plateau = {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    try:
        assert set_value(plateau, 0, 0, 1) == {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [1,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
        medium_display(plateau)
        next("set_value, cellule (0;0) val 1")
        
        assert set_value(plateau, 1, 2, 0) == {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [1,2,3,2,0,2,0,2,0,2,2,0,1,0,0,0]}
        medium_display(plateau)
        next("set_value, cellule (1;2) val 0")
        
        assert set_value(plateau, 2, 3, 6) == {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [1,2,3,2,0,2,0,2,0,2,2,6,1,0,0,0]}
        medium_display(plateau)
        next("set_value, cellule (2; 3) val 6")
        

        #Doit renvoyer une erreur : Si erreur, on passe à l'assert d'après
        try:
            set_value(plateau, 18, 3,5)
            echec("set_value")
        except:
            #Doit renvoyer une erreur : Si erreur, on affiche succès
            next("set_value, paramètre cellule (18; 3) echec :")
            try:
                set_value(plateau, 1, 3, -5)
                echec("set_value")
            except:
                next("set_value, paramètre cellule (1; 3) val -5 echec :")
                succes("set_value")
    except:
        echec("set_value")

def test_is_room_empty():
    """
    Test la fonction is_room_empty()
    """
    from tiles.tiles_acces import is_room_empty
    from ui.play_display import medium_display

    plateau = {"n" : 4 , "nb_empty_rooms" : 16 , "tiles" : [0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0]}
    medium_display(plateau)
    try:
        assert not is_room_empty(plateau, 0, 1)
        next("is_room_empty, cellule (0; 1) val 2 :")

        assert is_room_empty(plateau, 3, 2) 
        next("is_room_empty, paramètre (1; 3) val 0 :")

        try:
            is_room_empty(plateau, 15, 2)
            echec("is_room_empty")
        except:
            next("is_room_empty, paramètre cellule (15; 2) :")
            try:
                is_room_empty(plateau, -2, 2)
                echec("is_room_empty")
            except:
                next("is_room_empty, paramètre cellule (-2; 2) invalide :")
                succes("is_room_empty")

    except:
        echec("is_room_empty")

def test_get_nb_empty_rooms():
    """
    Test la fonction get_nb_empty_rooms()
    """
    from tiles.tiles_moves import get_nb_empty_rooms
    from ui.play_display import medium_display

    try:
        assert get_nb_empty_rooms({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [6,2,3,2,12,2,6,2,6,2,2,12,1,6,3,1]}) == 0
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [6,2,3,2,12,2,6,2,6,2,2,12,1,6,3,1]})
        next("get_nb_empty_rooms, 0 cellules vides")

        assert get_nb_empty_rooms({"n" : 4 , "nb_empty_rooms" : 4 , "tiles" : [6,2,3,0,12,2,0,2,6,2,0,0,1,6,3,1]}) == 4
        medium_display({"n" : 4 , "nb_empty_rooms" : 4 , "tiles" : [6,2,3,0,12,2,0,2,6,2,0,0,1,6,3,1]})
        next("get_nb_empty_rooms, 4 cellules vides")

        succes("get_nb_empty_rooms")
    except:
        echec("get_nb_empty_rooms")

def test_is_game_over():
    """
    Test la fonction is_game_over()
    """
    from life_cycle.cycle_game import is_game_over
    from ui.play_display import medium_display

    try:
        assert is_game_over({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}) 
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
        next("is_game_over, Game Over")

        assert not is_game_over({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
        next("is_game_over, Game not Over")

        assert not is_game_over({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1]}) == 70
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1]})
        next("is_game_over, Game not Over")


        succes("is_game_over")
    except:
        echec("is_game_over")


def test_get_score():
    """
    Test la fonction get_score()
    """
    from life_cycle.cycle_game import get_score
    from ui.play_display import medium_display

    try:
        assert get_score({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}) == 16
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
        next("get_score, paramètre score de 16")

        assert get_score({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}) == 0
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
        next("get_score, paramètre score de 0")

        assert get_score({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [2,1,5,4,7,8,9,4,1,2,0,1,5,4,8,9]}) == 70
        medium_display({"n" : 4 , "nb_empty_rooms" : 0 , "tiles" : [2,1,5,4,7,8,9,4,1,2,0,1,5,4,8,9]})
        next("get_score, paramètre score de 70")


        succes("get_score")
    except:
        echec("get_score")   

        
def test_full_display():
    """
    Test la fonction full_display()
    """
    from ui.play_display import full_display
    from ui.user_entries import get_user_custom


    plateau = {"n" : 2 , "nb_empty_rooms" : 0 , "tiles" : [2,84,1,0]}
    full_display(plateau)
    
    user_choice = get_user_custom(["o","O","n","N"], "Test concluant ?\n(O) Oui\n(N) Non", indic = " -> ")
    if user_choice == "O":
        plateau = {"n" : 6 , "nb_empty_rooms" : 0 , "tiles" : [1,645,456,2,126,0,162,0,6541,0,4,6,64,4,46,4,572,31,8414,71,14,645,465,57020,572572,789,6451,57200,2,1,56,4,0,410,5,4]}
        full_display(plateau)
    
        user_choice = get_user_custom(["o","O","n","N"], "Test concluant ?\n(O) Oui\n(N) Non", indic = " -> ")
        if user_choice == "O":

            succes("full_display")
        else:
            echec("full_display")
    else:
        echec("full_display")


def next(nom_fonction):
    """
    Affiche la réussite d'un assert
    """
    import time
    from ext_res.termcolor import colored, cprint

    time.sleep(0.5)
    print("Test fonction " + nom_fonction + " réussite")


def succes(nom_fonction):
    """
    Affiche le message de succes en vert
    """
    from ext_res.termcolor import colored, cprint

    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " SUCCES"),"blue","on_green"))

def echec(nom_fonction):
    """
    Affiche le message d'échec en rouge
    """
    from ext_res.termcolor import colored, cprint

    print(colored((">>> [TEST] <<< Test GENERAL de fonction " + nom_fonction + " FAILED"),"white","on_red"))
