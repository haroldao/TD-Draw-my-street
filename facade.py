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
    if niveau==0:
        pencolor("black")
        fillcolor(couleur)
        begin_fill()
        rectangle(x,y_sol,140,60)
        end_fill()
        right(90)
    else:
        pencolor("black")
        fillcolor(couleur)
        begin_fill()
        rectangle(x,y_sol,140,60)
        end_fill()
        up()
        goto(x,y_sol+60)
        down()
        facade(x,y_sol+60,couleur,niveau-1)
    

if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
