def vpp(a):
    leq = -1
    ideq = [-1, -1]
    for i in range(len(a)):
        for j in range(len(a)):
            v1 = a[i]
            v2 = a[j]
            if i != j and v1 - v2 >= 0 and (v1 - v2 < leq or leq == -1):
                leq = v1 - v2
                ideq = [v1, v2]
    
    return (ideq[0], ideq[1])
