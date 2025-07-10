import random
from hangman_words import word_list  # TODO-1: Import word list from hangman_words.py
from hangman_art import stages, logo  # TODO-2: Import stages from hangman_art.py and logo

# TODO-3: Print the logo at the start of the game
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []  

while not game_over:
    # TODO-6: Tell the user how many lives they have left
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: Check if the user has already guessed this letter
    if guess in guessed_letters:
        print(f"You've already guessed {guess}. Please try a different letter.")
        continue  

    guessed_letters.append(guess)  
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: If the letter is not in the chosen_word, tell the user it's not in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            # TODO-7: Show the correct word if the user loses
            print(f"***********************YOU LOSE**********************")
            print(f"It was {chosen_word}!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: Display the stages of hangman as lives decrease
    print(stages[lives])
