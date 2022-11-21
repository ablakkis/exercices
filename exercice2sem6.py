import copy
def construire_liste():
    my_list = [[1, 2, 3, 4, 5]]
    print("Mon liste est:")
    print(my_list)
    surface = my_list[0].copy()
    profondeur = list(my_list[0])
    my_list.append(surface)
    my_list.append(profondeur)
    print(my_list)
    mot = input("Entrer un mot de votre choix: ")
    my_list[1][1] = mot
    my_list[2][2] = mot
    print(my_list)

construire_liste()

