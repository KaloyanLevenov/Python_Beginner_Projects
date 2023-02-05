from english_words import english_words_lower_alpha_set
# This is my suitable set with different words in lower case letters where I can randomly pick a word
import random
import string

word_list = [word.upper() for word in english_words_lower_alpha_set]


# To pick a word and to be better looking transfer set to list and the words in upper case

def hangman():
    word = random.choice(word_list)
    word_letters = set(word)
    # Here in this set we contain all different letters in the word. We don't want repetitive letters here
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Here are the letters guessed by the user
    lives = 9 # User has 8 times to take a wrong guess

    while len(word_letters) > 0 and lives > 0:
        # Every time we guess a letter, we remove it from word_letters set
        used_letters_list = [letter if letter in used_letters else ' * ' for letter in word]
        print('Current word: ', ''.join(used_letters_list))
        # getting the user input
        user_input_letter = input("Take a guess: ").upper()
        if len(user_input_letter) > 1 or (not user_input_letter.isalpha()):
            print("Enter one and only one LETTER! TRY AGAIN !")
            continue
        if user_input_letter in alphabet - used_letters:
            used_letters.add(user_input_letter)
            if user_input_letter in word_letters:
                word_letters.remove(user_input_letter)
            else:
                lives -= 1
                print(f"Your letter {user_input_letter.upper()} is not in the word. Try again. Be careful!")
                print(f"You have {lives} left!")
        elif user_input_letter in used_letters:
            print("You have already used this letter. TRY AGAIN!")
            print("List with used letters: ", ', '.join(used_letters))
        else:
            lives -= 1
            print(f"Your letter {user_input_letter.upper()} is not in the word!")
            print(f"You have {lives} lives left!")
    if lives == 0:
        print(f"Sorry, you have died! The word was {word}")
    else:
        print(f"Congratulations! You guessed the word {word}")


hangman()
