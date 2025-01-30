'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.'''

import random

def noppa():
    perse = print(f'{(random.randint(1, 6))}')
    return perse

print('Heitetään noppaa...')
pylly = noppa()
if pylly != 6:
    noppa()
print('Hyvä peli!')