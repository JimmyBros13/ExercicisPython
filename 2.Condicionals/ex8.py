#Exercici 8
a=int(input("Introdueix un número del 0 al 10: "))
b=int(input("Introdueix un altre número del 0 al 10: "))

if (a or b)>10:
    print("Un o el dos números son majors que 10")
elif a==b:
    print(a,"i",b,"son iguals")
elif a>b:
    print(a,"és més gran que",b)
else:
    print(b,"és més gran que",a)