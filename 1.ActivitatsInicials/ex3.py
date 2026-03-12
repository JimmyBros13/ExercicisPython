#Exercici 3
a=int(input("Dona'm un número: "))
b=int(input("Dona'm un altre número: "))

suma=a+b
resta=a-b
multi=a*b
divisio=a/b
exponent=a**b
entera=a//b

print("El total de ",a,"+",b,"= ",suma)
print("El total de ",a,"-",b,"= ",resta)
print("El total de ",a,"x",b,"= ",multi)
print("El total de ",a,"/",b,"= ",round(divisio,2))
print(a," elevat a ",b,"= ",exponent)
print("La divisió entera de",a,"i",b," és ",entera)