"""1. Create a function that takes a string and returns it as an integer.
Examples
"6" ➞ 6
"1000" ➞ 1000
Notes
All numbers will be whole.
All numbers will be positive.
"""

my_var=input("Please, enter a whole number: ")
print(int(my_var))


"""2. Create a function that takes a boolean variable flag and returns it as a string.
Examples
True ➞ "True"
False ➞ "False" """
x=False
z=x*"True"+(not x)*"False"
print(z,type(z))

"""
3. Write a function that returns the string "something" joined with a space " " and the given argument a.
Examples
"is better than nothing" ➞ "something is better than nothing"
"Bob Jane" ➞ "something Bob Jane"
"something" ➞ "something something"
"""


my_arg=input("Please enter an argument: ")
print(f"something {my_arg}")

"""4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
"Darth Vader" ➞ "Luke, I am your father."
"Leia" ➞ "Luke, I am your sister."
"Han" ➞ "Luke, I am your brother in law." """
var="Luke,I am your "
z=input("Enter your name: ")
print(var+((z=="Darth Vader")*"father")+((z=="Leia")*"sister")+((z=="Han")*"brother in low"))


"""5. Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
"Celebration" ➞ 5
"Palm" ➞ 1
"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
"""

my_string=input("Please, enter your string: ")
the_vowels=my_string.count("a")+ my_string.count("e") +my_string.count("i")+my_string.count("o") +my_string.count("u")
print(f"The string contain {the_vowels} vowels")



"""7. Create a function that replaces all the vowels in a string with a specified character.
Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"
"minnie mouse", "?" ➞ "m?nn?? m??s?"
"shakespeare", "*" ➞ "sh*k*sp**r*"
"""
str1="the aardvark"
str2="minnie mouse"
str3="shakespeare"
str1=str1.replace ("a" ,"#").replace("e","#").replace("i","#").replace("o","#").replace("u","#") 
str2=str2.replace ("a" ,"?").replace("e","?").replace("i","?").replace("o","?").replace("u","?")
str3=str3.replace ("a" ,"*").replace("e","*").replace("i","*").replace("o","*").replace("u","*")

print(str1,str2,str3)


"""8. Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
Examples
"1234123456785678" ➞ "************5678"
"8754456321113213" ➞ "************3213"
"35123413355523" ➞ "**********5523" """
card_number="123456789009876543"
print(card_number.replace(card_number[0:-4],(len(card_number)-4)*"*"))

"""9. Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
Examples
"Donald Trump" ➞ "Trump Donald"
"Rosie O'Donnell" ➞ "O'Donnell Rosie"
"Seymour Butts" ➞ "Butts Seymour"
"""
name_surname=input("Please, enter your name,surname: ")
name_surname=name_surname.split()
print(f"{name_surname[-1]} {name_surname[0]}")



"""A valid pin pass
Exactly 4-6 character
Only numerical characters(0-9)
No whitespace
"""
pin_code=input("Enter the code: ")
a=(len(pin_code)==4 or len(pin_code)==6) and pin_code.isdigit() and " " not in pin_code
print(a)
