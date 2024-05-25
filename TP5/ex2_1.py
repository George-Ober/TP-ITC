

from random import *
import time


def occurences(t: list):
    occ = {}
    for el in t:
        if el in occ:
            occ[el] += 1
        else:
            occ[el] = 1
    return 


def test_egalite_dico_1(d1: dict, d2: dict):
    if len(d1) != len(d2):
        print("Les deux dictionnaires n'ont carrement pas la meme longueur")
        return False
    
    for el in d1:
        if d2[el] != d1[el]:
            print("L'element %s n'a pas le meme nombre d'occurences dans d2 (%s) et dans d1 (%s)" % (el, d2[el], d1[el]))
            return False
    
    return True

def test_egalite_dico_2(d1: dict, d2: dict):
    for cle in d1:
        assert cle in d2, "%s est une cle de %s et non de %s" %(cle, d1, d2)
        assert d1[cle] == d2[cle], "l'element %s n'a pas le meme nb dans les deux tableaux" %(cle)
    
    for cle in d2:
        assert cle in d1, "%s est une cle de %s et non de %s" %(cle, d1, d2)
        assert d1[cle] == d2[cle], "l'element %s n'a pas le meme nb dans les deux tableaux" %(cle)

def bien_ordonne(t):
    for i in range(len(t) - 1):
        assert t[i] <= t[i + 1], "Les elements d'indices %s et %s ne sont pas dans l'ordre" %(i, i + 1)

def test_tri(t, tri):
    occurences_avant = occurences(t)
    tri(t)
    occurences_apres = occurences(t)
    
    test_egalite_dico_1(occurences_avant, occurences_apres)

    bien_ordonne(t)

def tableau_aleatoire(n, a, b):
    return [randint(a, b) for k in range(n)]


def chrono(tri, t):
    t1 = time.time()
    tri(t)
    t2 = time.time()
    return t2 - t1

def temps_moyen(tri, nb, n, a, b):
    temps = 0
    for i in range(nb):
        t = tableau_aleatoire(n, a, b)
        temps += chrono(tri, t)
    
    return temps / nb

def minimum(t, k):
    min_indice = t[k]
    indice = k
    for i in range(k, len(t)):
        if t[i] < min_indice:
            indice = i
            min_indice = t[i]
    
    return indice

def tri_selection(t):
    n = len(t)
    for k in range(n):
        i_min = minimum(t, k)
        
        a = t[k]
        t[k] = t[i_min]
        t[i_min] = a

    return t

tri_selection([3, 2, 3, 3, 2, 1, 2, 3, 1, 2])


def insere(t, k):
    k = k
    
    while k > 0 and t[k] < t[k - 1]:
        t[k], t[k - 1] = t[k - 1], t[k]
        k -= 1


def tri_insertion(t):
    n = len(t)
    for i in range(1, n):
        insere(t, i)

def histo(t, b_max):
    histo = [0] * len(t)
    for el in t:
        histo[el] += 1
        