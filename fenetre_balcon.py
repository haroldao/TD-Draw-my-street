from turtle import *
from rectangle import rectangle
from trait import trait


def fenetre_balcon(x, y):
    print("\nFenetre Balcon file")
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    up()
    goto(x-15, y)
    down()
    pencolor("black")
    fillcolor("white")
    begin_fill()
    rectangle(x-15, y, 30, 50)
    end_fill()
    up()
    pencolor("black")
    left(90)

    trait((xcor() - 4.2), ycor(),
          (xcor() - 4.2), ycor())

    trait(xcor(), ycor(),
          xcor(), (ycor() + 25))

    # For loop pour les barreaux
    for i in range(9):

        trait((xcor() + 4.2), ycor() - 25,
              (xcor() + 4.2), ycor())

    right(90)
    rectangle(x - 15, y, 38.4, 25)


if __name__ == '__main__':
    fenetre_balcon(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
