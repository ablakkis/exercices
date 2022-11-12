def addition_fraction(fraction_1,fraction_2):
    a, b = fraction_1
    c, d = fraction_2
    num = a*d + b*c
    denom = b*d
    return num, denom

def soustraction_fraction(fraction_1, fraction_2):
    a, b = fraction_2
    a, b = -a, -b
    return addition_fraction(fraction_1, (a, b))

def multiplication_fraction(fraction_1, fraction_2):
    a, b = fraction_1
    c, d= fraction_2
    return a*c, b*d

def division_fraction(fraction_1, fraction_2):
    a, b = fraction_2
    a, b = b, a
    return multiplication_fraction(fraction_1, (a,b))  
    
def fraction_to_str(fraction):
    a, b = fraction
    return str(a) + '/' + str(b) +': '
def affiche_fraction(fraction):
    a, b = fraction
    print((fraction_to_str(fraction), a/b))
    
affiche_fraction((3,2)) 
   