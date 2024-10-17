import random


def display_hangman(strikes):
    stages = [
        " _______\n |/    |\n |\n |\n |\n |\n |\n_|___",
        " _______\n |/    |\n |    (_)\n |\n |\n |\n |\n_|___",
        " _______\n |    (_)\n |     |\n |     |\n |\n |\n_|___",
        " _______\n |/    |\n |    (_)\n |    \\|\n |     |\n |\n |\n_|___",
        " _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |\n |\n_|___",
        " _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |    /\n |\n_|___",
        " _______\n |/    |\n |    (_)\n |    \\|/\n |     |\n |    / \\\n |\n_|___"
    ]
    print(stages[strikes])


def gametime(word, strikes, none_guesses, blank, guesses):
    """Function that runs the hangman game"""
    while strikes <= 6:
        display_hangman(strikes)
        print(f"Word: {' '.join(blank)}")
        print(f"Incorrect guesses: {none_guesses}")

        userin = input("Guess a letter: ").lower().strip()
        guesses += 1

        if len(userin) != 1 or not userin.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if userin in blank or userin in none_guesses:
            print(f"You've already guessed '{userin}'!")
            continue

        if userin in word:
            for index, letter in enumerate(word):
                if letter == userin:
                    blank[index] = userin
            print(f"Good job! {userin} is in the word.")
        else:
            none_guesses.append(userin)
            strikes += 1
            print(f"Sorry, {userin} is not in the word.")

        if "".join(blank) == word:
            print(f"Congratulations! You guessed the word: {
                  word} in {guesses} guesses.")
            return

        if strikes == 6:
            display_hangman(strikes)
            print(f"Game over! The word was: {word}")
            return


def replay():
    """Ask the user if they want to play again"""
    while True:
        userin = input(
            "Would you like to play again? [Yes/No]: ").lower().strip()
        if userin in ["yes", "y"]:
            return True
        elif userin in ["no", "n"]:
            return False
        else:
            print("Not a valid response. Try again!")


def main():
    """Main function to start the game"""
    while True:
        list_of_words = ["sprite", "head", "runtime", "authority", "python", "kraft",
                         "duck", "junk", "klins", "teams", "rainbow", "chrome", "steam", "file"]
        word = random.choice(list_of_words)
        blank = ["_"] * len(word)
        none_guesses = []
        guesses = 0
        strikes = 0

        userin = input(
            "Would you like to play a game of hangman? [Yes/No]: ").lower().strip()
        if userin in ["yes", "y"]:
            gametime(word, strikes, none_guesses, blank, guesses)
            if not replay():
                break
        elif userin in ["no", "n"]:
            break
        else:
            print("Not a valid response. Try again!")


if __name__ == '__main__':
    main()
