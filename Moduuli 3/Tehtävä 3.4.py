#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat
# karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

import math
vuosi_str=int(input('Anna vuosiluku: '))
vuosi=float(vuosi_str)
nelj=vuosi%4
sata=vuosi%400
sata1=vuosi%100

if sata==0 and sata1==0:
    print('Vuosi on karkausvuosi')
elif nelj==0:
    print('Vuosi on karkausvuosi')
else:
    print('Vuosi ei ole karkausvuosi.')