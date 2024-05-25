def sommeTableaux(t_1, t_2):
    res = []
    for i in range(len(t_1)):
        res.append(t_1[i] + t_2[i])
    return res

def sommeTableaux2(t_1, t_2):
    return [t_1[k] + t_2[k] for k in range(len(t_1))]

def sommeTableaux3(t_1, t_2):
    if len(t_1) != len(t_2): return print("Les listes n'ont pas la même longueur, données à revoir.")
    return [t_1[k] + t_2[k] for k in range(len(t_1))]