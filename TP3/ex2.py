def maximum(a):
    m = a[0]
    for i in range(len(a)):
        if a[i] > m:
            m = a[i]
    return m

def deuxmax(a):
    if len(a) == 1: return (a[0], a[0])
    truc = [a[0], a[1]]
    if a[1] > a[0]:
        truc = truc[::-1]
    
    for i in range(1, len(a)):
        if a[i] >= truc[1]:
            if a[i] >= truc[0]:
                truc[1] = truc[0]
                truc[0] = a[i]
            else:
                truc[1] = a[i]
    return (truc[0], truc[1])

deuxmax([7, 1, 4, 6, 7, 5])