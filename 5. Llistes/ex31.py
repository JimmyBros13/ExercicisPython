#Exercici 31

import random

llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
item=random.randint(0,len(llista))

paraula=input("Introdueix la paraula secreta: ")
while paraula!=llista[item]:
    paraula=input("Introdueix la paraula secreta: ")
print("Has encertat!")