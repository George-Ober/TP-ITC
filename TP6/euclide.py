def euclide (a, b):
    if b == 0:
        return 1 , 0
    else:
        u, v = euclide(b, a%b)
        return v, u - (a//b)*v
    
euclide(-186, 102)
