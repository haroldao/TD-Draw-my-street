from facade import facade
from random import shuffle, randint
from porte import porte
from porte2 import porte2
from fenetre import fenetre
from turtle import *

def rdc(x, y_sol, c_facade, c_porte):
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
    facade(x,y_sol, c_facade, 0)

    liste=["porte","fenetre","fenetre"]
    shuffle(liste)
    listepos=[x-50,x,x+50]
    a=randint(0,2)   
    if liste[a]=="porte":
        b=randint(0,1)
        if b==1:
            setheading(0)
            porte(listepos[a],0,c_porte)
            del liste[a]
            del listepos[a]
        else:
            porte2(listepos[a],0,c_porte)
            del liste[a]
            del listepos[a]
        print(liste)
        print(listepos)
            
    
    c=randint(0,1)
    
    if liste[c]=="fenetre":
        fenetre(listepos[c],20)
    else:
        b=randint(0,1)
        if b==1:
            setheading(0)
            porte(listepos[c],0,c_porte)
            del liste[c]
            del listepos[c]

        else:
            porte2(listepos[c],0,c_porte)
            del liste[c]
            del listepos[c]
        print(liste)
        print(listepos)
    
    if liste[0]=="fenetre":
        fenetre(listepos[0],20)
    else:
        b=randint(0,1)
        if b==1:
            setheading(0)
            porte(listepos[0],0,c_porte)
        else:
            porte2(listepos[0],0,c_porte)
        print(liste)
        print(listepos)
    # Construit les 3 éléments (1 porte et 2 fenetres)

    

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
