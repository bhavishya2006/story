def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# It's looping through numbers from 1 to 19
# 2. When is the function meant to print "You got it"?
# It is supposed to print "You got it" when i equals 20, but since range(1, 20) never includes 20, this condition is never true.
# 3. What are your assumptions about the value of i?
#i will take values from 1 up to 19.
