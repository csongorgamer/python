import random
egyik = random.randint(1,10)
másik = random.randint(1,10)
összeg = egyik+másik
print(összeg)
if összeg%2 ==0: 
    print('páros')
    if összeg%3 ==0:
        print('oszthato 3-mal')
    else:
        print('nem oszthato 3-mal')
else:
    print('páratlan')
    
 
