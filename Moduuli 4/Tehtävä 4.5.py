'''Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen
ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus
ja salasana kysytään uudelleen. Tätä jatketaan kunnes
kirjautumistiedot ovat oikein tai väärät tiedot on syötetty
 viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa
  ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus
  on python ja salasana rules).'''



kerrat=0
while kerrat<=5:
    käyttis = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if käyttis!='python' or salasana!='rules':
        print('Pääsy evätty')
        kerrat = kerrat + 1
    else:
        print('Tervetuloa')
        break
