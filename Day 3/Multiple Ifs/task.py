print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        ticket = 5
        print("Please pay $5.")
    elif age <= 18:
        ticket = 7
        print("Please pay $7.")
    else:
        ticket = 12
        print("Please pay $12.")
    photo = input("do you want to take a photo or not? type y for yes and n for no.")
    if photo == "y":
        ticket += 3
        print(f"your total bill is {ticket}")

else:
    print("Sorry you have to grow taller before you can ride.")
