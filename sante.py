# Petit programme pour créer une calculatrice 
# d'IMC demandant à l'utilisateur sa grandeur(en mètres), 
# son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la personne.
from interval import interval, inf

def calcule_imc (poids, taille) :
    if taille > 0:
        return poids / taille**2
    else :
        return 0;

def calcule_imc2013(poids, taille):
    if taille > 0:
            return 1.3 * poids / taille**2.5
    else :
        return 0;

def  message_correspondant_resultat_imc(imc) :
    if imc < 20:
        return "Problemes de sante ou peut etre une mauvaise nutrition"
    if  20 <= imc <= 25:
        return "Sante sainne"
    if 25 < imc <= 27:
        return "Un risque possible de maladie"
    else :
        return "Un risque accru de probleme de sante"

def  message_correspondant_resultat_imc2013(imc) :
    if imc <= 15.5 :
        return "Maigreur severe ou anorexie"
    if  15.5 < imc <= 17.49:
        return "Insuffisance ponderale visible ou anorexie moderee"
    if 17.5 <= imc <= 18.49:
        return "Insuffisance pondderale legere"
    if 18.5 <= imc <= 24.9 :
        return "corpulence normale (poids ideal)"
    if 25 <= imc <= 29.9 :
        return "surpoids"
    if 30 <= imc <= 34.9 :
        return "Obesite de  classe I ou modere"
    if 35 <= imc <= 39.9 :
        return "Obesite de  classe II"
    else :
        return "Obesite de  classe III"

def message_correspondant_resultat_imc2013N(imc):
    x = round(imc,2)
    list = (interval([0,15.49]), interval([15.5,17.49]), interval([17.5,18.49]), interval([18.5,24.9]), interval([25,29.9]), interval([30,34.9]), interval([40,+inf]))
    messages = ("anorexie","anorexie moderee","Insuffisance pondderale legere","poids ideal", "surpoids", "Obesite de  classe I","Obesite de  classe II", "Obesite de  classe III" )
    for i in range(len(list)):
        if x in list[i] :
            return messages[i]
    
def main():
    poids = float(input("Entrer votre poids en Kg:" ))
    taille = float(input("Entrer votre taille en metres:" ))
    #imc = calcule_imc (poids, taille) 
    imc = calcule_imc2013 (poids, taille) 
    #resultat =  message_correspondant_resultat_imc2013 (imc)
    resultat =  message_correspondant_resultat_imc2013N(imc)
    print(f"IMC: {imc:.3} -> {resultat}")

main()
