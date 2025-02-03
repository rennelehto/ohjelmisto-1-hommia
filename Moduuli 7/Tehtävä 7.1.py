#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.




kuukausi = (input("Anna kuukauden numero: "))
vuodenajat = ("talvi", "kevät", "kesä", "syksy")
if kuukausi == 12 or 1 or 2:
        print(f'Kuu on {vuodenajat[0]}kuukausi.')
if kuukausi == 3 or 4 or 5:
        print(f'Kuu on {vuodenajat[1]}kuukausi.')
if kuukausi == 6 or 7 or 8:
        print(f'Kuu on {vuodenajat[2]}kuukausi.')
if kuukausi == 9 or 10 or 11:
        print(f'Kuu on {vuodenajat[3]}kuukausi.')
else:
        print('Eihän tuo ole kuukausi!')







'''if kuukausi == 12 or 1 or 2:
    kuu=vuodenajat[0]
elif kuukausi == 3 or 4 or 5:
    kuu=vuodenajat[1]
elif kuukausi == 6 or 7 or 8:
    kuu=vuodenajat[2]
elif kuukausi == 9 or 10 or 11:
    kuu=vuodenajat[3]
    print(f'Kuu on {kuu}kuukausi.')'''

   # else:
      #  print('Eihän tuo ole kuukausi!')


   # return kuu


#kaudet()
#kk=kaudet()







