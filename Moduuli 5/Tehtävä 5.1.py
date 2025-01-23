'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

import random
import math




'''noppaluku=[]
nopat=(input('Kuinka montaa nopaa heitetään? '))
noppa=(random.randint(1, 6))

while nopat!='':
    (noppaluku.append(nopat))
    for 
'''
tulokset=[]

heitot = int(input('Kuinka montaa nopaa heitetään? '))
while heitot>=1:

    noppa = (random.randint(1, 6))
    tulokset.append(noppa)
    if heitot>1:
        heitot=heitot+1
        print(f'{tulokset}')
        break

'''if noppa > 1:
    noppa = noppa + noppa
for vastaus in tulokset:
    vastaus=noppa
    print(f'Noppien silmälukujen summa on {vastaus}')

else:
    print('Vituiks meni.')


'''