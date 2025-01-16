nimi = 'Meikä'
print ('Moi ' + nimi + ', mitä kuuluu?')
print(f'Moi {nimi}, kuinkas nyt menee?')

#käyttäjän syötteen lukeminen
#huom: input lukee kaikki syötteet ainamerkkijonoina
lukuA_str = input('Anna kokonaisluku: ')
#muunnetaan merkkijono kokonaisluvuksi
lukuA = int(lukuA_str)
#luen käyttäjän syötteen lukuna,
#huom: +input
lukuB = int(input('Anna toinen luku: '))
summa = lukuA + lukuB
print (f'Lukujesi summa: = {summa}')

