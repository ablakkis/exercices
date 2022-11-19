from os import system, name

def clear():
  
    if name == 'nt':
        _ = system('cls')
       
def divisible_deux_trois(n):
    #n = int(input("Entrer un entier positif: "))
    if n % 2 == 0 and n % 3 == 0:
        print(f"Bravo {n} est divisible par 2 et par 3")
        return True
    elif n % 2 == 0:
        print(f"Bravoo {n} est divisible par 2 mais pas par 3")
        return True
    elif n % 3 == 0:
        print(f"Bravoo {n} est divisible par 3 mais pas par 2")
        return True
    else:
        print(f"{n} n'est pas divisible ni par 3 ni par 2")
        return False

def affiche_menu_saisie():
    print("Enter un entier positif: ", end = "")
    nb = int(input())
    return nb

def divisibilite23():
    ok = False
    while not ok:
        clear()
        nb = affiche_menu_saisie()
        ok = divisible_deux_trois(nb)
        if(not ok):
            input("Pour essayer une autre fois tapez sur 2 fois sur Enter ")
            input()

divisibilite23()


