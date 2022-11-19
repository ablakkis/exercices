def affiche_triangle(n):
    for i in range(n//2 + 1):
        for j in range(i+1):
            print("*", end = " ")
        print()
    for i in range(n//2, 0 , -1):
        for j in range(i):
            print("*", end = " ")
        print()
n = int(input("Number of lines(must be odd)? "))
affiche_triangle(n)
