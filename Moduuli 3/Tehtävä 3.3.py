import math

sp=input('Anna biologinen sukupuoli (m tai n): ')
arvo_str=float(input('Anna hemoglobiiniarvosi (g/l): '))
arvo=float(arvo_str)

if sp=='n' and arvo>=117 and arvo<=175:
    print('Hemoglobiiniarvosi on normaali.')
elif sp=='n' and arvo<=117:
    print('Hemoglobiiniarvosi on matala.')
elif sp=='n' and arvo>=175:
    print('Hemoglobiiniarvosi on korkea.')

if sp=='m' and arvo>=134 and arvo<=195:
    print('Hemoglobiiniarvosi on normaali.')
elif sp=='m' and arvo<=134:
    print('Hemoglobiiniarvosi on matala.')
elif sp=='m' and arvo>=195:
    print('Hemoglobiiniarvosi on korkea.')