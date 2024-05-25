def somme1(n):
    somme = 0
    for i in range(n + 1):
        for j in range(1, i + 1):
            somme += 2**i + j ** 5
    return somme

def somme2(n):
    somme = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            somme += i*j
    return somme

def somme3(n, p):
    somme = 0
    for i in range(1, n + 1):
        for j in range(i, p + 1):
            somme += j**i
    return somme