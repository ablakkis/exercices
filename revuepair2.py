def saisie_liste():
    liste_positif = []
    print("Entre une liste d'entier positifs. Un entier negatif pour arret de saisie")
    fin = False
    while not fin:
        nb = int(input())
        if(nb < 0):
            fin = True
        else:
            liste_positif.append(nb)
    return liste_positif

def trier_suite_ascendant(suite):
    def deplacer_a_droite_le_plus_grand(suite, n):
        permuter = False
        for i in range(n):
            if(suite[i] > suite [i+1]):
                permuter = True
                suite[i] , suite[i+1] = suite[i+1] , suite[i]
        return permuter
    
    continuer = True
    n = len(suite) - 1
    i = 0
    while i < n and continuer:
        continuer = deplacer_a_droite_le_plus_grand(suite, n - i)
        i = i+1
def inverser_suite(suites):
    suite_inverse = []
    n = len(suites)
    for i in range(n):
        suite_inverse.append(suites[n-i-1])
    return suite_inverse

def trouve_max(suite: list):
    if len(suite) > 0 :
        max  = suite[0]
        for ent in suite:
            if ent > max:
                max = ent
    return max

def trouve_min(suite: list):
    if len(suite) > 0 :
        min  = suite[0]
        for ent in suite:
            if ent < min:
                min = ent
    return min

def mediane(suite: list):
  #La médiane (la valeur à la position centrale si la longueur de la liste est 
  # impaire et la moyenne des deux valeurs centrales si paire) 
    n = len(suite)
    if n == 1:
        return suite[0]
    if n % 2 == 0 :
        m = n // 2
        return (suite[m-1] + suite[m]) / 2
    return suite[n//2]

def trouve_modes(suite: list) :
    modes = []
    dictionnaire = {} 
    for ent in suite:
        if ent in dictionnaire:
            dictionnaire[ent] = dictionnaire[ent] + 1
        else:
            dictionnaire[ent] = 1
    print(dictionnaire)
    occurences = list(dictionnaire.values())
    max_occ = trouve_max(occurences)
    if max_occ == 1:
        return None
    else:
        for cle in dictionnaire.keys():
            if dictionnaire[cle] == max_occ:
                modes.append(cle)
        return modes

def tester():
    entiers = saisie_liste()
    max = trouve_max(entiers)
    min = trouve_min(entiers)
    print(f"max = {max}, min = {min}")
    trier_suite_ascendant(entiers)
    print(entiers)
    med = mediane(entiers)
    print(f"mediane = {med}")
    entiers_inverse = inverser_suite(entiers)
    print(entiers_inverse) 
    modes = trouve_modes(entiers) 
    print(modes)     
    
tester()
