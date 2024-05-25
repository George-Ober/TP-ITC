def sommeTermes(t):
	if len(t) == 0: return None
	a = 0
	for k in range(len(t)):
		a += t[k]
	return a

def sommeTermesPonderes(t):
	if len(t) == 0: return None
	a = 0
	for k in range(len(t)):
		a += t[k] * (k + 1)
	return a