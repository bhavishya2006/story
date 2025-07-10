numbers = [1, 2, 3]
new_numbers = [item + 1 for item in numbers]
print(new_numbers)

name = "bhavishya"
new_list = [letter for letter in name]
print(new_list)


names = ["Alice", "Bob", "Jonathan", "Eva", "Bhavishya", "Mark"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)
