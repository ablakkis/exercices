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
    return a*b, c*d
def division_fraction(fraction_1, fraction_2):
    a, b = fraction_2
    a, b = b, a
    return multiplication_fraction((a,b))  
def fraction_to_str(fraction):
    a, b = fraction
    return str(a) + '/' + str(b) +':'
def affiche_fraction(fraction):
    a, b = fraction
    print((fraction_to_str(fraction) + str(a/b)))
fraction_result = addition_fraction((3,5),(4,6))
affiche_fraction(fraction_result)
fraction_result = soustraction_fraction((3,5),(4,6))
affiche_fraction(fraction_result)
fraction_result= multiplication_fraction((3,5),(4,6))
affiche_fraction(fraction_result)
fraction_result = division_fraction((3,5),(4,6))
affiche_fraction(fraction_result)


   