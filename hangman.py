import random


def gametime(word, strikes, none_guesses, blank, guesses):
    """Function that makes the game work"""
    while strikes <= 6:
        if strikes == 0:
            print(" _______\n |/    |\n |\n |\n |\n |\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 1:
            print(" _______\n |/    |\n |    (_)\n |\n |\n |\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 2:
            print(" _______\n |/    |\n |    (_)\n |     |\n |     |\n |\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 3:
            print(" _______\n |/    |\n |    (_)\n |    \\|\n |     |\n |\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 4:
            print(" _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 5:
            print(
                " _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |    /\n |\n_|___")

            while True:
                print(blank)
                userin = input("What would you like to guess? ")
                guesses += 1
                if userin in word and userin != blank and userin != none_guesses and len(userin) < 2:
                    index_of_letter = (word.index(userin))
                    blank[index_of_letter] = userin
                    print(f"{userin} is in the word.")
                    return [strikes, none_guesses, blank, guesses]

                else:
                    none_guesses.append(userin)
                    print("Not in word.")
                    strikes += 1
                    return [strikes, none_guesses, blank, guesses]

        elif strikes == 6:
            print(
                " _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |    / \\ \n |\n_|___")

            return [strikes, none_guesses, blank, guesses]


def replay():
    """Allows the user to restart the game"""
    while True:
        userin = input(
            "Would you like to play again? [Yes/No]: ").lower().strip()
        if userin == "yes" or userin == "y":
            main()
        elif userin == "no" or userin == "n":
            exit()
        else:
            print("Not a valid response. Try again!")


def main():
    """Main area where all functions are applied"""
    guesses = 0
    strikes = 0
    none_guesses = []
    list_of_words = ("sprite", "head", "runtime", "authority",
                     "Python", "Kraft", "duck", "junk", "klins", "edge", "teams", "rainbow", "chrome", "steam", "file")

    word = random.choice(list_of_words)
    blank_word = (list("_" * (len(word))))
    userin = input(
        "Would you like to play a game of hangman? [Yes/No]: ").lower().strip()

    while True:
        if userin == "yes" or userin == "y":
            strikes, none_guesses, blank_word, guesses = gametime(
                word, strikes, none_guesses, blank_word, guesses)
            print(f"Letters not in the word: {none_guesses}")

            if "".join(blank_word) == word and strikes < 6:
                print(f"""You Won! The word was {
                      word}, it took you {guesses} guesse(s).""")
                replay()
            elif strikes == 6:
                print(f"You lost! The word was {word}.")
                replay()


if __name__ == '__main__':
    main()
