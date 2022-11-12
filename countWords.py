#Ce programme a pour but de calculer le nombre de mots dans un texte tapé au clavier
#La saisie s'arrete lorsque l'utilisateur tape deux enters successif
def count_words():
    word_counter = 0 # au début le compteur est 0
    separators = "./$#@!\\ =*&(){}[];:,<>%+-_|€¥¥\'\"\n\t"   #séparateurs entre les mots
    print("Enter your texte, empty line to stop input")
    fin = False
    previous_sep = True
    while not fin:
        line = input()
        if len(line) == 0:
            fin = True
        else:
            for ch in line:
                if ch in separators:
                    if not previous_sep:
                        word_counter = word_counter + 1 # on est arrivé a un separateur et 
                                                        # precedent n'est pas separateur on incremente 
                                                        # le compteur de mots 
                    previous_sep = True            
                else:
                    previous_sep = False
    return word_counter

def statistictis_about_texte() :
    counters = count_words()
    print(f"Number of words in our texte is : {counters}")

statistictis_about_texte()
                