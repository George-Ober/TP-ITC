from random import randint

def proba_paire(n):
    count = 0
    for i in range(n):
        de1 = randint(1,6)
        de2 = randint(1,6)

        if de1 == de2:
            count += 1
    
    return count / n