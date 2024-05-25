from math import *


def encrypt():
    key = input("Veuillez entrer votre cle\n(lettres, sans espace)\n$ ").lower()
    msg = input("Veuillez entrer le message\n$ ").lower()
    calculateEncryption(key, msg)

def calculateEncryption(key, msg):
    str = ""
    count = 0
    unsupported = -1
    for i in range(len(msg)):
        if alphabet.find(msg[i]) == -1 and msg[i] != " ":
            unsupported = i
            break
        elif msg[i] != " ":
            str += alphabet[((alphabet.find(msg[i])) + (alphabet.find(key[count % len(key)]))) % 27]
            count += 1
        else:
            str += " "
    if unsupported != -1:
        print("Charactere \""+msg[unsupported]+"\" n'est pas\nsupporte")
    else:
        print(str)
    input("\nAppuyez sur entree pour\ncontinuer...")
    menu()

def decrypt():
    key = input("Veuillez entrer votre cle\n(lettres, sans espace)\n$ ").lower()
    msg = input("Veuillez entrer le message\n$ ").lower()
    calculateDecryption(key, msg)

def calculateDecryption(key, msg):
    str = ""
    count = 0
    unsupported = -1
    for i in range(len(msg)):
        if alphabet.find(msg[i]) == -1 and msg[i] != " ":
            unsupported = i
            break
        elif msg[i] != " ":
            str += alphabet[((alphabet.find(msg[i])) - (alphabet.find(key[count % len(key)])))]
            count += 1
        else:
            str += " "
    if unsupported != -1:
        print("Charactere \""+msg[unsupported]+"\" n'est pas\nsupporte")
    else:
        print(str)
    input("\nAppuyez sur entree pour\ncontinuer...")
    menu()

def menu():
    ans = input("Souhaitez vous\n 1.  Crypter\n 2.  Decrypter\n 3.  Sortir\n$ ")
    if ans == "1":
        encrypt()
    elif ans == "2":
        decrypt()
    elif ans == "3":
        print("A Bientot")
    else:
        print("Reponse invalide")
        input("\nAppuyez sur entree pour\ncontinuer...")
        menu()

alphabet = "abcdefghijklmnopqrstuvwxyz!"
separator = "================="
print(separator+"\nCodeur et decodeur de\nchiffrement vigenere\n"+separator)
menu()
