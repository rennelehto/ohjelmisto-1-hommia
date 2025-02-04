#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä
# valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä
# lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
# ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina
# siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman
# yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

asemat={'333':'sss','444':'rrr'}

def lööps():
    toiminto = input('Kirjoita [S] syöttääksesi uuden lentoaseman, [H] hakeaksesi jo syötetyn aseman tietoja tai [X] lopettaaksesi: ')
    if toiminto != 'x' or toiminto != 'X':
        if toiminto=='s' or toiminto=='S':
                uusinimi = input('Syötä aseman nimi: ')
                uusikoodi = input('Syötä aseman ICAO-koodi: ')
                asemat[uusikoodi] = uusinimi
                print(f'Lisätiin asema {uusinimi} ICAO-koodi {uusikoodi}.')
        elif toiminto=='h' or toiminto=='H':
            koodi=input('Syötä aseman ICAO-koodi: ')
            if koodi in asemat:
                print(f'Aseman {koodi} nimi on {asemat[koodi]}.')
            else:
                print('Koodia ei löydy tietokannasta.')
    return toiminto

while lööps()!= 'x':
    lööps()
print('Heihei!')