# """1. Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.
# Can you help her?
# Examples
# "Matt" ➞ "Hello, Matt!"
# "Helen" ➞ "Hello, Helen!"
# "Mubashir" ➞ "Hello, my Love!"""


# usersName=input("Who are you? ")
# res="Mubashir"==usersName
# print(res*"Hello,my love!"+(not res)*("Hello, " + usersName+"!"))


# """2. Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
# Examples
# a,b = 9, 10 ➞ True
# a,b = 9, 9 ➞ False
# a,b = 1, 9 ➞ True
# """

# a,b=int((input("Please enter the digit: "))),int(input("Please enter the other one: "))
# print(a==10 or b==10 or a+b==10)

# """3. Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
# Examples
# 5 ➞ True
# -55 ➞ True
# 37 ➞ False"""

# fiveDiv=int(input("Please, enter your number: "))
# print(fiveDiv%5==0)


# """4. Extra Knowledge
# Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# Examples
# "AB", "CD" ➞ True
# "ABC", "DE" ➞ False
# "hello", "edabit" ➞ False"""


# a,b=(input("Please, enter the first string: ")), input("Please, enter the second string: ")
# print(len(a)==len(b))


# """5. Given a string, return True if its length is even or False if the length is odd.
# """
# example=input("Please, enter the string: ")
# print(len(example)%2==0)


"""6. Create a function that takes a string txt and a number n and returns the repeated string n number of times.
If given argument txt is not a string, return Not A String !!
Examples
"Mubashir", 2 ➞ "MubashirMubashir"
"Matt", 3 ➞ "MattMattMatt"
1990, 7 ➞ "Not A String !!" """

strName, strCount = input("Please, enter the string: "), int(    input("Please, enter the number: "))
print(strName*strCount + (int(strName) == True)*  "Not a string")
