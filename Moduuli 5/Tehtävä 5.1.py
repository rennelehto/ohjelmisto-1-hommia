'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

import random
import math

tulokset=[]

heitot = int(input('Kuinka montaa nopaa heitetään? '))
while heitot>=1:

    noppa = (random.randint(1, 6))
    tulokset.append(noppa)
    if heitot>1:
        heitot=heitot+1
        print(f'{tulokset}')
        break