def construire_liste_determinants_from_file(file: str): 
    with open(file, "r", encoding = "utf8") as fin:
        contenu = fin.read()
        return contenu.rsplit(",")

def split_ligne(ligne: str, sep: str, determinants: list):
    res = []
    word =""
    ligne = ligne.lower()
    for ch in ligne:
        if ch not in sep:
            word += ch
        else:
            if word not in determinants:
                word = si_enleve_apostrophe(word)
                if len(word) > 1:
                    if word not in determinants:
                        res.append(word)
            word = ""
    return res
def si_enleve_apostrophe(mot : str):
    n = mot.find("'")
    if(n == 1):
        if mot not in determinants:
            if len(mot) > 2:
                mot = mot[2:]
            else:
                mot = "" 
    return mot
       
    

determinants = list_determinants_marq_relation = construire_liste_determinants_from_file("determinants.txt")
ligne= input()
res = split_ligne(ligne, ".,;?!: #/{}[]-_+=()@$\n\t%\"\—«»",determinants)
print(res)