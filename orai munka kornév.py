kor = int(input('adja meg az életkorát'))
nev = input('neve?')
if kor <= 3:
    print('olvassa a Totyogóknak a kettes számrendszerről könyvet!')
elif kor <=6:
    print('olvasd ezt: Hackeljük meg az óvodát!')
elif kor <=14 or 7:
    print('olvasd ezt: Felhőtechnológia a menzán!')
else:
    print('olvasd ezt: Big data a középiskolában!')
print(f'{nev},{kor}')

