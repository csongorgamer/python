nev = input("mi a neved?")
Bogyó = int(input("kérem adja meg mennyi bogyót gyüjtött"))

if Bogyó < 10 :
    minősítés = 'zsenge'
elif Bogyó > 20:
    minősítés = 'nagy koponya'
else: 
    minősítés ='gyűjtögető'
print(f'{nev} egy {minősítés} .')