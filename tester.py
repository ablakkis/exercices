import os, random

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

    
def calcul_liste_somme(val: int, table: list) -> list:
    if len(table) > 0:
        if table[0] == val:
            return [val] + calcul_liste_somme(val, table[1:])
        elif table[0] < val:
                val_1 = val - table[0]
                res = []
                res = calcul_liste_somme(val_1, table[1:])
                if len(res) > 0:
                    return res + [table[1]]
                return calcul_liste_somme(val_1, table[1:])
        else:
            return calcul_liste_somme(val, table[1:])
    else:
        return []

            
cls()           
table : list
table = [2, 5, 3, 1, 2, 4, 8, 6]
liste  = calcul_liste_somme(7, table )
print("la liste est")
print(liste)
