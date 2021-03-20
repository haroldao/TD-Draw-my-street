from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    print("\n Etage file")
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    y = y_sol + niveau * 60
    # dessin des murs
    facade(x, y_sol, couleur, niveau)
    # dessin des 3 Eléments
    for i in range(3):
      i = randint(1, 2)
      print("i", i)
      if i == 1:
        fenetre(x, y)
      else:
        fenetre_balcon(x, y)


if __name__ == '__main__':
    etage(0, 0, "red", 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()