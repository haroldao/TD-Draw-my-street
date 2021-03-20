from rectangle import rectangle
from turtle import *

def fenetre(x,y):
    print("\n Fenetre file")
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    up()
    goto(x, y)
    down()
    pencolor("black")
    fillcolor("white")
    begin_fill()
    rectangle(x,y,30,30)
    end_fill()


if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
