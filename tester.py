import os, random

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def fill_liste(a: int, liste: list):
    if a < 10:
        liste.append(a)
        fill_liste(a+1, liste)




def calcul_liste_somme(val: int, table: list, attente: list, result: list[list]):
    if table :
        if table[0] == val:
            result.append(attente + [table[0]] )
            calcul_liste_somme(val, table[1:], attente, result) 
        elif table[0] < val:
                val_1 = val - table[0]
                calcul_liste_somme(val_1, table[1:], attente + [table[0]], result)
                calcul_liste_somme(val, table[1:], attente, result )
        else:
            calcul_liste_somme(val, table[1:], attente, result)
           
cls()           
table : list
result = []
table = [7, 2, 5, 1, 7, 8, 3, 1, 4]
calcul_liste_somme(7, table, [], result)
#fill_liste(0, result)
print(result)
