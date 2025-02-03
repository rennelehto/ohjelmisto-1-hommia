#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.



vuodenajat = ("talvi", "kevät", "kesä", "syksy")
def kaudet():

    if kuukausi == 12 or 1 or 2:
        kuu=vuodenajat[0]
    if kuukausi == 3 or 4 or 5:
        kuu=vuodenajat[1]
    if kuukausi == 6 or 7 or 8:
        kuu=vuodenajat[2]
    if kuukausi == 9 or 10 or 11:
        kuu=vuodenajat[3]
    return kuu

kuukausi = int(input("Anna kuukauden numero: "))
kaudet()
kk=kaudet()
print(f'Kuu on {kk}kuukausi.')






