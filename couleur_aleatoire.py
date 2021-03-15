from turtle import *
from random import *

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    
    r = random()
    g = random()
    b = random()
    color(r, g, b)
    colormode(255)
    forward(30)
