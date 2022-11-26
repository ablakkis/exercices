def construite_liste_determinants_from_file(file: str): 
    with open(file, "r", encoding = "utf8") as fin:
        contenu = fin.read()
        return contenu.strip(",")
def construire_liste_mots_du_fichier(file: str):
    separateurs = ".,;?!: #/{}[]-_+=()@$\"\n\t{%\\"
    with open(file, "r", encoding = "utf8") as fin:
        contenu = fin.read()
        contenu = contenu.lower()
        liste_mots = contenu.strip(separateurs)
        return liste_mots

def si_apostrophe_a_enlever(mot: str):
    n = mot.index("'")
    if n == 1:
        return True
    else:
        return False
    
def construire_dictionnaire_compteur(dictionnaire: dict, contenu_file: list,  determinants: list):

    def ajout_mot_dictionnaire(dictionnaire: dict, mot: str):
        if mot in dictionnaire:
            dictionnaire[mot] += 1
        else:
            dictionnaire[mot] = 1 
    
    for mot in contenu_file:
        if mot not in determinants:
            if si_apostrophe_a_enlever(mot):
                if(len(mot) > 2):
                    mot = mot[2:]
                    ajout_mot_dictionnaire(dictionnaire, mot)
            else:
                ajout_mot_dictionnaire(dictionnaire, mot)  

def calcul_probabilite_occurence_mots(dictionnaire: dict):
    liste_cles = list(dictionnaire.keys())
    length = len(dictionnaire)
    for k in liste_cles:
        dictionnaire[k] /= length

def mot_probabilite_max(dictionnaire: dict):
    liste_cles = list(dictionnaire.keys())
    max, cle = dictionnaire[liste_cles[0]], liste_cles[0]
    for k in liste_cles:
        if max < dictionnaire[k]:
            max, cle = dictionnaire[k], k
    return k 

def traitement():

    dictionnaire : dict
    dictionnaire = {}
    list_determinants_marq_relation = construite_liste_determinants_from_file("determinants.txt")
    liste_mots_texte = construire_liste_mots_du_fichier("texte.txt")
    construire_dictionnaire_compteur(dictionnaire, liste_mots_texte, list_determinants_marq_relation)
    calcul_probabilite_occurence_mots(dictionnaire)
    mot_occurence_max = mot_probabilite_max(dictionnaire)
    print(f"Il y a une tres grande chance que le texte concerne le sujet de {mot_occurence_max}")

traitement()




