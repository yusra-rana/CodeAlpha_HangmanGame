# =============================
# CodeAlpha Internship Task 1
# Hangman Game in Python
# Developed by: Yusra Rana
# =============================

import random

# List of predefined words
words = ["python", "laptop", "computer", "programming", "keyboard"]

# Randomly select a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

# Game loop
while incorrect_guesses > 0:

    # Display the word with underscores
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_ " not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    print("Remaining incorrect guesses:", incorrect_guesses)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        incorrect_guesses -= 1

# If user loses
if incorrect_guesses == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")