kanta_str = input('Anna suorakulmoin kanta: ')
korkeus_str = input ('Anna suorakulmion korkeus: ')

kanta = float(kanta_str)
korkeus = float(korkeus_str)

piiri = float(kanta)*2+(korkeus)*2
pinta = float(kanta)*(korkeus)

print (f'Suorakaiteen piiri on {piiri} + ja pinta-ala on {pinta}')

