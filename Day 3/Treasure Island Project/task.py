print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
option = input("You are at crossroad where do you want to go type left or right:")
# choice = input("Type 'wait' to wait for a boat.Type 'swim' to swim across:")
# colour = input("choose a colour red , yellow, and blue:")
if option == "left":
    print("you have come to lake. There is an island in the middle of the lake.")
    option2 = input("Type 'wait' to wait for a boat.Type 'swim' to swim across:")
    if option2 == "wait":
        print("you arrive at the island unharmed there is a house with three doors.one red,one yellow and one blue.which one do you choose?")

        option3 = input("choose a colour red , yellow, and blue:")
        if option3 == "red":
            print("it's a room full of fire.Game over.")
        elif option3 == "yellow":
            print("you found the treasure! you win!")
        else:
            print("you enter a room of beasts.Game over")
    elif option2 == "swim":
        print("You get attacked by an angry trout.Game over.")

elif option == "right":
    print("You fell into a hole game over")


