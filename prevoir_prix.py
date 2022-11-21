#À partir de votre programme de calcul de l'effet de 
#l'inflation (Semaine 3), implémentez un programme prenant une fichier intitulé 
#ipc.txt où vous aurez les IPCs des années 1960 à 2021 et permettant à l'utilisateur 
#d'entrer une année de son choix pour effectuer le calcul. Vous devez aussi permettre à 
#l'utilisateur d'entrer le prix de l'article en 1970 et son coût en 2021 
def read_file(name_file: str):
    file = open(name_file,"r")
    data = file.readlines()
    taux_inflation = {}
    for line in data:
        (annee, tinfl) = line.split(":")
        taux_inflation[annee] = float(tinfl[: len(tinfl) - 1])
    file.close()
    return taux_inflation

def calcule_prix(taux_inflation, annee_achat, prix_achat, annee_previs):
    #kys = taux_inflation.keys()
    #annee_achat = int(input("Annee d'achat du produit?(doit etre apres 1960) ")
    #prix_achat = float(input)("Prix d'achat? ")
    prix = prix_achat
    #index = annee_achat - 1960
    for a in range(annee_achat, annee_previs, 1):
        prix = prix + prix * taux_inflation[str(a)]/100
    return prix
def prevoir_prix(): 
    dict_inflation = read_file("pci.txt")
    annee_achat = int(input("Annee d'achat du produit?(doit etre apres 1960 et avant 2022) "))
    message = "Prix d'achat en "+ str(annee_achat) + "?"
    prix_achat = float(input(message))
    annee_previs = int(input("En quelle annee souhaite-tu connaitre le prix? "))
    prix = calcule_prix(dict_inflation, annee_achat, prix_achat, annee_previs)
    print(f"Ce produit coute {prix:.3f} en {annee_previs}")
    
prevoir_prix()

 
    




