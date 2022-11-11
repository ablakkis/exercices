def prime_number(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for d in range(3, n // 2 + 1 , 2) :
            if(n % d == 0): 
                return False
        return True

def go():
    ok = False
    while not ok: 
        a = int(input("Entre un nombre entier superieur ou egale a 2: "))
        if a >= 2:
            ok = True
        else:
            print("Nombre invalid ")
    if(prime_number(a)):
        print(f"{a} est un nombre premier") 
    else: 
        print(f"{a} est un nombre non premier")   

go()



