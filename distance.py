#programme qui calcule la distance entre deux point
#cette fonction effectue des conversion de DMS vers DD
def convertir_DMS_vers_DD(degres,minutes,secondes):
    resultat = (minutes*60+secondes) / 3600 + degres
    return resultat
def point_vers_DD(point_DMS) :
    degres1, minutes1, secondes1, degres2, minutes2, secondes2= point_DMS
    xpointDD = convertir_DMS_vers_DD(degres1,minutes1,secondes1)
    ypointDD = convertir_DMS_vers_DD(degres2,minutes2,secondes2)
    return xpointDD,ypointDD 
def distance(point_1,point_2):
    point1 = point_vers_DD(point_1)
    point2 = point_vers_DD(point_2)
    xpoint1, ypoint1 = point1
    xpoint2, ypoint2 = point2
    resultat = (xpoint1-xpoint2)**2 + (ypoint1-ypoint2)**2
    return resultat**0.5

d = distance((30,40,50,45,55,25),(35,45,55,35,25,45))
print("distance entre les deux points:",d)
    

