'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''


import random
import math


kerrat=int(input('Kuinka montaa noppaa heitetään? '))
tulokset=[]
for luku in range(0, kerrat):
    luku = (random.randint(1, 6))
    tulokset.append(luku)
else:
    print(f'{tulokset}')