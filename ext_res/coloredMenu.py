import sys
from os import path, system

sys.path.append("../")
from ext_res.getkey import *
from ui.play_display import clear_screen, printc


def afficheMenu(menu, i, indic):
    """
    Fonction qui affiche un menu. La cellule active est mise en surbrillance, après l'indicateur (indic) et est définie par l'indice i
    """
    # La largeur du menu
    taille = 40

    # On parcours chaque element du menu
    for j in range(len(menu)):
        line = ""

        # Si j=0, il s'agit du nom du menu en haut, ce n'est pas une option
        if j == 0:
            line = "        ╔═════════[\033[1m" + menu[j].center(taille - 21) + "\033[0m]═════════╗"

        # Ici, l'element j est actif, il doit donc être mit en surbrillance
        elif j == i:
            # On applique une couleur en fonction des options :
            if menu[j] in ["(F) Fermer", "(R) Retour", "(N) Non"]:
                # Rouge si non, fermer ou retour
                color = "\033[0;37;41m"
            elif menu[j] == "(O) Oui":
                # Vert si oui
                color = "\033[0;37;42m"
            else:
                # Blanc sinon
                color = "\033[0;30;47m"

            # On ajoute à la ligne avec l'indicateur et la couleur voulu
            line = " " * 14 + "║" + indic + color + menu[j] + "\033[0m"

            # On ajoute des espaces jusqu'a obtenir une grande taille
            while len(line) < taille + 28:
                line += " "
            # A la fin de la ligne on met une barre verticale
            line += "║"

        # Ici, on affiche les autres éléments
        # Ligne vide, c'est donbc une bordure
        elif menu[j] == "":
            line += "╟"

            while len(line) < taille:  # +4:
                line += "─"
            line += "╢"
        # les autres lignes
        else:

            line = "║ " + menu[j]  # + "\033[0m"

            while len(line) < taille:  # +4:
                line += " "
            line += "║"

        printc(line + "\033[0m")
    # On afiche la bordure inferieur
    printc("╚" + "═" * (taille - 1) + "╝    ")


def coloredMenu(menu, values, indic="", indice=1, beforeMessage=None):
    """
    Fonction qui gére les déplacement au sein du menu
    """
    user_entrie = ""
    i = 1
    # Tant que le choix n'est pas entrer ou dans valeur
    while user_entrie != "ENTER" and not user_entrie in values:
        # SI le beforeMessage existe, on l'affiche avant chaque menu
        if beforeMessage is not None:
            printc(beforeMessage)

        # On affiche le menu
        afficheMenu(menu, i, indic)
        user_entrie = getkey().upper()

        # Si on est tout en haut, on peut descendre
        # Si on est tout en bas, on peut monter
        # Si on est tout en haut et qu'on monte, on atterit tout en bas
        # Si on est tout en bas et qu'on descend, on atterit tout en haut

        if user_entrie == "H" and i > 1:
            i -= 1
            if menu[i] == "":
                i -= 1
        elif user_entrie == "H" and i == 1:
            i = len(menu) - 1


        elif user_entrie == "B" and i < len(menu) - 1:
            i += 1
            if menu[i] == "":
                i += 1
        elif user_entrie == "B" and i == len(menu) - 1:
            i = 1
        clear_screen()

    if user_entrie in values:
        return user_entrie.upper()
    return (menu[i][indice])
