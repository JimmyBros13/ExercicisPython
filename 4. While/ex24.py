#Exercici 24

contador=0
sumatori=0

while sumatori<50:
    contador+=1
    a=int(input("Dona'm un número:"))
    b=int(input("Dona'm un número:"))
    suma=a+b
    sumatori+=suma
    print("El resultat és",suma)
    if contador==1:
        print("El total acumolat és de",sumatori,"i has realitzat 1 operació")
    else:
        print("El total acumolat és de",sumatori,"i has realitzat",contador,"operacions")
    
print("-- Fi de programa --")