#Exercici 25

import random

n=random.randint(0,1000)
contador=1
#print(n)
a=int(input("Encerta el número [0-1000]:"))

while a!=n:
    contador+=1
    if a<n:
        print("El nombre introduït és menor")
    else:
        print("El nombre introduït és major")
    a=int(input("Encerta el número [0-1000]"))

print("Has encertat el número",n,"en",contador,"intents!")
