leiviskä = input('Anna leivisköjen määrä: ')
naula = input('Anna naulojen määrä: ')
luoti = input('Anna luotien määrä: ')
leiviskä = float(leiviskä)
naula = float(naula)
luoti = float(luoti)
naula = (luoti * 32)
leiviskä = (naula * 20)
grammamuunnos = (leiviskä)+(naula)+(luoti)
grammat = (grammamuunnos*13.3)
Kilot = int(grammat/1000)
loputgrammat = float(Kilot%1000)
print (f'Paino nykyään olisi {Kilot} kiloa ja {loputgrammat} grammaa.')









