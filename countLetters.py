#Programme qui calcule le nombre d'occurence de chaque lettre dans un texte tapé au clavier
def count_letters():
    counters = [0] * 26  # 26 est le nombre de lettre dans l'alphabet
    print("Enter your texte, empty line to stop input")
    fin = False
    while not fin:
        line = input()
        if len(line) == 0:
            fin = True
        else:
            for ch in line:
                if ord('A') <= ord(ch) <= ord('Z'): #On regarde si le caractere lu est une lettre majuscule
                    index = ord(ch) - ord('A')
                    counters[index] = counters[index] + 1
                elif ord('a') <= ord(ch) <= ord('z') : #On regarde si le caractere lu est une lettre majuscule
                    index = ord(ch) - ord('a')
                    counters[index] = counters[index] + 1
    return counters    

def display_counters(counters):
    a = ord('A')
    for i in range(len(counters)):
        print(f"[{chr(a+i)} : {counters[i]}]", end =" ")

def statistictis_about_texte() :
    counters = count_letters()
    display_counters(counters)

statistictis_about_texte()


   
