#2-100 primszám
"""
for x in range(101,1,-2):
    print(x)
"""
for x in range(2,101):
    for osztó in range(2,x//2+1):# IGY 4 NEM LESZ PRÍM
        print (x,osztó)
        if (x % osztÓ) ==0:
            break
    else:
        print(x, 'prím')