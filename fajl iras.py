from os import close, write


wr = open('csongor.txt','w')
wr = write('varhegyi csongor')
wr = close()


wr = open('csongor.txt','.a')
wr.write() 