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

asemat={'333':'sss'}

def lööps():
    toiminto = input('Kirjoita [s] syöttääksesi uuden lentoaseman, [h] hakeaksesi jo syötetyn aseman tietoja tai [x] lopettaaksesi: ')
    while toiminto != 'x':
        if toiminto=='s':
                uusinimi = input('Syötä aseman nimi: ')
                uusikoodi = input('Syötä aseman ICAO-koodi: ')
                asemat[uusikoodi] = uusinimi
        elif toiminto=='h':
            koodi=input('Syötä aseman ICAO-koodi: ')
            if koodi in asemat:
                print(f'Aseman {koodi} nimi on {asemat[koodi]}.')
            else:
                print('Koodia ei löydy tietokannasta.')
    return

print('Käynnistetään..')
lööps()
print('Kiitos!')

