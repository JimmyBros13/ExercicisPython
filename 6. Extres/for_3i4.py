# Realiza un un programa que al escribir un número por teclado se visualice la tabla de multiplicar del 1 al 10 del valor introducido

num=int(input("numero: "))

for m in range(1,11):
    multi=num*m
    print(f"{num}*{m}={multi}")

#que imprimeixi fins que la multiplicació sigui superior a 40

for m in range(1,11):
    multi=num*m
    if multi<=40:
        print(f"{num}*{m}={multi}")
    else:
        print(f"Multiplicació aturada, {num}*{m}>40")
        break