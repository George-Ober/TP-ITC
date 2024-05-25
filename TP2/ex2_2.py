def ordre_lexico(a: tuple, b:tuple):
    return a[0] < b[0] or (a[0] == b[0] and a[1] <= b[1])