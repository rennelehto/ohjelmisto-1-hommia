import mysql.connector

#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

def kysely(maakoodi):
    sql = f"select type as 'Kentän tyyppi', count(type) as 'Kenttien määrä' from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' group by type;"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Kentän tyyppiä {rivi[0]} ja niitä on  {rivi[1]} kappaletta.")
    return

yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)
maakoodi = input('Anna maakoodi: ')
kysely(maakoodi)