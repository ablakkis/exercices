#exercice 3
import datetime as dt
from operator import truediv
def anniversaire(date_auj):
    jour = int(input("Entre votre jour de naissance: "))
    mois = int(input("Entre votre mois de naissance: "))
    jour_auj, mois_auj = date_auj
    if jour ==jour_auj and mois == mois_auj :
        print("Bonne fete")
    else :
        printf("Ce n'est ta fete aujourd'hui")

#jra = dt.datetime.today().day
#moa = dt.datetime.today().month
#2anniversaire((jra,moa))

def pair_impaire() :
    premier = int(input("Entre ton premier entier: "))
    second = int(input("Entre votre deuxieme entier: "))
    if premier % 2 == 0 and second % 2 == 1 :
        print(f" Votre nombre impair est {second}, votre nombre pair est {premier} et le résultat de leur division est égal à:", premier/second)
    elif  premier % 2 == 1 and second % 2 == 0 :
        print(f" Votre nombre impair est {premier}, votre nombre pair est {second} et leur division est egal à:", premier/second)
    else:
        print ("Mauvaise entree: Les deux nombre ne doivent pas etre tous les deux pairs ou impairs ")

#pair_impaire()

def saisie_date() :
    jour   = int(input("Entre ton jour de naissance: "))
    mois = int(input("Entre votre mois de naissance: ")) 
    annee = int(input("Entre votre annee de naissance: ")) 
    if(jour <= 0 or jour > 31) :
        print("Mauvaise jour de naissance le programme quit.......")
        return 0, 0, annee
    if(mois <=0 or mois > 12):
        print("Mauvaise mois de naissance le programme quit...")
    return (jour, mois, annee)
def si_printemps(date):
    jour, mois = date;
    if 3 <= mois <= 6 (mois >= 3 and mois <= 6) :
        if(jour < 21 and mois == 3):
            return False
        elif jour > 21 and mois == 6 :
            return False
        return True
    else : 
        return False   
def si_hiver(date):
    jour, mois = date
    if 1<= mois <= 3:
      if mois == 3 and jour >= 21:
           return False
      return True       
    if(mois == 12 and jour < 21) :
        return False
    if mois == 12 :
        return True
    return False

def si_ete(date):
    jour, mois = date
    if(6 <= mois<= 9) :
        if (mois == 6 and jour < 21):
            return False
        if    

def saison_naissance(date):
    jour, mois, annee = saisie_date()
    if jour == 0 or mois == 0 :
        return
    if si_printemps():
        print("tu es ne en printemps")
    elif si_hiver() :
        print("tu es ne en hiver")
    elif si_ete() :
        print("tu es ne en ete") 
    else:
       print("tu es ne en hiver") 
 




        
       


