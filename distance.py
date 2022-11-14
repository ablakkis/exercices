#programme qui calcule la distance entre deux point
#cette fonction effectue des conversion de DMS vers DD
def convertir_DMS_vers_DD(degres,minutes,secondes,cardinalite):
    resultat = (minutes*60+secondes) / 3600 + degres
    if cardinalite == "S" or cardinalite == "W": 
            return -resultat
    else:
        return resultat

def point_vers_DD(point) :
    ((degres1, minutes1, secondes1, cardinalite1),(degres2, minutes2, secondes2, cardinalite2))= point               
    xpointDD = convertir_DMS_vers_DD(degres1, minutes1, secondes1, cardinalite1)
    ypointDD = convertir_DMS_vers_DD(degres2, minutes2, secondes2, cardinalite2)
    return xpointDD, ypointDD 

def distance(point_1,point_2):
    point1 = point_vers_DD(point_1)
    point2 = point_vers_DD(point_2)
    xpoint1, ypoint1 = point1
    xpoint2, ypoint2 = point2
    resultat = (xpoint1-xpoint2)**2 + (ypoint1-ypoint2)**2
    return resultat**0.5

def saisie_points_file(fichier):
    f = open(fichier,"r")
    data_liste = f.readlines()
    f.close()
    return data_liste

def calcule_donnee_point(data):
    list_longitude = [int(data[0]), int(data[1]) int(data[2]), data[3]]
    list_atitude = [int(data[4]), int(data[5]) int(data[6]), data[7]]
    return list_longitude, list_atitude

def tirer_Points(points:list[tuple]):
  data_liste = saisie_points_file("data.txt")
  for data in data_liste:
    liste_donnee = data.split(",")
    resultat = calcule_donnee_point(liste_donnee)
    points.append(resultat)


print("Entre votre point on commence par l'attitude") 
degres = int (input())
minutes = int(input()) 
secondes= int(input()) 
cardinalite = input()
degres1 = int (input())
minutes1 = int(input()) 
secondes1 = int(input()) 
cardinalite1 = input() 
point1 = ((degres,minutes,secondes,cardinalite),(degres1,minutes1,secondes1,cardinalite1) )
point2 = ((86, 5, 0, "N"),(172,6,0,"W"))
d = distance(point1,point2)
print(f"Distance avec le point nord magnetique en 2017 est: {d}")
    

