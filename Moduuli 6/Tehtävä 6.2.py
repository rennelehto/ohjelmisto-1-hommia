#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä
# tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
# kunnes saadaan nopan maksimisilmäluku, joka kysytään
# käyttäjältä ohjelman suorituksen alussa.

import random
tahkot=int(input('Anna noppien tahkojen määrä: '))
def noppa(tahkot):
    luku = int(random.randint(1, tahkot))
    print(f'{luku}')

    return
luku2=noppa(tahkot)
while luku2!=noppa(tahkot):
    noppa(tahkot)
else:
    print(tahkot)
print('Hyvä peli!')

