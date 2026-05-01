#Exercici 20

n=int(input("Dona'm un número enter: "))

contparells=0 #si seguim el resultat de l'exercici on conta 4 parells en comptes de 5, contparells=-1
contimparells=0 #si volem contar el "-99", contimparells=1
contpositius=0
contnegatius=0 #si volem contar el "-99", contnegatius=1
contz=0
suma=0 #si volguessim contar el "-99", suma=-99 ja que és l'unic número que no seria sumat i si s'introduiria al sistema.

while n!=-99:
    if n%2==0:
        contparells+=1
    else:
        contimparells+=1
    if n>0:
        contpositius+=1
    elif n<0:
        contnegatius+=1
    else:
        contz+=1
    suma+=n
    n=int(input("Dona'm un número enter: "))

print("")
print("RESUM:")
print("Nombre total de parells:",contparells)
print("Nombre total d'imparells:",contimparells)
print("Nombre total de positius:",contpositius)
print("Nombre total de negatius:",contnegatius)
print("Nombre total de zeros:",contz)
print("Suma de tots els números introduïts:",suma)