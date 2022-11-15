def saisie_info_file(file):
    f = open(file,"r")
    texte = f.readlines()
    f.close()
    return texte
def count_words():
    word_counter = 0 # au début le compteur est 0
    separators = "./$#@!\\ =*&(){}[];:,<>%+-_|€¥¥\'\"\n\t"   
    #liste des séparateurs entre les mots
    print("Lecture du ")
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
    