'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

#miten for-rakenne mahtuu tähän?????

import random
import math

kerrat=int(input('Kuinka montaa noppaa heitetään? '))
kierros=0
tulokset=[]
summa=0
while kerrat>kierros:
    luku=(random.randint(1, 6))
    tulokset.append(luku)
    kierros=kierros+1
    summa = summa + luku
print(f'{summa}')