def exp_th(x, n):
    """
    Entrée: x (float), n (int)
    Sortie: x**n (float)
    Calcul naif en effectuant n - 1 multiplications
    """
    p = 1
    

    for k in range(n - 1, -1, -1):
        p = p * x
        assert p * x**k == x**n

    return p