
def construite_liste_determinants_from_file():
    with open("determinants.txt", "r", encoding = "utf8") as fin:
        contenu = fin.read()
        return contenu.strip(",")
    return contenu
