def creer_pile_vide():
    # Renvoie une pile vide
    return []


def empiler(e, p):
    p.append(e)


def depiler(p):
    sommet = p.pop()
    return sommet


def est_pile_vide(p):
    return len(p) == 0


def creer_file_vide():
    return []


def enfiler(e, f):
    f.append(e)


def defiler(f):
    e = f.pop(0)
    return e


def est_file_vide(f):
    return len(f) == 0


def sommet(p):
    assert not est_pile_vide(p)
    s = depiler(p)
    empiler(s, p)
    return s

def taille_pile(p):
    s = creer_pile_vide()
    n = 0
    while not est_pile_vide(p):
        empiler(depiler(p), s)
        n += 1

    while not est_pile_vide(s):
        empiler(depiler(s), p)

    return n

def taille_file(f):
    j = creer_file_vide()
    n = 0
    while not est_file_vide(f):
        enfiler(defiler(f), j)
        n += 1

    while not est_file_vide(j):
        enfiler(defiler(j), f)

    return n

# Exercice 2.1.3

def permuter_somet(p):
    n = taille(p)
    if n > 1:
        a = depiler(p)
        b = depiler(p)
        empiler(a, p)
        empiler(b, p)

def renvoyer(k, p):
    b = creer_pile_vide()
    n = 0
    a = None
    while n < k and not est_pile_vide(p):
        a = depiler(p)
        empiler(a, b)
        n += 1

    while not est_pile_vide(b):
        empiler(depiler(b), p)

    return None if n != k else a


def tete(f):
    a = defiler(f)
    b = creer_file_vide()
    enfiler(a, b)
    while not est_file_vide(f):
        enfiler(defiler(f), b)

    while not est_file_vide(b):
        enfiler(defiler(b), f)

    return a

def deverser(p_1, p_2):
    while not est_pile_vide(p_1):
        empiler(depiler(p_1), p_2)

def extraire_positif(p):
    a = creer_pile_vide()
    b = creer_pile_vide()
    
    while not est_pile_vide(p):
        j = depiler(p)
        if j > 0:
            empiler(j, a)
        empiler(j, b)

    n = 0
    while not est_pile_vide(a):
        empiler(depiler(a), p)
        n += 1

    while not est_pile_vide(p):
        empiler(depiler(p), b)

    k = 0
    while k < n:
        empiler(depiler(b), a)
        k += 1

    while not est_pile_vide(b):
        empiler(depiler(b), p)

    return a

# Méthode VB

def extraire_positif2(p):
    a = creer_pile_vide()
    b = creer_pile_vide()
    while not est_pile_vide(p):
        k = depiler(p)
        empiler(k, a)
        if k > 0:
            empiler(k, b)
    
    deverser(a, p)
    deverser(b, a)
    return a

def parentheses(m):
    a = creer_pile_vide()
    for car in m:
        if car == "(":
            empiler('c', a)
        elif car == ")":
            if est_pile_vide(a): return False
            depiler(a)
    return est_pile_vide(a) 

def evalue(expr :str) -> int:
    pile = creer_pile_vide()
    for s in expr:
        if s == "+":
            a = depiler(pile)
            b = depiler(pile)
            empiler(a + b, pile)
        elif s == "*":
            a = depiler(pile)
            b = depiler(pile)
            empiler(a * b, pile)
        elif s == "-":
            a = depiler(pile)
            b = depiler(pile)
            empiler(a - b, pile)
        else:
            empiler(int(s), pile)
    
    return depiler(pile)

evalue("123*+4*")


def heise_kartoffel(f, k):
    N = taille_file(f)
    n = N
    while n > 1:
        j = 0
        while j < k:
            enfiler(defiler(f), f)
            j += 1
        defiler(f)
        n -= 1

    return defiler(f)

def george():
    a = []
    truc = "george"
    for s in truc:
        empiler(s, a)

    return a


class Pile:
    def __init__(self):
        self.val = []

    def empiler(self, v):
        self.val.append(v)

    def depiler(self):
        return self.val.pop()
    
    def taille_pile(self):
        return len(self.val)

    def est_pile_vide(self):
        return len(self.val) == 0
