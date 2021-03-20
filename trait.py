from turtle import * 

def trait(x1,y1,x2,y2):
    print("\nTrait file")
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)

if __name__ == '__main__':
    trait(0,0,100,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
