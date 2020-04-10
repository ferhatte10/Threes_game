# -*- coding: utf-8 -*-

# QUESTION 1.2 :
def check_indice(board, indice):
    """
    Retourne True si l'indice saisi passé en paramètres (indice) est une case du board passé en paramètres (board), False sinon.
    """
    return indice in range(board["n"])


# QUESTION 1.3 :
def check_room(board, lig, col):
    """
    Retourne True si la cellule passée en paramètres (ligne, colonne) du board passé en paramètres (board) est une cellule valide (=apaprtient au board)
    """
    return check_indice(board, lig) and check_indice(board, col)


# QUESTION 1.4 :
def get_value(board, lig, col):
    """
    Retourne la valeur d'une cellule passée en paramètre (ligne, colonne) d'un board passé en paramètres (board). Retourne une erreur si la cellule n'est pas valide
    """
    if check_room(board, lig, col):
        return board["tiles"][(board["n"] * lig) + col]
    else:
        raise IndexError("La cellule (", lig, col, ") n'est pas valide")  # = out of range


# QUESTION 1.5 :
def set_value(board, lig, col, val):
    """
    Défini une valeur passée en paramètre (val) à une cellule passée en paramètre (ligne, colonne) d'un board passé en paramètres (board)
    """
    if val >= 0:
        # On regarde d'abord si la cellule existe
        if check_room(board, lig, col):

            # On affecte à la cellule la valeur
            board["tiles"][(board["n"] * lig) + col] = val

            # Si la valeur etait !=0 et est remplacée par 0 , on a une case libre en plus
            if get_value(board, lig, col) != 0 and val == 0:
                board["nb_empty_rooms"] += 1

            # Si la valeur etait 0 et est remplacée par != 0 , on a une case libre en moins
            elif get_value(board, lig, col) == 0 and val != 0:
                board["nb_empty_rooms"] -= 1

            # Si la valeur etait 0 et est remplacée par 0 , ou si la valeur etait != 0 et est remplacée par !=0, rien change
            return board

        else:
            # Une erreur est levée si la cellule n'es pas valide
            raise IndexError("La cellule (", lig, col, ") n'est pas valide")  # équivalent à "out of range"
    else:
        # Une erreur est levée si la val est <0
        raise TypeError("La valeur", val, " à affecter n'est pas >= à 0")

        # Nous avons séparé les deux IF pour avoir deux erreurs distinctes


# QUESTION 1.6 :
def is_room_empty(board, lig, col):
    """
    Vérifie si la cellule passée en paramètres (ligne, colonnes) est vide dans le palteau passé en paramètre (board). Une cellule est vide si sa valeur est de 0
    """
    return get_value(board, lig, col) == 0
