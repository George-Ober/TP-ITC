def trianglePascal(n):
    lignes = [[1, 0]]
    for i in range(1, n + 1):
        nouvelleLigne = []
        for j in range(n + 1):
            nouvelleLigne[j] = lignes[i - 1][j]
        lignes[i]