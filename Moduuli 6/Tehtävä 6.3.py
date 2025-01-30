#Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
# vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
# gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista
# jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

 #   Yksi gallona on 3,785 litraa.


gallonat = float(input('Syötä gallonamäärä: '))
def bensiini(gallonat):
    litrat=gallonat*3.785
    return litrat
while gallonat>=0:
    litrat=bensiini(gallonat)
    print(f'{gallonat} gallonaa on {litrat} litraa.')
    gallonat = float(input('Syötä gallonamäärä: '))
if gallonat<=0:
    print('Kiitos!')