def count_letters():
    counters = [0]*26 
    print("Enter your text, empty line to indicate text end")
    fin = False
    while not fin:
        line = input()
        if len(line) == 0:
            fin = True
        else:
            for ch in line:
                if ord('A') <= ord(ch) <= ord('Z'):
                    index = ord(ch) - ord('A')
                    counters[index] = counters[index] + 1
                elif ord('a') <= ord(ch) <= ord('z') :
                    index = ord(ch) - ord('a')
                    counters[index] = counters[index] + 1
    return counters    

def display_counters(counters):
    a = ord('A')
    for i in range(len(counters)):
        print(f"[{chr(a+i)} : {counters[i]}]", end =" ")

def statistictis_on_texte() :
    counters = count_letters()
    display_counters(counters)

statistictis_on_texte()


   
