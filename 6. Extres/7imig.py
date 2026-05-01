# el joc del 7 i mig amb un diposit de 100 punts, 10 punts en joc per partida

import random

cartes=[1,2,3,4,5,6,7,0.5,0.5,0.5]
diposit=100
punts=0
carta=0
jugar=input("Vols jugar? (s/n): ")
while jugar.lower()=="s":
    if diposit>=0:
        pregunta=input("Vols jugar carta? (s/n): ")
        while pregunta.lower()=="s":
            carta=random.randint(0,len(cartes)-1)
            punts+=float(cartes[carta])
            print(f"{cartes[carta]}, sumant un total de {punts} punts")
            if punts>7.5:
                break
            elif punts==7.5:
                print("Has guanyat!")
                break
            else:
                pregunta=input("Vols seguir jugant? (s/n): ")
        if punts==7.5:
            diposit+=10
            print(f"Has sumat un total de 10 punts!")
            punts=0
        elif punts>=6 and punts<=7:
            diposit+=5
            print(f"Has sumat un total de 5 punts!")
            punts=0
        elif punts<6:
            diposit-=5
            print(f"Has perdut un total de 5 punts!")
            punts=0
        else:
            diposit-=10
            print(f"Has perdut un total de 10 punts!")
            punts=0
        jugar=input(f"Vols tornar a jugar? Tens {diposit} punts (s/n): ")
    else:
        print("No pots seguir jugant, t'has quedat sense punts")
        break
print(f"Fi del joc! Acabes amb {diposit} punts!")
    