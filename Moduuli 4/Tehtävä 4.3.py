'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.'''

import math

pieni=suuri=0
while True:
    luku = input('Syötä luku: ')
    if luku=='':
        break
    if pieni==0:
        pieni=luku
    if suuri==0:
        suuri=luku
    if pieni>luku:
        pieni=luku
    if suuri<luku:
        suuri=luku

print(f'Pienin luku on {pieni} ja suurin {suuri}.')