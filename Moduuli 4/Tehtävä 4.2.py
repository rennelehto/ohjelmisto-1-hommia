'''Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm'''
import math

tuuma_str=input('Syötä tuumamäärä: ')
tuuma=float(tuuma_str)

while tuuma>0:
    print(f'{tuuma} tuumaa on {tuuma*2.54} senttimetriä')
    if tuuma<0:
        break

