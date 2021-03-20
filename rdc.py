from facade import facade
from random import shuffle, randint
from porte import porte
from porte2 import porte2
from fenetre import fenetre
from turtle import *


def rdc(x, y_sol, c_facade, c_porte):
    print("\nRDC File")
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    facade(x, y_sol, c_facade, 0)
    
    i = randint(1, 3)
    print("i", i)
    if i == 1:
        fenetre(x-25, 10)
        up()

        pendown()
        fenetre(x, 10)
        up()

        down()
        porte(x+25, 0, "red")
        up()

    elif i == 2:
        fenetre(x-25, 10)
        up()

        down()
        porte(x, 0, "red")
        up()

        down()
        fenetre(x+25, 10)
        up()
    elif i == 3:
        porte(x-40, 0, "red")
        up()

        down()
        fenetre(x+10, 10)
        up()

        down()
        fenetre(x+50, 10)
        up()

if __name__ == '__main__':
    rdc(0, 0, "red", "green")
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
