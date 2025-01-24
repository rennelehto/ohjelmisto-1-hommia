luku=input('Syötä luku: ')
luvut=[]
while luku!='':
    luku = input('Syötä luku: ')
    luvut.append(luku)
    if luku=='':
        luvut.sort(reverse=True)
        print(luvut[0:4])
