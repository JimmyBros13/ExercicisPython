#Exercici 6
print("Calcul de la massa coropral IMC")
pes=float(input("Pes:")) #float tot i que a l'exercici els pesos siguin enters
h=float(input("Alçada:"))
imc=pes/h**2

if imc<25:
    print("Amb un pes de",pes,"kgs i una alçada de",h,"m, el teu IMC és de",round(imc,2),". No pateixes sobrepes")
else:
    print("Amb un pes de",pes,"kgs i una alçada de",h,"m, el teu IMC és de",round(imc,2),". Pateixes sobrepes")