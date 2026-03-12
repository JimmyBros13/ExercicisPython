#Exercici 9
import math
print("Calculadora d'equacions de segons grau:")
a=int(input("a= "))
b=int(input("a= "))
c=int(input("a= "))

inrq=b**2-4*a*c
if inrq<0:
    print("El valor de l'arrel quadrada és negatiu, no es pot prosseguir amb el càlcul.")
else:
    rq=math.sqrt(inrq)
    eqc1=(-b+rq)/(2*a)
    eqc2=(-b-rq)/(2*a)
    print("x1 =",eqc1,"x2 =",eqc2)