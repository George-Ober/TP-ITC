from math import *

def ensemble_diviseurs(n):
    a = set()
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            a.add(int(i))
            a.add(int(n/i))
        i += 1
    return a

def sommediviseurs(n):
    div = ensemble_diviseurs(n)
    s = 0
    for i in div:
        s += i
    return s
    

def recherche_parfait(p):
    a = []
    n = 1
    while len(a) < p:
        if sommediviseurs(n) == 2*n:
            a.append(n)
        n += 1
    return a


def plus_petit_abondant(a):
    n = a
    while True:
        if sommediviseurs(n) > 2*n and n % 2 == 1:
            return n
        n += 1

print(plus_petit_abondant(0))