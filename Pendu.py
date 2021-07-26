import random
import time

print("Bienvenue sur le jeu le Pendu par Hector Bertucat\n")
name=input("Quel est votre nom : ")
print("Bonjour " + name + ", bonne chance !")
time.sleep(3)
print("Le jeu va commencer...\n C'est parti pour le Pendu !")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["bonjour", "canape", "vinyl", "zebre", "tomahawk", "clavecin", "printemps", "tambourin",
                      "coquelicot", "baccalaureat"]

