import re
def construire_liste_determinants_from_file(file: str): 
    with open(file, "r", encoding = "utf8") as fin:
        contenu = fin.read()
        return contenu.rsplit(",")
def construire_lignes_du_fichier(file: str):
    
    with open(file, "r", encoding = "utf8") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line[:-1]
            line = line.lower()
        return lines

def split_line_update_dictionnaire(dictionnaire: dict, line: str, sep: str, determinants: list):
    def ajout_mot_dictionnaire(dictionnaire: dict, mot: str):
        if mot in dictionnaire:
            dictionnaire[mot] += 1
        else:
            dictionnaire[mot] = 1 

    def si_apostrophe_a_enlever(mot: str):
        n = mot.find("\'")
        if n == 1:
            return True
        else:
            return False

    liste_mots = line.rsplit(sep)
    print(liste_mots)
    for mot in liste_mots:
        if mot not in determinants:
            if si_apostrophe_a_enlever(mot):
                if(len(mot) > 2):
                    mot = mot[2:]
            ajout_mot_dictionnaire(dictionnaire, mot)
      
def construire_dictionnaire_compteur(dictionnaire: dict, lines: list,  determinants: list, sep: str):

    for line in lines:
        split_line_update_dictionnaire(dictionnaire, line, sep, determinants)


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
    return cle 

def traitement():
    separateurs = ".,;?!: #/{}[]-_+=()@$\n\t%\"\—«»"
    dictionnaire : dict
    dictionnaire = {}
    list_determinants_marq_relation = construire_liste_determinants_from_file("determinants.txt")
    liste_lignes = construire_lignes_du_fichier("texte.txt")
    construire_dictionnaire_compteur(dictionnaire, liste_lignes, list_determinants_marq_relation, separateurs)
    calcul_probabilite_occurence_mots(dictionnaire)
    mot_occurence_max = mot_probabilite_max(dictionnaire)
    print(f"Il y a une tres grande chance que le texte concerne le sujet de {mot_occurence_max}")

#traitement()
if __name__ == '__main__':
    separateurs = ".,;?!: #/{}[]-_+=()@$\n\t%\"\—«»"
    res = re.split(separateurs, "je, suis, abbas. j'aime ma femme(salwa) mais aussi [sajed]")
print(res)




