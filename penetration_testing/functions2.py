# This is a simple game that asks the user to guess the words an admin types

# Put all functions within here
##-------------------------------####

#Admin types in the word of his choice
password = int(input("Type in your password if you're an admin \n"))

if password == int(1234):
    salute = str(input("ADMIN Shina Salau: Input a word \n"))
elif password == int(4321):
    salute = str(input("ADMIN Mary Salau: Input a word \n"))
else:
    print("You're not an admin!")
