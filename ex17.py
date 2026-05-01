#Exercici 17

patron="*****"

for i in range(len(patron),-1,-1):
    print(patron[i:])
for i in range(len(patron)-1,-1,-1):
    print(patron[:i])