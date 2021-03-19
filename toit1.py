from turtle import *

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    up()
    goto(x,y_sol+(60*niveau))
    left(180)
    forward(140//2+10)
    left(180)
    down()
    color("black")
    begin_fill()
    forward(160)
    left(180-20)
    forward(85)
    left(40)
    forward(85)
    end_fill()

if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
