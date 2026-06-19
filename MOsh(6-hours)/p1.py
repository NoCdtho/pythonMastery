import math

"""Inputs: They are taken in the console using the function called input"""

# name = input("what is ur name sir: ")
# color = input("what is ur fav color: ")
# print(f"{name} likes {color} ")


# Type Conversion

# number = input("any numer")
# print(200 - int(number))

# String

name1 = "Jennifer"
print(name1[2:-1])

# formatted string
print(f" {name1} [ aosdbfi ]")

# methods
Course = 'python ehh finsihh him'
print(len(Course))
print(Course.upper())  # converts all the letter into upper letter.
print(Course.lower())  # converts all the letters into lower letter.
print(Course.title())  # coverts the first letter in each word to uppercase and the rest in lowercase
print(Course.find('p'))  # returns the index of the letter in the string.
print(Course.replace('p', 'kl'))  # used to return the string with the new string
print('python' in Course)

# if statement
price = 1000000
good_credit = True
if good_credit:
    credit = price * 0.1
    print(f"the amount = {credit}")
else:
    credit = price * 0.2
    print(f"the amount = {credit}")

# Logical operator
has_high_salary = True
has_good_credit = True

if has_high_salary and has_good_credit:
    print("Loan is approved")

# changed the good credit
has_good_credit = False

if has_high_salary or has_good_credit:
    print("still approved")

if has_high_salary and not has_good_credit:
    print("approved enjoy loan nigga")

# Comparison operator
name = "rhit"
if len(name) < 3:
    print(f"{name} must be greater than 3 characters")
elif len(name) > 50:
    print(f" {name} must be of 50 characters")
else:
    print("names look great")

# Guess game
secret_game = 3
i = 0
while i < 3:
    random = input("guess the number: ")
    i = i + 1
    if secret_game == int(random):
        print("u won niogga")
        break
    elif i < 3:
        print(f"try again chances left {3-i}")
    else:
        print("you loser bigga  die bnc")

