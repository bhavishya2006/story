from random import randint
from art import logo

easy_level = 10
hard_level = 5

def correct_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = difficulty()

    guess = 0
    while guess!= answer :
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess:"))
        turns = correct_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()

