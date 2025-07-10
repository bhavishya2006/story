year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

#1994 doesnot work because in if statement we kept the year lessthan 1994 and in
 #in elfi we kept greater than so to work we have to keep greaterthan or equalto