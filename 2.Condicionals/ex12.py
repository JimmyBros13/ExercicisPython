#Exercici 12
lletra=input("Dona'm una lletra: ")
if "a"<=lletra.lower()<="z":
    if lletra==lletra.lower():
        print(lletra,"és minuscula")
    else:
        print(lletra,"és Majuscula")
elif "0"<=lletra<="9":
    print(lletra,"és un número")
else:
    print(lletra,"és un simbol")