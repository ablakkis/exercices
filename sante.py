# Petit programme pour créer une calculatrice 
# d'IMC demandant à l'utilisateur sa grandeur(en mètres), 
# son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la personne.

def calcule_imc (poids, taille) :
    if taille > 0:
        return poids / taille**2
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

def main():
    poids = float(input("Entrer votre poids en Kg:" ))
    taille = float(input("Entrer votre taille en metres:" ))
    imc = calcule_imc (poids, taille) 
    resultat =  message_correspondant_resultat_imc(imc)
    print(f"IMC: {imc:.3} -> {resultat}")

main()