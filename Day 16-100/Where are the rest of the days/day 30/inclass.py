# # with open("a_file.txt") as file:
# #     file.read( )
#
#
# try :
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("something")
# except KeyError:
#     print("The key is not present in the dictionary")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("this is an error that i made up")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)