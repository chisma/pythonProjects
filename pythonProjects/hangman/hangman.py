from words import words
import random
import string


def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word or len(word) < 4:
        word = random.choice(words)
    return word.upper()


def hangman():
    lives = 8
    word = get_valid_word()
    letters_in_the_word = set(word)  # Gives letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(letters_in_the_word) > 0 and lives > 0:
        available_letters = alphabet.difference(used_letters)
        print("You have used the following letters:", ' '.join(used_letters))
        # Current word being guessed as a list
        current_word = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", ' '.join(current_word))
        # user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in available_letters:
            used_letters.add(user_letter)
            if user_letter in letters_in_the_word:
                letters_in_the_word.remove(user_letter)
            else:
                lives -= 1
                if lives > 0:
                    print(f"You have {lives} lives left!")
        elif user_letter in used_letters:
            print("You have already guessed this letter!")

        else:
            print(
                "That's not a valid character or the letter is not available, try again!")

    if lives > 0 and len(letters_in_the_word) == 0:
        print(
            f"*******CONGRATULATIONS, YOU GUESSED IT RIGHT! THE WORD WAS {word}")

    elif lives == 0:
        print(
            f"SORRY!!!You used all your lives, better luck next time!!!The word was {word}")


hangman()
