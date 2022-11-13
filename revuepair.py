import math
#Ce programme a pour but de créer une calculatrice de fraction
def ppcm(a, b):
    #En math ppcm*pgcd = a*b
    return a*b//math.gcd(a,b)


def addition_fraction(fraction_1,fraction_2):
    #On prend le ppcn des deux dénominateurs comme dénominateur commun
    num1, denum1 = fraction_1
    num2, denum2 = fraction_2
    denominateur = ppcm(denum1,denum2)
    numerateur = (denominateur//denum1) * num1 + (denominateur//denum2)*num2
    return numerateur, denominateur

def soustraction_fraction(fraction_1, fraction_2):
    num, denum = fraction_2
    return addition_fraction(fraction_1, (-num, denum))

def multiplication_fraction(fraction_1, fraction_2):
    num1, denum1 = fraction_1
    num2, denum2= fraction_2
    return num1 * num2, denum1 * denum2

def division_fraction(fraction_1, fraction_2):
    a, b = fraction_2
    return multiplication_fraction(fraction_1,(b,a)) 

def fraction_to_str(fraction):
    a, b = fraction
    return str(a) + '/' + str(b) 

def affiche_fraction_resultat(fraction, dictionnaire, choix):
    num, denum = fraction
    print(f"Resultat de l'opération {dictionnaire[choix]}: {fraction_to_str(fraction)}")
    print(f"Resultat de l'opération {dictionnaire[choix]} en décimal: {num/denum:.3f}")

def saisie_fraction(n):
    s = "eme"
    if n == 1:
        s = "er"
    str_fraction = input(f"Entre le {n}{s} fraction sous la forme: numérateur/dénominateur: ")
    slach = str_fraction.find("/")
    numerateur = str_fraction[:slach]
    numerateur = numerateur.rstrip( )
    denominateur = str_fraction[slach+1:]
    denominateur = denominateur.strip( )
    return int(numerateur), int(denominateur)

def affiche_menu(dictionnaire):
    print("Calculatrice sur les fractions")
    for cle in dictionnaire:
        print(f"{cle}: {dictionnaire[cle]}")
    print("Votre choix:",end = " ")
    choix = int(input())
    return choix
def simplifie_fraction(fraction):
    num, denum = fraction
    pgcd = math.gcd(num, denum)
    return num//pgcd, denum//pgcd

def calculatrice():
    dictionnaire = {1: "Addition", 2: "Soustraction", 3: "Multiplication", 4: "Division"}
    choix = affiche_menu(dictionnaire)
    if(not 1<= choix <= 4):
        print("Operation invalide")
    else:
        num1, denum1 = saisie_fraction(1)
        num2, denum2 = saisie_fraction(2)
        result_num = -1
        result_denum = -1
        if choix == 1:
            result_num, result_denum  = addition_fraction((num1, denum1), (num2, denum2))
        elif choix == 2:
            result_num, result_denum  = soustraction_fraction((num1, denum1), (num2, denum2))
        elif choix == 3:
            result_num, result_denum  = multiplication_fraction((num1, denum1), (num2, denum2))
        else:
            result_num, result_denum  = division_fraction((num1, denum1), (num2, denum2))
        result_num, result_denum = simplifie_fraction((result_num, result_denum))
        affiche_fraction_resultat((result_num, result_denum), dictionnaire, choix)


calculatrice()    
        
