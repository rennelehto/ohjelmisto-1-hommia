

luku_str= input('Syötä luku: ')
luvut=[]
while luku_str!='':
    luvut.append(int(luku_str))
    luku_str = input('Syötä luku: ')

else:
    luvut.sort(reverse=True)
    print(luvut[0:5])
