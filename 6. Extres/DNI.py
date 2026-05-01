#Exercici DNI

lletra=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
intents=[]
correctes=[]
incorrectes=[]
inclong=[]
incnum=[]
incnoex=[]

def menuP0():
    print("\nRESULTATS\n1. Llistar DNIs correctes de menor a major\n2. Llistar DNIs incorrectes ordenats de menor a major\n3. Número total d'errors produïts\n4. Número total de DNIs correctes\n5. Percentatges d'errors i encerts\n6. Introduïr més números\n7. Sortir")
    opcioP0=input("\nQue vols fer? ")
    while opcioP0!="7":
        if opcioP0=="0":
            print("\nRESULTATS\n1. Llistar DNIs correctes de menor a major\n2. Llistar DNIs incorrectes ordenats de menor a major\n3. Número total d'errors produïts\n4. Número total de DNIs correctes\n5. Percentatges d'errors i encerts\n6. Introduïr més números\n7. Sortir")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="1":
            print(f"\nDNIs correctes:\n{sorted(correctes)}")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="2":
            print(f"\nDNIs incorrectes:\n{sorted(incorrectes)}")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="3":
            print(f"\nS'ha introduït un total de {len(correctes)} DNIs correctes")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="4":
            print(f"\nS'ha introduït un total de {len(incorrectes)} DNIs incorrectes\n   Errors de longitud: {len(inclong)}\n   Errors de format: {len(incnum)}\n   Errors d'existència: {len(incnoex)}")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="5":
            print(f"\nValors en %:\nEncerts: {round(len(correctes)/len(intents)*100,2)}%\nErrors: {round(len(incorrectes)/len(intents)*100,2)}%\n   Errors de longitud: {round(len(inclong)/len(incorrectes)*100,2)}%\n   Errors de número: {round(len(incnum)/len(incorrectes)*100,2)}%\n   Errors d'exixtència: {round(len(incnoex)/len(incorrectes)*100,2)}%")
            opcioP0=input("\nQue vols fer? ")
        elif opcioP0=="6":
            loopintroDNI=(input("\nSegur? (s/n): "))
            introDNI(loopintroDNI)
            print("\nRESULTATS\n1. Llistar DNIs correctes de menor a major\n2. Llistar DNIs incorrectes ordenats de menor a major\n3. Número total d'errors produïts\n4. Número total de DNIs correctes\n5. Percentatges d'errors i encerts\n6. Introduïr més números\n7. Sortir")
            opcioP0=input("\nQue vols fer? ")
        else:
            opcioP0=input("\nOpció erronea. Que vols fer? [0-7]: ")
def introDNI(loopintroDNI):
    while loopintroDNI.lower()=="s":
        numero=input("\nIntrodueix EL NUMERO del DNI: ")
        if len(numero)==8:
            if numero.isdigit():
                if int(numero)%23>=0 and int(numero)%23<=22:
                    correctes.append(f"{numero}-{lletra[int(numero)%23]}")
                    intents.append(f"3.{numero}")
                    print(f"\n## {numero}-{lletra[int(numero)%23]} ##")
                else:
                    incorrectes.append(numero)
                    incnoex.append(numero)
                    intents.append(f"2.{numero}")
                    print("\n-- El numero no és correcte, no podem assignar lletra --")
            else:
                incorrectes.append(numero)
                incnum.append(numero)
                intents.append(f"1.{numero}") 
                print("\n-- Ha de ser tot números --")
        else:
            incorrectes.append(numero)
            inclong.append(numero)
            intents.append(f"0.{numero}") 
            print("\n-- La longitud no és correcta --")
        loopintroDNI=input("\nVols introduïr un altre número? (s/n): ")

loopintroDNI="s"
introDNI(loopintroDNI)
menuP0()
print("\n-- Programa finalitzat --\n")