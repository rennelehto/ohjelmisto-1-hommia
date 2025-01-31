'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.'''

import random

def noppa():
    y = print(f'{(random.randint(1, 6))}')
    return y

print('Heitetään noppaa...')
p = noppa()
if p != 6:
    noppa()
else:
    print(p)
print('Hyvä peli!')