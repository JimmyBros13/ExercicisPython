#Crea un programa que pida dos números por teclado y visualice por pantalla los números pares e impares del rango que va del primero hasta el segundo

a=int(input("Numero a: "))
b=int(input("Numero b: "))

for num in range(a,b+1):
    if num%2==0:
        print(f"{num} és parell")
    else:
        print(f"{num} és imparell")

#Añade en el programa anterior la opción de continuar o no la ejecución del programa "desea repetir el programa? si/no". Se adunta ejemplo de resultado

pregunta=input("Vols continuar? (s/n): ")

while pregunta.lower()=="s":
    a=int(input("Numero a: "))
    b=int(input("Numero b: "))

    for num in range(a,b+1):
        if num%2==0:
            print(f"{num} és parell")
        else:
            print(f"{num} és imparell")
            
    pregunta=input("Vols continuar? (s/n): ")

print("Programa finalitzat")