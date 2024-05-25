def convertirBase2(t):
    for i in range(len(t)):
        t[i] = t[i] % 2

def denombreModulo3(t):
    compte = [0, 0, 0]
    for i in range(len(t)):
        compte[t[i] % 3] += 1
    return compte

def denombreModulop(t, p):
    if p < 2: return 
    compte = [0] * p
    for i in range(len(t)):
        compte[t[i] % p] += 1
    return compte