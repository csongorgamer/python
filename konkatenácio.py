gyumolcs = 'banán'
m = gyumolcs [1]
print(m)

gyumolcs = ('banán')
lista = list(enumerate(gyumolcs))
print(lista)
primek = [2,3,5,7,11,13,17,19,23,29,31]
p4 = primek[4]
print(p4)

hossz = len(gyumolcs)
print(hossz)
sz= len(gyumolcs)
utolso = gyumolcs[sz-1]
print(utolso)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[1]
    print(karakter)
    i += 1
for c in gyumolcs:
    print(c)

       
    nev = 'Alice'
    kor = 10
    s2 = 'a nevem {1},és {0}éves vagyok.'.format(kor, nev) 
    print(s2)