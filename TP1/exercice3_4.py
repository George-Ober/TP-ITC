def affiche_etat_reponse(booleen):
	print("*---*\nSolution %s.\n*---*"%("correcte" if booleen else "fausse"))

def separe():
	print("*---*")

def affiche_etat_reponse2(booleen):
	separe()
	print("Solution %s."%("correcte" if booleen else "fausse"))
	separe()

def separe2(motif):
	print(motif)


def affiche_etat_reponse3(booleen, motif):
	separe2(motif)
	print("Solution %s."%("correcte" if booleen else "fausse"))
	separe2(motif)
