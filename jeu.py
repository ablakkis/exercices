from os import system, name
import random 

def clear():
    if name == 'nt':
        _ = system('cls')

def jouer():

    clear()
    limite = int(input("Limit: "))
    nb_essais = int(input("Nombre d'essais: "))
    nombre_a_deviner = random.randint(1,limite)
    i = 1
    trouve = False
    while i <= nb_essais and not trouve:
        choix_utilisateur = int(input("Votre proposition: "))
        if choix_utilisateur == nombre_a_deviner:
            print(f"Gagner aprés {i} tentatives")
            trouve = True
        elif  choix_utilisateur < nombre_a_deviner :
            print("Votre nombre est trop petit")
            i = i + 1
        else:  #choix_utilisateur > nombre_a_deviner: 
            print("Votre nombre est trop grand")
            i = i + 1
    if not trouve:
        print(f"Vous avez perdu, le nombre à deviner était {nombre_a_deviner}")   

jouer()
        

