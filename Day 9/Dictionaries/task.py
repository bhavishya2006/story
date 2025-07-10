programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary["Bug"])
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}
print(colours["pear"])
my_empty_dictionary = {}

colours["peach"] = "pink"


colours["apple"] = "green"


for key in colours:
    print(key)


for key in colours:
    print(colours[key])
