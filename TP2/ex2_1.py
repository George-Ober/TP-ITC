def recherche_elt(s, elt):
    for i in range(len(s)):
        if s[i] == elt:
            return i
    return None