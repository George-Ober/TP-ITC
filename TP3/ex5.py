def rech_mot(t: str, m: str):
    n = len(m)

    for i in range(len(t)):
        j = 0
        while i + j < len(t) and j < n and t[i + j] == m[j]:
            j += 1
        if j == n: return i

def rechs_mot(t: str, m: str):
    n = len(m)
    
    for i in range(len(t)):
        if t[i:(i+n)] == m: return i

rech_mot('Jeffrey David Ullman', 'David')
rechs_mot('Jeffrey David Ullman', 'David')


def recha_mot(texte, motif):
    t = len(texte)
    m = len(motif)
    i_max = t - m

    for i in range(0, i_max - 1):
        j = 0
        while j <= m - 1 and motif[j] == texte[i+j]:
            j += 1
        if j > m - 1:
            return i

print(recha_mot('Jeffrey David Ullman', 'David'))