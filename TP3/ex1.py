def existef(s, x):
    for element in s:
        if element == x:
            return True
    return False

def existefi(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return True
    return False

def existefw(s, x):
    i = 0
    n = len(s)

    while 1 <= n - 1 and s[i] != x:
        i += 1
    return True if i <= n - 1 else False