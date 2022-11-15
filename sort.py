def saisie_suite(suite):
    n = int(input("Donner le nombre des elements dans la suite: "))
    print("Entre vos element un a un: ")
    for i in range(n):
         a = int(input("Entre l'element suivant: "))
         suite.append(a)
    return suite

def deplacer_a_droite_le_plus_grand(suite, n):
    permuter = False
    for i in range(n):
        if(suite[i] > suite [i+1]):
            permuter = True
            suite[i] , suite[i+1] = suite[i+1] , suite[i]
    return permuter

def trier_suite_ascendant(suite):
    continuer = True
    n = len(suite) - 1
    i = 0
    while i < n and continuer:
        continuer = deplacer_a_droite_le_plus_grand(suite, n - i)
        i = i+1
    

def go():
    suite = []
    saisie_suite(suite)
    print(suite)
    trier_suite_ascendant(suite)
    print("Suite triee en ordre ascendant:", suite)
go()


