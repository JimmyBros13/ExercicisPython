#Exercici 10
lletra=input("Dona'm una lletra: ")
if "a"<=lletra.lower()<="z":
    if lletra==lletra.lower():
        print(lletra,"és minuscula")
    else:
        print(lletra,"és Majuscula")
else:
    print(lletra,"és Majuscula?")
