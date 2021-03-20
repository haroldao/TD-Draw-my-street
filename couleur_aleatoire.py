from random import sample

def couleur_aleatoire():
    print("\nRandom Color file")
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    hexa = "ABCDEF0123456789"
    return('#' + ''.join(sample(hexa, 6)))
