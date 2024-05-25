def spositif(d):
    """
        Cette méthode renvoie la séropositivité du dictionnaire qui est entré.
    """
    a = {}
    for i in d:
        if d[i] > 0:
            a[i] = d[i]
    return a

a = { 
    "a": 1,
    "b": 0,
    "c": 3,
}

spositif(a)