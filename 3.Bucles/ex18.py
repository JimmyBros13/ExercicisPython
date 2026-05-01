#Exercici 18

palabra=input("Eintrodueix una paraula: ")
vocals=""
consonants=""
check="aeiouàáèéíòóú"

for lletra in palabra.lower():
    if lletra.isalpha():
        if lletra in check:
            vocals+=lletra
        else:
            consonants+=lletra
print("Les vocals de la paraula son: ",vocals)
print("Les consonants de la paraula son: ",consonants)