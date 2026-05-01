#Exercici 27

elements=int(input("Quants elements vols ficar? "))
entrades=0
llista=[]

while entrades<elements:
    entrada=input("Introdueix un número: ")
    entrades+=1
    llista.append(entrada)

llista.sort()
print(llista)
