#programme qui calcule la distance entre points geographique
#cette fonction effectue des conversion de DMS vers DD
def convertir_DMS_vers_DD(degres,minutes,secondes,cardinalite):
    resultat = (minutes*60+secondes) / 3600 + degres
    if cardinalite == "S" or cardinalite == "W": 
            return -resultat
    return resultat

def point_vers_DD(point) :
    (deg1, min1, sec1, cardinalite1),(deg2, min2, sec2, cardinalite2)= point             
    xpointDD = convertir_DMS_vers_DD(deg1, min1, sec1, cardinalite1)
    ypointDD = convertir_DMS_vers_DD(deg2, min2, sec2, cardinalite2)
    return (xpointDD, ypointDD) 

def distance(point1,point2):
    #point1 = point_vers_DD(point_1)
    #point2 = point_vers_DD(point_2)
    xpoint1, ypoint1 = point1[0], point1[1]
    xpoint2, ypoint2 = point2[0], point2[1]
    resultat = (xpoint1-xpoint2)**2 + (ypoint1-ypoint2)**2
    return resultat**0.5

def saisie_info_file(file):
    f = open(file,"r")
    data_liste = f.readlines()
    f.close()
    return data_liste

def calcule_points_geo(data_liste, points:list[tuple], villes):
    n = len(data_liste)
    for i in range(n):
        line = data_liste[i]
        if i < n-1:  
            line = line[:len(line)-1]
        data = line.split(",")
        villes.append(data[0]) 
        atitude = (int(data[1]), int(data[2]), int(data[3]), data[4])
        longetitude= (int(data[5]), int(data[6]), int(data[7]), data[8])
        point = point_vers_DD((atitude,longetitude))
        points.append(point)

def distances_villes_pole_nord(file:str,villes, distance_list):
    pole_nord_2017 = point_vers_DD(((86, 5, 0,"N"),(172, 6, 0, "W")))
    
    points : list[tuple] = []
    data_list = saisie_info_file(file)
    calcule_points_geo(data_list, points, villes)
    for p in points:
        distance_list.append(distance(p,pole_nord_2017))

def affiche_distances_villes(distances, villes):
    for i in range(len(distances)):
        print(f"[{villes[i]}: {distances[i]:.3f}]", end = ";")
    print()


def calcule_position_proche_Pôle_nord(file:str):
    villes = []
    distances =[]
    distances_villes_pole_nord(file,villes, distances)
    min = distances[0]
    v = villes[0]
    for i in range(1,len(distances)):
        if min > distances[i]:
            v, min= villes[i], distances[i]
    print("Liste des villes avec leurs distances:")
    affiche_distances_villes(distances, villes) 
    #print(villes)
    #print("Liste des distances distances avec le pole nord:")
    #print(distances)

    print(f"La ville la plus proche du pole nord en 2017 est {v}")

calcule_position_proche_Pôle_nord("data.txt")
