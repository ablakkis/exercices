def capitale_apres(capitale_initiale,nb_annee,taux):
    new_capitale = capitale_initiale
    for i in range(nb_annee):
        new_capitale = new_capitale + new_capitale*taux
    return new_capitale

def doubler_capitale(capitale,taux):
    y = 0
    capitale_courant = capitale
    while capitale_courant < 2*capitale:
        capitale_courant = capitale_courant + capitale_courant*taux
        y = y+1
    return y

def go():
    taux = 0.03
    cap = float(input("Capitale a deposer: "))
    nb_year = int(input("Nombre d'anneés: "))
    print(f"La capitale devient {capitale_apres(cap, nb_year, taux):.3f}")
    print(f"Votre capitale doublera dans {doubler_capitale(cap,taux)} années")

go()