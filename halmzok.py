 #) hozzon létre egy halmazt és törölje

# másolja át a halmaz értékkészletét egy másik halmazba

#) hozzon létre két halmazt és képezze a két halmaz különbségét (difference()metódus)

#) hozzon létre két halmazt és képezzen egy olyan halmazt, amely mind a két halmaz ban megtalálható elemeket tartalmazza difference_update()

#) hozzon létre két halmazt és használja intersection () metódust. Írja le mit kapott végeredményként!

#) hozzon létre két halmazt és képezzen egy olyan halmazt, amely azokat az elemeket tartalmazza, amelyek nem szerepelnek mindkettőben. intersection_update()

#) hozzon létre két halmazt és használja az isdisjoint() metódust. Írja le mikor kaphatunk True és False kimeneti értéket.

#) mire használható issubset() metódus? Írjon rá példát!

#) mire használható issuperset() metódus? Írjon rá példát!

#) mire használható symmetric_difference() metódus? Írjon rá példát!

#) keressen még további három metódus az interneten, próbálja ki írja le milyen műveletet hajtanak végre egy halmazon!
A = set(['alma','banán','dinnye']) 
A.add('körte') 
B = set(['alma','kiwi','szőlő'])	
C1 = A.difference(B)
C2 = B.difference(A)
print(C1,C2)

A = set(['alma','banán','dinnye']) 
A.add('körte') 
A.discard('alma')
print(A)

A = set(['alma','banán','dinnye']) 
A.add('körte') 
B = set(['alma','kiwi','szőlő'])	
C1 = A.difference(B)
C2 = B.difference(A)
print(C1,C2)

A = set(['alma','banán','dinnye']) 
A.add('körte') 
B = set(['alma','kiwi','szőlő'])	
C1 = A.difference(B)
C2 = B.difference(A)
print(C1,C2)

A = set(['alma','banán','dinnye']) 
A.add('körte') 
B = set(['alma','kiwi','szőlő'])	
C1 = A.difference(B)
C2 = B.difference(A)
print(C1,C2)

A = set(['alma','banán','dinnye']) 
A.add('körte') 
B = set(['alma','kiwi','szőlő'])	
C1 = A.difference(B)
C2 = B.difference(A)
print(C1,C2)
