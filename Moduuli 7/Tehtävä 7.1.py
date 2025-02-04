#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

kuukausi = int(input("Anna kuukauden numero: "))
vuodenajat = ("talvi", "kevät", "kesä", "syys")

if kuukausi in range(1, 13):
        if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
                print(f'Kuu on {vuodenajat[0]}kuukausi.')
        elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
                print(f'Kuu on {vuodenajat[1]}kuukausi.')
        elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
                print(f'Kuu on {vuodenajat[2]}kuukausi.')
        elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
                print(f'Kuu on {vuodenajat[3]}kuukausi.')
else:
        print('Eihän tuo ole kuukausi!')