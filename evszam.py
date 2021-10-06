evszam = int (input('adjon meg egy számot ne kelljen már megszurjalak tesomsz'))
if evszam%4 == 0 and evszam%100 != 0:
    print('Szökőév')
else:
    print('Nem szökőév')