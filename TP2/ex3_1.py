from math import *

def ajoute_fractions(f, g):
    p0 = f[0]
    q0 = f[1]
    p1 = g[0]
    q1 = g[1]

    b = q0 * q1

    a = p0 * q1 + q0 * p1

    return [a, b]

def soustrait_fractions(f, g):
    p0 = f[0]
    q0 = f[1]
    p1 = g[0]
    q1 = g[1]

    b = q0 * q1
    a = p0 * q1 - q0 * p1

    return [a, b]

def decomp_valide(t):
    u = t[1]
    s = [0, 1]
    for i in range(1, len(t)):
        if t[i] <= u and i > 1:
            return False
        s = ajoute_fractions(s, [1, t[i]])
        u = t[i]
    return s[0] / s[1] == t[0][0] / t[0][1]
        

""" assert decomp_valide([[1, 2], 2])
assert not decomp_valide([[1, 2], 4, 4])
assert not decomp_valide([[1, 2], 4, 8, 8])
assert decomp_valide([[3, 16], 6, 48])
assert not decomp_valide([[3, 16], 6, 176, 66])
assert decomp_valide([[3, 16], 6, 66, 176]) """

def partie_entiere_sup(p, q):
    return q // p + 1

def algo_Fibo(t):
    p = t[0]
    q = t[1]
    r = []
    while p != 1:
        a = partie_entiere_sup(p, q)
        r.append([1, a])
        [p, q] = soustrait_fractions([p, q], [1, a])
        d = gcd(int(p), int(q))
        [p, q] = [int(p/d) , int(q/d)]
    return r

#algo_Fibo([5, 2])

def seuil_harmonique(x):
    s = 1
    n = 1
    while s <= x:
        n += 1
        s += 1/n
    return n

print(seuil_harmonique(29/12))