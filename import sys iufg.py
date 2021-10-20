import sys 
oldout = sys.stdout 
print('képernyőre ír.')
wr = open('test2.txt', 'w')
sys.stdout = wr
print('fájlba ít.')
wr.close()
sys.stdout = oldout
print('képernyőre ír ismét.')