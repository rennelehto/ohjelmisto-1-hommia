import mysql.connector
from geopy import distance

#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.

def kent(k1):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{k1}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Toisen kentän koordinaatit ovat {rivi[0]}, {rivi[1]}.")
    return tulos

def kent(k2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{k2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Toisen kentän koordinaatit ovat {rivi[0]}, {rivi[1]}.")
    return tulos

yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)

k1=input('Anna ensimmäisen kentän ICAO-koodi: ')
eka=kent(k1)
k2=input('Anna toisen kentän ICAO-koodi: ')
toka=kent(k2)

print(f'Kenttien välimatka on {distance.distance (eka, toka).km:.3f} kilometriä')