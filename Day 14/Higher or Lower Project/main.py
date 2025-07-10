from game_data import data
import random
from art import logo
from art import vs

def information (account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
while game_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {information(account_a)}.")
    print(vs)
    print(f"Against B: {information(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = answer(guess, a_follower_count, b_follower_count)
    if is_correct :
        score += 1
        print(f"You are Right.Your score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_continue = False