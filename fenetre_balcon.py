from turtle import *
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
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
    goto(x,y)
    left(180)
    forward(30//2)
    left(180)
    down()
    pencolor("black")
    fillcolor("white")
    begin_fill()
    rectangle(x,y,30,50)
    right(90)
    forward(-25)
    left(90)
    trait(xcor()-5,ycor(),xcor()+35,ycor())
    up()
    right(90)
    forward(25)
    right(90)
    trait(xcor(),ycor(),xcor()-40,ycor())
    for i in range(9):
        trait(xcor(),ycor(),xcor(),ycor()+25)
        up()
        goto(xcor()+45//9,ycor()-25)
    end_fill()



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
