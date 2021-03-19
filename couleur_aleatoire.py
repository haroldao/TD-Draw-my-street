from random import sample

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    hexa = "0123456789ABCDEF"
    return('#' + ''.join(sample(hexa, 6)))
