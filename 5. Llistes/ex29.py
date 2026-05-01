#Exercici 29

lista1=["a","b","D","x","r","X","3","h","w","2","i"]

longitud=len(lista1)
total=0
contnumeros=0
contmayus=0
contminus=0

for item in lista1:
    if item.isdigit():
        contnumeros+=1
        total+=int(item)
    elif item.isupper():
        contmayus+=1
    elif item.islower():
        contminus+=1

contlletres=longitud-contnumeros

print("El total de valors de la llista és de",longitud,"items")
print("Números:",contnumeros)
print("Lletres:",contlletres)
print("Majúscules:",contmayus)
print("Minúscules:",contminus)
print("Suma total dels valors:",total)