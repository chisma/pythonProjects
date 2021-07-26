from words import words
import random
import string


class Hangman:

    def __init__(self, letters_in_the_word, used_letters, available_letters, lives):
        self.letters_in_the_word = letters_in_the_word
        self.used_letters = used_letters
        self.available_letters = available_letters
        self.lives = lives

    def get_valid_word(self):
        word = random.choice(words)
        while '-' in word or ' ' in word or len(word) < 4:
            word = random.choice(words)
        return word.upper()

    def keep_guessing_the_letters(self, valid_word):
        used_letters_not_in_the_word = self.used_letters.difference(
            set(valid_word))
        print("You have used the following letters:",
              ' '.join(used_letters_not_in_the_word))

    def print_current_word(self, valid_word):
        # Current word being guessed as a list
        current_word = [
            letter if letter in self.used_letters else '-' for letter in valid_word]
        print("Current word is: ", ' '.join(current_word))

    def update_used_letters(self, letter_to_be_added):
        self.used_letters.add(letter_to_be_added)

    def update_letters_in_the_word(self, letter_to_be_removed):
        self.letters_in_the_word.remove(letter_to_be_removed)

    def update_available_letters(self):
        self.available_letters = self.available_letters.difference(
            self.used_letters)

    def play(self, valid_word):
        self.letters_in_the_word = set(valid_word)
        while len(self.letters_in_the_word) > 0 and self.lives > 0:
            self.update_available_letters()
            self.keep_guessing_the_letters(set(valid_word))
            self.print_current_word(valid_word)
        # user input
            user_letter = input("Guess a letter: ").upper()
            if user_letter in self.available_letters:
                self.update_used_letters(user_letter)
            # used_letters.add(user_letter)
                if user_letter in self.letters_in_the_word:
                    self.update_letters_in_the_word(
                        user_letter)
                    self.update_available_letters()
                # set(valid_word).remove(user_letter)
                else:
                    self.lives -= 1
                    if self.lives > 0:
                        print(f"You have {self.lives} lives left!")
            elif user_letter in self.used_letters:
                print("You have already guessed this letter!")
            else:
                print(
                    "That's not a valid character or the letter is not available, try again!")

        if self.lives > 0 and len(self.letters_in_the_word) == 0:
            print(
                f"*******CONGRATULATIONS, YOU GUESSED IT RIGHT! THE WORD WAS {valid_word}")

        elif self.lives == 0:
            print(
                f"SORRY!!!You used all your lives, better luck next time!!!The word was {valid_word}")


hangman = Hangman(set(), set(), set(string.ascii_uppercase), 8)
hangman.play(hangman.get_valid_word())
