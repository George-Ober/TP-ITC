def f1(t):
   t.append(4)

def f2(t):
   return t.append(4)

def f3(t):
   t.append(4)
   return t

def complete(t):
    if len(t) <= 3:
        for i in range(4):
            t.append(0)
    else:
        for i in range(4):
            t.append(t[i])
    return t



def complete2(t):
    if len(t) <= 3:
        t.extend([0, 0, 0, 0])
    else:
        t.extend(t[:4])
    return t

