#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
# ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
# yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math




def pizzapie(ekapiz, tokapiz):


    ekapiz=Yks/Halk
    tokapiz=Yks2/Halk2
    if ekapiz>tokapiz:
        print('Ensimmäinen pizza on halvempi')
    else:
        print('Toinen Pizza on halvempi')
    return
Halk = float(input('Anna pizzan halkaisija: '))
Yks = float(input('Anna pizzan hinta: '))
Halk2 = float(input('Anna toisen pizzan halkaisija: '))
Yks2 = float(input('Anna toisen pizzan hinta: '))

pizzapie(ekapiz, tokapiz)
print('Hyvää ruokahalua!')
