from turtle import *

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    pensize(4)
    up()
    goto(x,y_sol+(60*niveau))
    forward(140//2+10)
    down()
    color("black")
    begin_fill()
    forward(160)
    forward(85)
    end_fill()

if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
