def fib_opti(n):
    liste_fibo = [0, 1]
    convergence_quotient = []

    for i in range(n):
        liste_fibo.append(liste_fibo[i] + liste_fibo[i + 1])
        if i >= 1:
            convergence_quotient.append(liste_fibo[i + 1] / liste_fibo[i])

    return liste_fibo

print(fib_opti(10000))