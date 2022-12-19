def somme(liste: list):
    s = 0
    for elem in liste:
        s += elem
    return s
def ajout_list_to_list(liste_1: list, liste_2: list, val: int):
    return liste_1 + liste_2 + [val]
def calcul_liste_somme(initial_val: int, liste_attente: list, table: list, list_resultat):
    if len(table) > 0:
        if table[0] == initial_val:
            liste_resultat.append(table[0])
            
            return liste

        if somme(liste_attente) + table[0] == initial_val:
            liste_resultat = ajout_list_to_list(liste_resultat, liste_attente, table[0])
            return calcul_liste_somme(initial_val,[],table[1:], liste_resultat)
        elif somme(liste_attente) + table[0] < initial_val:
            liste_attente.appemd(table[0])
            return calcul_liste_somme(initial_val, liste_attente, table[1:])
        else:
            return calcul_liste_somme(initial_val, liste_attente, table[1:])
    else:
        pass

def test(liste: list):
    for i in range(10):
        liste.append(i)

liste : list
liste = []
test(liste)
print(liste)
