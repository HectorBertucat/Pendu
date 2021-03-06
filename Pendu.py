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
    global already_guessed # liste des lettres déjà devinées
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

def play_again():
    global play_game
    play_message = "Voulez-vous jouer à nouveau ? y = Oui, n = Non \n"
    play_game = input(play_message)
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input(play_message)
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Merci d'avoir jouer, à bientôt !!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Le mot du pendu est : " + display + " Entrez votre choix: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9": # si l'input est différent d'une lettre
        print("Mauvaise saisie, veuillez saisir une lettre\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Essayez une autre lettre.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvais choix... " + str(limit - count) + " essais restants.\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvais choix... " + str(limit - count) + " essais restants.\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvais choix... " + str(limit - count) + " essais restants.\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvais choix... dernier essai.\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Mauvais choix. Vous êtes pendu!!!\n")
            print("Le mot était: ", already_guessed, word)
            play_again()

    if word == '_' * length:
        print("Félicitations ! Vous avez trouvé le mot !")
        play_again()

    elif count != limit:
        hangman()

    main()

    hangman()

main()
hangman()
