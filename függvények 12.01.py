def alahuzas(jel):
    for _ in range(10):
        print(jel,end='')
    print('')
    

print('Ez egy fontos figyelmeztetés!')
alahuzas('-')
print('Minden sora nagyon fontos!')
alahuzas('*')
print('Komolyan!')
alahuzas('~')

def pluszkettő(szám):
    print(szám+2)

print('5+2= ', end='')
pluszkettő(5)
print('4+2= ', end='')
pluszkettő(4)


def pluszkettő(szám):
    return szám+2

print('5+2= ', pluszkettő(5))
print('4+2= ', pluszkettő(4))



#def megítél(mondat):
    #if len(mondat) > 0:
       # if mondat [-1] != '!' and mondat [-1] != '?' and mondat [-1]  != '.':
        #    print('Hát ejnye!')
        #else:
         #   print('Gyönyörű mondat!')


#mondat = None
#while mondat != '':
 #   mondat = input('Írj egy mondatot!')
  #  megítél(mondat)


def pozneg(szám):
    if szám > 0:
       print(szám, 'pozitív. ')
    elif szám < 0:
        print(szám, 'pozitív.')
    else:
        print('A szám nulla.')


szám = None
while szám != '':
    szám = input('Írj ide egy számot! ')
    if szám != '':
        szám = float(szám)
        pozneg(szám)