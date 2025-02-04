import random
arvotut=set()

while len(arvotut) < 4:
    uusiluku = random.randint(1, 9)
    arvotut.add(uusiluku)

    for i in arvotut:
        print(i)
print (arvotut)