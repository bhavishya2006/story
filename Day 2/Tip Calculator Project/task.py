print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_multiplier = 1 + (tip / 100)
total_per_person = (bill / people) * tip_multiplier
final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: ${final_amount}")
