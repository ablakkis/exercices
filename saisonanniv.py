def si_bissec(annee) :
    if annee % 4 == 0 and annee % 100 == 0 :
        return annee % 400 == 0
    return annee % 4 == 4

def correcte_date(date) : 
    annee_bissec = ( (31, 28, 31, 30, 31, 30, 31, 31,30,31,30,31), (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) )
    jour, mois , annee = date
    bissec = si_bissec(annee)
    if 1<= mois <= 12 : 
       return 1 <= jour <= annee_bissec[bissec][mois-1]
    else :
        return False

def trouve_saison(date) :
    saisons = ("hiver", "printemps", "ete", "automne")
    jour, mois = date
    if mois in (3, 6, 9, 12) and jour < 21 :
        return saisons[mois //3 - 1]
    return saisons[mois // 3 % 4]

def affiche_saison_anniversaire () :
    annee = int (input("Entre to annee de naissance: "))
    mois = int (input("Entre ton mois de naissance: "))
    jour = int (input("Entre ton jour de naissance: "))
    if correcte_date((jour, mois, annee)):
        print(f" Tu es ne {trouve_saison((jour, mois))} ")
    else :
        print("Tu a entre une mauvaise date le program quit .....")

affiche_saison_anniversaire()

