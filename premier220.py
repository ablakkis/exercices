def premier_entre_2_20( n ):
    if n % 2  == 0 or n == 9 or n == 15:
        print (f"Le nombre {n} n'est pas premier")
    else:
        print (f"Le nombre {n} n'est pas premier")
    
def saisie_nombre():
    n = int(input("Entre en entier entre 2 et 20: "))
    if not 2 <= n <= 20:
        print("Valeur en dehors de 2 et 20 - programme s'arrete")
        return False, -1
    else:
        return True, n

def traiter():
    ok, n = saisie_nombre()
    if ok:
        premier_entre_2_20(n)

traiter()
               

      
