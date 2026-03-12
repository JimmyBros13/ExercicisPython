#Exercici 14
num=50
contadorpar=0
contadorimp=0

for i in range(0,num):
    if i%2==0:
        contadorpar+=1
    else:
        contadorimp+=1
print("Total de parells:",contadorpar)
print("Total d'imparells:",contadorimp)