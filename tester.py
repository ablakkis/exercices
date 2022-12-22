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
def intersection(l1: list, l2: list):
    for t in l1:
        if t in l2:
            return True
    return False
        
def nettoyer_liste(liste: list):
    liste_bis = []
    for i, k in enumerate(liste):
        j = i + 1
        fin = False
        while j < len(liste) and not fin:
            if intersection(k, liste[j]):
                fin = True
            j += 1
        if not fin:
            liste_bis.append(k)
    return liste_bis

cls()           
table : list
result = []
table = [9, 2, 5, 1, 6, 8, 3, 7, 4, 10]
calcul_liste_somme(9, table, [], result)
print(result)
result = nettoyer_liste(result)
print("Apres nettoyage")
print(result)
