import random

def show_intro():
    """Display the introduction of the game."""
    print("------------------------------------------------")
    print("               HANGMAN GAME")
    print("------------------------------------------------")
    print("Guess the hidden word letter by letter.")
    print("You get only 6 wrong attempts.")
    print("------------------------------------------------\n")

def get_word():
    """Return a random word from the given list."""
    words = ["tiger", "apple", "chair", "plane", "smile"]
    return random.choice(words)

def show_status(display, wrong, guessed):
    """Show current progress of the game."""
    print("\nWords:", " ".join(display))
    print("Wrong guesses:", wrong, "/6")
    print("Guessed letters:", ", ".join(guessed))

def update_display(word, display, letter):
    """Update the blanks if the letter is correct."""
    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter

def valid_input():
    """Ensure the user enters only one letter."""
    while True:
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid! Please enter ONLY one alphabet letter.")
        else:
            return letter

def Play():
    """Main game logic."""
    secret = get_word()
    display = ["_"] * len(secret)
    guessed_letters = []
    wrong = 0

    while wrong < 6 and "_" in display:
        show_status(display, wrong, guessed_letters)
        letter = valid_input()

        if letter in guessed_letters:
            print("Already guessed! Try another letter.")
            continue

        guessed_letters.append(letter)

        if letter in secret:
            print("Correct!")
            update_display(secret, display, letter)
        else:
            print("Wrong!")
            wrong += 1

    print("\n------------------------------------------------")
    if "_" not in display:
        print("You WON! The word was:", secret)
    else:
        print("You LOST! The word was:", secret)
    print("------------------------------------------------")

show_intro()
Play()
