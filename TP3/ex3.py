def occurences(s, x):
    count = 0
    for el in s:
        if el == x:
            count += 1
    return count