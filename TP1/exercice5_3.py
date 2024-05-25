def calcule(t, op):
    if len(t) == 0: return None

    match op:
        case "+":
            a = 0
            for i in range(len(t)):
                a += t[i]
            return a
        case "*":
            a = 1
            for i in range(len(t)):
                a = a * t[i]
            return a
        case "-":
            a = 0
            for i in range(len(t)):
                a -= t[i]
            return a
        case "/":
            a = 1
            for i in range(len(t)):
                a = a * t[i]
            return 1/a
        case _:
            print("Le calcul demandé est vraiment mal défini")
            
