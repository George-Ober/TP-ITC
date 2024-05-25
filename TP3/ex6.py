from random import randint

def alea(n):
    return [randint(0, 1E6) for k in range(1, n)]

def tri_bulles(a):
    n = len(a)

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a