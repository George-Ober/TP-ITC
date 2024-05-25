def comptage(s):
    a = {}

    for el in s:
        if el in a.keys():
            a[el] += 1
        else:
            a[el] = 1
    return a