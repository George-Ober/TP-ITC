from math import sqrt
from random import randint

liste_test = [0, 3, 5, 6, 8,  9, 12, 13, 16, 17, 22, 24]

def recherche_dichoto(x, a):
    m = 0
    n = len(a) - 1
    tableau = [[m, n]]
    compa = 0

    while m <= n:
        u = randint(m, n)
        compa += 1
        if a[u] == x:
            return (u, compa)
        elif a[u] < x:
            m = u + 1
            tableau.append([m, n])
        elif a[u] > x:
            n = u - 1
            tableau.append([m, n])
    return (None, compa)
        
recherche_dichoto(10, liste_test)

grosse_liste = [randint(0, 100000) for k in range(10000)]
grosse_liste.sort()

def recherche_dichoto_milieu(x, a):
    m = 0
    n = len(a) - 1
    tableau = [[m, n]]
    compa = 0

    while m <= n:
        u = (m + n) // 2
        compa += 1
        if a[u] == x:
            return (u, compa)
        elif a[u] < x:
            m = u + 1
            tableau.append([m, n])
        elif a[u] > x:
            n = u - 1
            tableau.append([m, n])
    return (None, compa)


def stat():
    somme_moyenne = 0
    somme_ecartype = 0
    N = 1000
    valeurs_trouvees = []
    for i in range(N):
        j = recherche_dichoto_milieu(500.5, grosse_liste)
        valeurs_trouvees.append(j[1])
        somme_moyenne += j[1]
    
    moyenne = somme_moyenne / N

    for i in range(N):
        somme_ecartype += (valeurs_trouvees[i] - moyenne)**2
    
    ecartype = sqrt(somme_ecartype / N)

    return (moyenne, ecartype)

stat()