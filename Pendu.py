import random
import time

print("Bienvenue sur le jeu le Pendu par Hector Bertucat\n")
name=input("Quel est votre nom : ")
print("Bonjour " + name + ", bonne chance !")
time.sleep(3)
print("Le jeu va commencer...\n C'est parti pour le Pendu !")
time.sleep(3)

def main():
    global count # incrément
    global display # sert à afficher le bon nombre de "_" en fonction du mot
    global word # mot à deviner
    global already_guessed # liste des mots déjà devinés
    global length # longueur du mot à deviner
    global play_game # input pour jouer ou arreter de jouer
    words_to_guess = ["bonjour", "canape", "vinyl", "zebre", "tomahawk", "clavecin", "printemps", "tambourin",
                      "coquelicot", "baccalaureat"] # liste des mots à deviner
    word = random.choice(words_to_guess) # choix du mot au hasard depuis la liste
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

