import random

nev = input('Kéremadjameg a nevét!')
szam2 = int(input('adjon meg egy számot'))
szam1 = (random.randint(10,50))
while szam1 % 2 == 1:
    szam1 = (random.randint(10,50))
print(szam1)
print(szam2)
print(nev)
SZAM3 = 5
#halmaz
szamok2 = {23}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(SZAM3)
print(szamok2)
#lista
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)

print(szamok)

if szam1 % 2 == 0:
    print('páros')
else:
    print('páratlan') 

my_list = [1,2,3,4,5,"abc","def"]
with open ('csongor11.txt', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)

f = open("csongor11.txt")
tartalom = f.read()
print(tartalom)
f.close()

gyumolcsok = ["eper","alma","ananász"]
print(f' a gyumolcsok lista ezeket tartalmazza: {gyumolcsok}')
for (i,y) in enumerate (gyumolcsok):
    print(i,y)

