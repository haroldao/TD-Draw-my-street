from turtle import *
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    up()
    pencolor("black")
    fillcolor(couleur)
    y = y_sol + niveau * 60

    goto(x, y)
    begin_fill()
    rectangle(x, y, 140, 60)
    end_fill()
    up()
   

if __name__ == '__main__':
    facade(0, 0, "red", 0)
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
