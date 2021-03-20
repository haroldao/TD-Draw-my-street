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
    facade(x, y_sol, c_facade, 0)
  
    liste=["porte","fenetre","fenetre"]
    shuffle(liste)
    print("Liste >>>>", liste)

    listepos=[x-50, x, x+50]
    # Construit les 3 éléments (1 porte et 2 fenetres)
    for i in range(len(liste)-1):
      if liste[i]=="porte":
          # Choisir entre les deux portes
          b = randint(0, 1)
          if b==1:
              setheading(0)
              porte(listepos[i], y_sol, c_porte)
              del liste[i]
              del listepos[i]
          else:
              porte2(listepos[i], y_sol, c_porte)
              del liste[i]
              del listepos[i]
          print("Liste{2}",liste)
          print("Liste position",listepos)
          
      if liste[i]=="fenetre":
          fenetre(listepos[i], y_sol)
      else:
          print("else")
      

if __name__ == '__main__':
    rdc(0, 0,"red", "green")
    # On ferme la fenêtre s'il y a un clique gauche
    exitonclick()
