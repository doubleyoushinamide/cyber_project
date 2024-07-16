#This is neater! I love writing in one line
#print("My name is, " + input("First Name? \n") + " " + input("Last Name? \n"))

#print(f"Your new twitter handle and bio is @cyber{input("petName? \n")} from {input("Location? \n")}")


# An if/else statement to check student grades from their score

#Ternary operators
score = int(input("What is your score? \n"))
rem = (
    "F" if score <= 45 else 
    "D" if 45 < score <= 50 else 
    "C" if 50 < score <= 60 else 
    "B" if 60 < score <= 69 else 
    "A")

# Print the grade
print(f"Your grade in school is: {rem}")
print(
    "Failed!" if rem == "F" else 
    "Poor" if rem == "D" else 
    "Average!" if rem == "C" else 
    "Good!" if rem == "B" else 
    "Excellent!")
