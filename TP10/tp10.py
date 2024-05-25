import random

liste_gr1 = {
    "a": ["b", "c"],
    "b": ["a", "d"], 
    "c": ["a", "e"],
    "d": ["b", "f", "e"],
    "e": ["c", "d", "f", "h"],
    "f": ["d", "e", "g"],
    "g": ["f"],
    "h": ["e"],
    "i": ["j", "k"],
    "j": ["i", "k"],
    "k": ["i", "j"]
}

alphabet = "abcdefghijklmnopqrstuvwxyz"

matrice_gr1 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

def degre_liste(gr, s):
    return len(gr[s])

def degre_matrice(gr, s):
    voisins = gr[s - 1]
    n_voisins = 0

    for b in voisins:
        n_voisins = n_voisins + b

    return n_voisins

def egal(ar1, ar2):
    return (ar1[0] == ar2[1] and ar1[1] == ar2[0]) or (ar1[0] == ar2[0] and ar1[1] == ar2[1])

def arretes(gr):

    complet = []

    for depart in gr:
        for arrivee in gr[depart]:
            conjugue = [arrivee, depart]
            if not ([depart, arrivee] in complet or conjugue in complet):
                complet.append([depart, arrivee])

    return complet

def n_arretes(gr):
    return len(arretes(gr))

def n_sommets(gr):
    return len(gr)

def graphe_complet(n):
    graphe = {}

    for i in range(n):
        graphe[i] = [j for j in range(n) if i != j]
        # for j in range(n):
        #     if j != i:
        #         graphe[i].append(j)

    return graphe

def explorer(gr, s):
    C = [s]
    marque = []

    while not len(C) == 0:
        i = random.randint(0, len(C) - 1)
        v = C.pop()
        if not v in marque:
            marque.append(v)
            for voisin in gr[v]:
                if not voisin in marque:
                    C.append(voisin)

    return marque

def dFS_gen(G, s):
    C = [s]
    marque = []

    while not len(C) == 0:
        v = C.pop()
        if not v in marque:
            marque.append(v)
            # Ordre lexicographique négligé
            for voisin in G[v]:
                if not voisin in marque:
                    C.append(voisin)

    return marque

def comp_connexes(gr):
    sommets = list(gr.keys())

    composantes = []

    while not len(sommets) == 0:
        nouvelle = dFS_gen(gr, sommets[0])
        for i in nouvelle:
            sommets.remove(i)
        composantes.append(nouvelle)
    
    return composantes

def DFS_class(gr, s):
    p = [s]
    marque = [s]

    while not len(p) == 0:
        v = p[-1]

        un_voisin_non_marque = False

        for voisin in gr[v]:
            if voisin not in marque:
                un_voisin_non_marque = True
                p.append(voisin)
                marque.append(voisin)

        if not un_voisin_non_marque:
            p.pop(-1)

    return marque

def DFS_class_vue_pile(gr, s):
    p = [s]
    marque = [s]

    print(p)

    while not len(p) == 0:
        v = p[-1]

        un_voisin_non_marque = False

        for voisin in gr[v]:
            if voisin not in marque:
                un_voisin_non_marque = True
                p.append(voisin)
                marque.append(voisin)

        if not un_voisin_non_marque:
            p.pop(-1)

        print(p)

    return marque

def DFS(gr, s):
    marque_rec = []

    def DFS_rec(gr, s):
        marque_rec.append(s)
        for v in gr[s]:
            if v not in marque_rec:
                DFS_rec(gr, v)

    DFS_rec(gr, s)
    return marque_rec
