#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko
# tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma
# luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa
# järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.



nimet = set()
def pööt():
    nimi = input("Kirjoita nimi: ")
    if nimi !='':
        if nimi in nimet:
                print('Aiemmin syötetty.')
        else:
            nimet.add(nimi)
            print('Uusi nimi')
    return

pööt()

'''for n in nimet:
    print(nimet)'''