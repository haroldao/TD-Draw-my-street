from turtle import *

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    up()
    setheading(0)
    goto(x,y)
    left(180)
    forward(30//2)
    left(180)
    down()
    pencolor("black")
    fillcolor(couleur)
    begin_fill()
    forward(30)
    left(90)
    forward(40)
    circle(15,180)
    forward(40)
    end_fill()
    

if __name__ == '__main__':
    porte2(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
