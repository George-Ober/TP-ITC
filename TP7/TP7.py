
from random import randint


def poids(sac):
    return info(sac, 1)

def valeur(sac):
    return info(sac, 2)

def info(sac, k):
    return sum([sac[i][k] for i in range(len(sac))])

def presentation(sac):
    a = [item[0] for item in sac]
    a.append(poids(sac))
    a.append(valeur(sac))
    return a

def comp_valeur(objet1, objet2):
    return objet1[2] >= objet2[2]

def comp_poids(objet1, objet2):
    return objet1[1] >= objet2[1]

def comp_valeur_sur_poids(objet1, objet2):
    return objet1[2] / objet1[1] >= objet2[2] / objet2[1]

def tri_butin(butin, comp):
    n = len(butin)
    for i in range(n - 1):
        for k in range(n - 1):
            if comp(butin[k], butin[k + 1]):
                butin[k], butin[k + 1] = butin[k + 1], butin[k]

"""
liste_bidon = [randint(0, 100) for k in range(100)]
def relation(a, b):
    return a >= b

"""
e = [('A', 3, 200), ('B', 1, 300), ('C', 4, 500)]

# les mecs derriere qui faisaient genre de bosser quand il est passé

situation_a = [('A', 8, 4800), ('B', 5, 4000), ('C', 4, 3000), ('D', 1, 500)]

def remplir_sac(butin, comp, poids_total):
    sac = []
    tri_butin(butin, comp)
    poids = 0
    k = 0
    b = len(butin)
    while poids + butin[k][1] <= poids_total and k < b:
        sac.append(butin[k])
        poids += butin[k][1]
        k += 1
    return presentation(sac)

import itertools

def sacs_possibles(butin, poids_total):
    parties_trop_belles_pas_comme_mr_menard = list(itertools.chain(*(itertools.combinations(butin, k) for k in range(0, len(butin) + 1))))
    liste_des_meilleurs_pas_comme_mr_menard = []
    for partie in parties_trop_belles_pas_comme_mr_menard:
        if poids(partie) <= poids_total:
            liste_des_meilleurs_pas_comme_mr_menard.append(partie)
    liste_des_meilleurs_pas_comme_mr_menard[1:]
    return liste_des_meilleurs_pas_comme_mr_menard

def remplir_sac_optimal(butin, poids_total):
    possibles = sacs_possibles(butin, poids_total)
    meilleurs_trouves = []
    meilleure_valeur = 0
    for el in possibles:
        if valeur(el) > meilleure_valeur:
            meilleure_valeur = valeur(el)
            meilleurs_trouves = []
            meilleurs_trouves.append(el)
        elif valeur(el) == meilleure_valeur:
            meilleurs_trouves.append(el)
    return meilleurs_trouves


situation_d = [("A" ,	7,	9100),
("B" ,	6,	7200),
("C" ,	4,	4800),
("D" ,	3,	2700),
("E" ,	2,	2600),
("F" ,	1,	200)]