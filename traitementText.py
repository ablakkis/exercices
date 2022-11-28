
def construire_liste_determinants_from_file(file: str): 
   with open(file, "r", encoding = "utf8") as fin:
        contenu = fin.read()
        return contenu.rsplit(",")

def construire_lignes_du_fichier(file: str):
    with open(file, "r", encoding = "utf8") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.lower()
        return lines

def split_ligne(ligne: str, sep: str, determinants: list):

    def si_enleve_apostrophe(mot : str):
        n = mot.find("'")
        m = mot.find("’")
        if n == 1 or m == 1:
            if len(mot) > 2:
                mot = mot[2:]
            else:
                mot = "" 
        return mot

    res = []
    word = ""
    for ch in ligne:
        if ch not in sep:
            word += ch
        else:
            if word not in determinants:
                word = si_enleve_apostrophe(word)
                if len(word) > 1:
                    word = word.lower()
                    if word not in determinants:
                        res.append(word)
            word = ""
    return res

def ajout_mot_dictionnaire(dictionnaire: dict, mot: str):
    if mot in dictionnaire:
        dictionnaire[mot] += 1
    else:
        dictionnaire[mot] = 1 
    
def split_lignes(lignes: str, sep: str, determinants: list):
    result = []
    for ligne in lignes:
        result += split_ligne(ligne, sep, determinants)
    return result

def construire_dictionnaire_compteur(dictionnaire: dict, lines: list):
    separateurs = ".,;?!: #/{}[]-_+='()@$\n\t%\"\—«»"
    determinants = construire_liste_determinants_from_file("determinants.txt")
    result = split_lignes(lines, separateurs, determinants)
    for mot in result:
        ajout_mot_dictionnaire(dictionnaire, mot.lower())

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

def tri_valeurs_cles(dictionnaire : dict, nb: int):
    def deplacer_a_droite_le_plus_petit(kys: list, items: list, n: int):
        permuter = False
        for i in range(n):
            if(items[i] < items [i+1]):
                permuter = True
                items[i] , items[i+1] = items[i+1] , items[i]
                kys[i] , kys[i+1] = kys[i+1] , kys[i]
        return permuter

    def trier_suite_decroissant(kys: list, items: list):
        continuer = True
        n = len(kys) - 1
        i = 0
        while i < n and continuer:
            continuer = deplacer_a_droite_le_plus_petit(kys, items, n - i)
            i = i+1
    
    kys = list(dictionnaire.keys())
    items = list(dictionnaire.values())
    trier_suite_decroissant(kys, items)
    sous_dic= {}
    for i in range(nb):
        sous_dic[kys[i]]= items[i]
    return sous_dic
    #print(result)

def traitement():
    dictionnaire : dict
    dictionnaire = {}
    liste_lignes = construire_lignes_du_fichier("texte.txt")
    construire_dictionnaire_compteur(dictionnaire, liste_lignes)
    sous_dic = tri_valeurs_cles(dictionnaire, 15)
    print(sous_dic)
    #calcul_probabilite_occurence_mots(dictionnaire)


    
traitement()



