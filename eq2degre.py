import math

def delta(coeficient):
    a, b, c = coeficient
    return b*b - 4*a*c

def calcule_racines(coefficient):
    a, b, c = coefficient
    d = delta(coefficient)
    if d < 0:
        return ()
    else:
        x1 = (- b - math.sqrt(d))/(2*a)
        x2 = (- b + math.sqrt(d))/(2*a)
        return x1, x2

def saisie_coefficients():
    a = float(input("Le premier coefficient? "))
    b = float(input("Le seconnd coefficient? "))
    c = float(input("Le troisieme coefficient? "))
    return a, b, c

def resolution():
    coefficient = saisie_coefficients()
    r = calcule_racines(coefficient)
    if r:
        x1, x2 = r
        print(f"Les racines sont {x1:.2f} {x2: .2f} ")
    else:
        print("Pas de racines")
resolution()