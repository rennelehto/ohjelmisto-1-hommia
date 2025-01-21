#Kirjoita ohjelma, joka kysyy kalastajalta kuhan
# pituuden senttimetreinä. Jos kuha on alamittainen,
# ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
# samalla käyttäjälle, montako senttiä alimmasta sallitusta
# pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on
# alle 37 cm.

import math
pituus_str=input('Anna kuhan pituus senttimetreinä: ')
pituus= float(pituus_str)
määrä=37-pituus
if pituus < 37:
    print (f'Kuha on {määrä} cm alimittainen, laske se takaisin veteen.')
else:
    print ('Hyvä saalis!')

