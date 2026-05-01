#joc del penjat

import random

palabrasecreta=["muntanya","manchester","transmissions","realització","arsenal","leverkusen","bodoglimt","nashville","digestió","micròfon"]
resposta=[]
pista=[]
errors=0
ahorcado=["A","H","O","R","C","A","D","O"]
posicio=random.randint(0,len(palabrasecreta)-1)

a=random.randint(0,len(palabrasecreta)-1)
print(palabrasecreta[a])
for lletra in palabrasecreta[a]:
    resposta.append(lletra)
pista=["_"]*len(resposta)
print(resposta)

print(f"\nEndevina la paraula de {len(palabrasecreta[a])} lletres: {pista}\n")
while errors<8:
    paraula=input(f"Paraula ({len(palabrasecreta[a])} lletres): ").lower()
    if paraula==palabrasecreta[a]:
        print(f"\nCORRECTE! La paraula és {palabrasecreta[a].upper()}, l'has encertat en {errors+1} intents!\n")
        break
    elif len(paraula)!=len(palabrasecreta[a]):
        print(f"\n-- Has d'escriure una paraula amb {len(resposta)} lletres! --\n")
    elif paraula.isalpha()==False:
        print(f"\n-- Has d'escriure una paraula sense números ni caràcters especials amb {len(resposta)} lletres! --\n")
    else:
        errors+=1
        if errors==8:
            print(f"\n{ahorcado}\n\nHas perdut! La paraula era {palabrasecreta[a].upper()}\n")
            break
        else:
            for lletra in paraula:
                for pos in range(len(resposta)):
                    if lletra == resposta[(pos)]:
                        pista[pos]=lletra.upper()       
            print(f"\n{pista}")    
            print(f"\n{ahorcado[:errors]} -- et queden {len(ahorcado)-errors} intents\n")


