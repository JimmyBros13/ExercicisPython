#Exercici 19

a=int(input("Primer número:"))
b=int(input("Segon número: "))

if a<b:
    numero=[str(n) for n in range(a,b+1)]
    interval="-".join(numero)
    print(interval)

elif a>b:
    numero=[str(n) for n in range(a,b-1,-1)]
    interval="-".join(numero)
    print(interval)

else:
    print("Els números son iguals")


