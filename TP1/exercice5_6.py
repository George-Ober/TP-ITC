def maxi(t):
    if len(t) == 0: return None
    trouve = t[1]
    for i in range(len(t)):
        if t[i] > trouve:
            trouve = t[i]
    return trouve

def maxi_mult(t):
    if len(t) == 0: return None
    trouve = t[1]
    compte = 1
    for i in range(len(t)):
        if t[i] == trouve:
            trouve = t[i]
            compte += 1
        elif t[i] > trouve:
            trouve = t[i]
            compte = 1
    return [trouve, compte]