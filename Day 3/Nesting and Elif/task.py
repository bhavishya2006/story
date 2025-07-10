print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("enter your age:"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <=12 :
        print("your ticket is $5")
    elif 12 < age <= 18:
        print("your ticket is $7")
    else:
        print("your ticket is $12")

else:
    print("Sorry you have to grow taller before you can ride.")
