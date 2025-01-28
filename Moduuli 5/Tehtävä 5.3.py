'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
jotka ovat jaollisia vain ykkösellä ja itsellään.'''

import math

luku_str = int(input('Anna kokonaisluku: '))
for kerroin_str in range(2, luku_str, 1):
    if luku_str%kerroin_str==0:
        print('LUKU EI OLE ALKULUKU')
        break
else:
    print('LUKU ON ALKULUKU')
