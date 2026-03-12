#Exercici 7
a=int(input("Introdueix un número:"))
b=int(input("Introdueix un altre número:"))

if a==b:
    print(f"{a} i {b} son iguals")
elif a>b:
    print(a,"és més gran que",b)
else:
    print(b,"és més gran que",a)