#Exercici 32

import random

llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
item=random.randint(0,len(llista))
paraula=[]
resposta=""
contador=0

for lletra in llista[item]:
    paraula.append(lletra)
random.shuffle(paraula)
print(paraula)
while resposta!=llista[item]:
    if contador==3:
        print("Limit d'intents superat")
        break
    resposta=input("Digues la paraula: ")
    contador+=1
    if resposta!=llista[item]:
        print("Error!")
    else:
        print("L'has encertat!")
