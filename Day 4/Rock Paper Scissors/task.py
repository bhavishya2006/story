import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor:"))
computer_choice = random.randint(0,2)

print(f"computer choose {computer_choice}")
print(game_images[computer_choice])

if user >= 3 or user< 0:
    print("You typed an invalid number. You lose!")
elif user == 0 and computer_choice == 2 :
    print("You win!")
elif user == 2 and computer_choice == 0:
    print("you lose")
elif user > computer_choice :
    print("you win")
elif computer_choice > user :
    print("You lose")
elif user == computer_choice :
    print("It's a draw")
else:
    print("You typed an invalid number! You lose!!")

