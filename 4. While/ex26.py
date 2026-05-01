#Exercici 26

import random

n=0
contador=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0

while contador<100:
    n=random.randint(1,6)
    contador+=1
    if n==1:
        c1+=1
    elif n==2:
        c2+=1
    elif n==3:
        c3+=1
    elif n==4:
        c4+=1
    elif n==5:
        c5+=1
    elif n==6:
        c6+=1
    
print("1:",c1)
print("2:",c2)
print("3:",c3)
print("4:",c4)
print("5:",c5)
print("6:",c6)