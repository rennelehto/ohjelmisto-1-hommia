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
    vastaus = print (f'{gallonat} gallonaa on {gallonat*3.785} litraa.')
    return vastaus

bensiini(gallonat)
if gallonat<=0:

    print('Kiitos!')


'''vastaus=gallonat/3.785
if vastaus >= 3.785:
    print('Kiva kiitti.')
    
    print(f'{litrat}')'''


