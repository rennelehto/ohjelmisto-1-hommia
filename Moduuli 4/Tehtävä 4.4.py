'''Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
lukuaan arvauskertojen välissä.'''

import random
vastaus=(random.randint(1, 10))


while True:
    arvaus=int(input('Anna luku 1-10: '))
    if arvaus==vastaus:
        print('Arvaus on oikein!')
        break
    if arvaus>vastaus:
        print('Arvaus on liian suuri!')
    if arvaus<vastaus:
        print('Arvaus on liian pieni!')

