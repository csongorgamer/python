egyik = int(input("addjon meg egy számot"))
masik = int(input("addjon meg egy másik számot"))
jel = input("addjon meg egy műveleti jelet")

#print("A művelet eredménye:',end='' )
print('A művelet eredménye:',end='' )
if jel == '+':
    print(egyik+masik)
elif jel == '-':
    print(egyik-masik)
elif jel == '%':
    print(egyik % masik)
elif jel == '>>':
    print(egyik >> masik)