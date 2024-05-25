def somme_chiffres():
    a = 0
    n = int(input("Veuillez entrer un nombre entier"))
    for i in range(0, n+1):
        a += i
    return a
