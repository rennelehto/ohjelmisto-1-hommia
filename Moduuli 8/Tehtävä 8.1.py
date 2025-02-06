import mysql.connector
#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

def kysely(vastaus):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{vastaus}'"
   # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Kentän nimi on {rivi[0]} ja sijaintikunta {rivi[1]}.")

    return



yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)

vastaus = input('Anna ICAO-koodi: ')

kysely(vastaus)









