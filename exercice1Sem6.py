# programme qui permet de trouver la liste des nombres 
#premier entre 2 et une limite saiosie au clavier
from os import system, name 

def clear():
    if name == 'nt':
        _ = system('cls')

def si_premier(n, prem_liste):
    fin = False
    indice = 0
    while not fin:
        if prem_liste[indice] > n // 2:
            fin = True
            prem_liste.append(n)
        elif n % prem_liste[indice] == 0:
                fin = True
        else:
            indice += 1

def construire_liste_premier(n):  
    liste_premier = [2] 
    for ent in range(3, n+1, 2):
       si_premier(ent, liste_premier) 
    return liste_premier

def nombree_premiers():
    limite = int(input("entre 2 et quoi vous voulez la liste des nombres premier? "))
    liste_premier = construire_liste_premier(limite)
    return liste_premier

def voir_si_premier(n, premiers):
    if n in premiers:
        print(f"{n} est premier")
    else:
       print(f"{n} est non premier") 

def traitement():
    clear()
    fin = False
    liste_premiers = nombree_premiers()
    while not fin:
        clear()
        n = int(input("Votre entier (taper -1) pour arreter? ")) 
        if n == -1:
            fin = True
        else:
            voir_si_premier(n, liste_premiers)
            input("Any key pour continuer")

traitement()






