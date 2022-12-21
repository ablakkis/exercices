import os, random

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def calcul_liste_somme(val: int, table: list) -> list:
    if table :
        if table[0] == val:
            L1 = [table[0]] 
            table.remove(table[0])
            L2 = calcul_liste_somme(val, table[1:])
            if  L2 :
                #L2 = add_to_lists(val, L2)
                return [L1, L2] 
            else:
                return L1
        elif table[0] < val:
                val_1 = val - table[0]
                L1 = calcul_liste_somme(val_1, table[1:])
                if L1:
                    return L1 + [table[0]]
                else:
                    L2 = calcul_liste_somme(val, table[1:])
                    if L2:
                        return L2+[table[0]]
                    else:
                        return []
                #if L1  and L2 :
                 #   return [L1+[table[0]], L2+[table[0]]]

                #elif  L1 :
                 #   return L1 + [table[0]]
                #elif L2:
                 #   return L2 + [table[0]]
        else:
            L1 = calcul_liste_somme(val, table[1:])
            return L1
    else:
        return []
           
cls()           
table : list
result = []
table = [7, 7, 4, 4, 3, 7, 1, 2]
result = calcul_liste_somme(7, table)
print(table)
print("la liste est")
print(result)
