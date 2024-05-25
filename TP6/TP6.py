# Exercice 1

def s_entiers(n):
    if n == 0:
        return 0
    else:
        return n + s_entiers(n)

# Exercice 2
def add1(a, b):
    if a == 0:
        return b
    else:
        return 1 + add1(a - 1, b)

def add2(a, b):
    if b == 0:
        return a
    else:
        return 1 + add2(a, b - 1)

def add3(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    else:
        return 1 + add3(a - 1, b - 1) + 1

# Penser à trouver une troisieme fonction (nul)

# Exercice 3

def mult(a, b):
    if a == 1:
        return b
    else:
        return b + mult(a - 1, b)
    
# Exercice 4

def mult_Peano(a, b):
    if a == 0:
        return 0
    else:
        return add1(mult_Peano(a - 1, b), b)
mult_Peano(3, 4)

def exp_rec(x, n):
    if n == 0:
        return 1
    else:
        return x * exp_rec(x, n - 1)
    
# Exercice 6
def expor_rec(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp_rec(x * x, n//2)
    elif n % 2 == 1:
        return x * exp_rec(x * x, (n-1)//2)

# Ex 7
def mr(a):
    if len(a) == 1:
        return a[0]
    else:
        if a[0] <= a[1]:
            return mr(a[1:])
        elif a[0] > a[1]:
            return mr(a[0:1] + a[2:])
        
# Ex 8
def inverse(ch):
    if len(ch) == 0:
        return ''
    elif len(ch) == 1:
        return ch
    else:
        return ch[-1] + inverse(ch[1:-1]) + ch[0]
    
def creuse(n):
    print(n)
    creuse(n + 1)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_opti(n):
    liste_fibo = [0, 1]
    convergence_quotient = []

    for i in range(n):
        liste_fibo.append(liste_fibo[i] + liste_fibo[i + 1])
        if i >= 1:
            convergence_quotient.append(liste_fibo[i + 1] / liste_fibo[i])

    return liste_fibo