
def lire_fichier_determinants():
    with open("determinants.txt", "r", encoding = "utf8") as fin:
        contenu = fin.read()
    return contenu

def construire_tuple_determinants_marqueurs_relation(contenu: str):
    liste_determinants = contenu.strip(",")
    determinants = tuple(liste_determinants)
    return determinants

def proceed():
    determs = lire_fichier_determinants()
    liste_determinants = determs.strip(",")
    tupl = construire_tuple_determinants_marqueurs_relation(liste_determinants)
    if("d'abort" in liste_determinants):
        print("ok")
    else:
        print("non ok")

    #for t in tupl:
     #   print(t, end = " ")
    #print(tupl)

proceed()



