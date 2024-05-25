# (Copyright (c) 2024 George Ober. All Rights Reserved.

peres = {
    'a': 'r',
    'b': 'a',
    'c': 'r',
    'd': 'r',
    'e': 'r',
    'f': 'e',
    'g': 'c',
    'h': 'c'
}

# def conversion(peres, r):
#     for (i, j) in peres.items():
#

def chemin(pcc, r, x):
    """
        Prend en entrée une arborescence des peres, une origine et renvoie la chaine liant ces deux points si elle existe
    """
    if x in pcc.keys():
        choisi = x
        a = [x]
        while choisi != r:
            choisi = pcc[choisi]
            a.append(choisi)

        return a[::-1]
    elif x == r:
        return [r]
    else:
        return []


def test(d, v):
    for (i, j) in d.items():
        if j == v: return True
    return False

def cle_de_valeur_mini(etat, dist, e):
    """
    Prend en arguments deux dictionnaires etat et dist ayant les memes cles, e une valeur du dictionnaire etat, et qui renvoie (parmi les clés de etat de valeur e) une clé dont la valeur dans le dictionnaire dist est minimale.
    """
    # Extrayons toutes les cles de `etat` de valeur e
    liste_cles = []
    mini = float('inf')

    cle = None
    for (i, j) in etat.items():
        if j == e and dist[i] < mini:
            cle = i
            mini = dist[i]
    return cle

# inatteignable

gr = {
    'a' : [('c', 2), ('b', 8), ('d', 1)],
    'b' : [('a', 8), ('c', 4), ('d', 6), ('e', 1)],
    'c' : [('a', 2), ('b', 4), ('e', 2)],
    'd' : [('a', 1), ('b', 6)],
    'e' : [('b', 1), ('c', 2)]
}

def dijkstra(g, s):
    etat = {k: 'blanc' for k in g.keys()}
    etat[s] = 'gris'
    dist = {k: float('inf') for k in g.keys()}
    dist[s] = 0

    pcc = {}

    while test(etat, 'gris'):
        s_proche = cle_de_valeur_mini(etat, dist, 'gris')
        for v,w in g[s_proche]:
            if etat[v] == 'blanc':
                etat[v] = 'gris'
                dist[v] = dist[s_proche] + w
                pcc[v] = s_proche
            elif etat[v] == 'gris':
                if dist[s_proche] + w < dist[v]:
                    dist[v] = dist[s_proche] + w
                    pcc[v] = s_proche
        etat[s_proche] = 'noir'
    
    return (dist, pcc)


achat = [20000 for k in range(7)]
# achat[i] : coût d'un véhicule neuf acheté le 1er janvier de l'année i
revente = [0, 14000, 12000, 8000, 6000, 4000, 2000]
# revente[i] : prinx de revente d'un véhicule neuf acheté et utilisé pendant i années
entretien = [0, 600, 1000, 1600, 2400, 3200, 4400]
# entretien[i] cout entretien au cours de la ieme année
# i < j

def graphe_choix_eco(n, achat, entretien, revente):
    liste = {k: [] for k in range(0, n + 1)}

    for i in range(n):
        for k in range(i + 1, n + 1):
            # Calculer le cout i -> k
            liste[i].append((k, cout(k - i, achat, entretien, revente)))

    return liste

def cout(k, achat, entretien, revente):
    n = achat[0]
    for j in range(k + 1):
        n += entretien[j]

    n -= revente[k]
    return n
