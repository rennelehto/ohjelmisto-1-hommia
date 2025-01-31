#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen
# kuin parametrina saatu lista paitsi että siitä on karsittu
# pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen
# sekä alkuperäisen että karsitun listan.

def poistolista(numero):
    parilliset = []
    for luku in numero:
        if luku%2==0:
            parilliset.append(luku)
    return parilliset

numerot=[1,3,5,65,76,34,34,56,65,32]

pois=poistolista(numerot)
print(numerot)
print(pois)
