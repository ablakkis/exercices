#trier 4 entiers sans utilisation de boucle

def permut(a, b):

    if(a > b):
        return b, a, True
    return a, b, False

def arranger(a1, a2, a3, a4, n ): # n étant le nombre de comparaison a faire a partir du début
    ok = False
    if n >= 1:
        a1, a2, ok = permut(a1, a2)
    if(n >= 2):
        a2, a3, ok = permut(a2, a3)
    if(n == 3):
        a3, a4 , ok = permut(a3, a4) 
    return a1, a2, a3, a4, ok

def saisie_suite():
    a1 = int(input("entrer le premier entier: "))
    a2 = int(input("entrer le second: "))
    a3 = int(input("entrer le 3eme: "))
    a4 = int(input("entrer le 4eme: "))
    return a1, a2, a3, a4

def go():
    a1, a2, a3, a4 = saisie_suite()
    a1, a2, a3, a4, ok = arranger(a1, a2, a3, a4, 3)
    if ok :
        a1, a2, a3, a4, ok = arranger(a1, a2, a3, a4, 2)
        if ok :
            a1, a2, a3, a4, ok = arranger(a1, a2, a3, a4,1)
    print(f"suite triée {a1}, {a2}, {a3}, {a4}")
go()



