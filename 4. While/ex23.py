#Exercici 23

contador=0
sumatori=0
resposta=""

while resposta!="n":
    contador+=1
    a=int(input("Dona'm un número:"))
    b=int(input("Dona'm un número:"))
    suma=a+b
    sumatori+=suma
    print("El resultat és",suma)
    resposta=input("Vols seguir? (s/n) ").lower()

print("RESUM:")
print("Has repetit el procés",contador,"vegades i el total sumat és",sumatori)