#Exercici 13
frase=input("Dona'm una frase: ")
long=len(frase)
if long>11:
    print("La frase té més d'11 caràcters")
elif long<11:
    print("La frase té menys d'11 caràcters")
else:
    print("La frase té just 11 caràcters")