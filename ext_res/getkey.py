import sys
from os import path, name

sys.path.append("../")


def getkey():
    """
    Renvoie la lettre saisie par l'utilisateur :
    "UP" pour flèche du haut
    "DOWN" pour flèche du bas
    "LEFT" pour flèche de gauche
    "RIGHT" pour flèche de droite
    """
    # Pour windows
    if name == "nt":
        # On importe la bibliotheque windows
        import msvcrt

        # On récupère le touche pressée par l'utilisateur, quon met en minuscule et on stoque dans une variable
        val = ord(msvcrt.getch().lower())

        # Les flèches renvoient deux valeurs, 0 puis une autre, Si la valeur est 0:
        if val == 0:
            # On restoque la touche pressées par l'utilisateur
            val = ord(msvcrt.getch())

        return ordToChr(val)

        # Pour mac et linux
    else:
        # On importe le module getkey téléchargé sur intenet
        import sys
        sys.path.append("../")
        from ext_res.getkey1.getkey.__init__ import getkey, keys

        # Les flèches renvoient "keys.UP" (ect) : On défini un dictionnaire pour convertir ça en code, pour uniformiser linux et winbdows
        controls = {keys.UP: 72, keys.DOWN: 80, keys.LEFT: 75, keys.RIGHT: 77, keys.ESCAPE: 27, keys.ENTER: 13}

        # On récupère la touche pressée par l'utilisateur
        val = getkey()

        # Si la touche est dans la liste, on renvoie la valeur correspondante à la clé
        if val in list(controls):
            return ordToChr(controls[val])

            # Sinon on renvoie la valeur
        return ordToChr(ord(val))


def ordToChr(ordChr):
    """
    13 : ENTER 
    27 : echap
    72 : Fleche haut
    75 : Fleche gauche
    77 : Fleche droite
    80 : Fleche bas
    
    113 : Q
    122 : Z
    115 : S
    D inutile car le d de HBGD = le d de ZQSD

    38 : &  : 1 (quand majuscule inactive)
    233 : é : 2 (quand majuscule inactive)
    34 : "  : 3 (quand majuscule inactive)
    39 : '  : 4 (quand majuscule inactive)
    40 : (  : 5 (quand majuscule inactive)

    339 - 253 : œ - œ - touche ²


    """
    # Défini les lettres prises par cycle_play (seulement h/b/g/d et m)
    # Permet une uniformisation pour tous les systèmes d'OS
    specialCars = {113: "g", 122: "h", 115: "b", 13: "ENTER", 27: "m", 72: "h", 75: "g", 77: "d", 80: "b",
                   38: "1", 233: "2", 34: "3", 39: "4", 40: "5", 339: "CONSOLE", 253: "CONSOLE"}

    # si l'ord est dans la liste:
    if ordChr in list(specialCars):
        # On retourne la valeur correspondant à la clé
        return specialCars[ordChr]
    return chr(ordChr)
