sexe = int(input("Quel est votre sexe?\n1. Masculin\n2. Féminin\n"))

nom = input("Entrez votre nom\n")

commande = input("Entrez votre Numéro de Commmande\n")

print("%s %s,\nle suivi de votre commande numéro %s est disponible dans votre espace client.\nCordialement. Votre conseiller personnel"
%(("Mr" if sexe == 1 else "Mme"), nom, commande))
