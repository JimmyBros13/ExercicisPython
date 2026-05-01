#Exercici 28

llista=[]
pregunta=""

while pregunta!="n":
    lletra=input("Introdueix una lletra: ")
    if lletra.isalpha():
        llista.append(lletra)  
        pregunta=input("Vols seguir? (s/n):").lower()

unica=list(set(llista))
print(unica)