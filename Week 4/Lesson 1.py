"""1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
relation_to_luke("Leia") ➞ "Luke, I am your sister."
relation_to_luke("Han") ➞ "Luke, I am your brother in law." """

my_text=input("Please enter your name: ")
if my_text=="Darth Vader":
    print("Luke,I am your father")
elif my_text=="Leia":
    print("Luke,I am your sister")
elif my_text=="Han":
    print("Luke,I am yor brother in low")        
else:
    print("Please,enter the valid name")    


"""2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
Examples
damage(40, 5, "second") ➞ 200
damage(100, 1, "minute") ➞ 6000
damage(2, 100, "hour") ➞ 720000
Notes
Return "invalid" if damage or speed is negative. """

damage=(2,100,"hour")
minute=damage[-1]*60
hour=damage[-1]*60*60
if damage[0]<0 or damage[1]<=0 or type(damage[0])==type(damage[1])!= int:
    print("invalid")
elif damage[-1]=="second" :
    print(damage[0]*damage[1])     
elif damage[-1]=="minute":
    print(damage[0]*damage[1]*60)
elif damage[-1]=="hour":
    print(damage[0]*damage[1]*60*60)
else:
    print("not valid")        

"""3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ [] """

filter_list=(["Nothing", "here"])
my_list=[]
for i in filter_list:
    if type(i) is int:
        my_list.append(i)
print(my_list)    

"""4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True """


my_text=input("Please enter the number: ") 
if my_text==my_text[::-1]:
    print(True)
else:
    print(False)      

"""5. Create a function that changes all the elements in a list as follows:
Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and make the first letter of the word a capital letter.
Changes all boolean values to its opposite.
Examples
change_types(["a", 12, True]) ➞ ["A!", 13, False]
change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
Notes
There won't be any float values.
You won't get strings with both numbers and letters in them.
Although the task may be easy, try keeping your code as clean and as readable as possible! """

change_type=[False, "False", "true"]
my_list=[]
for i in change_type:
    if type(i) is int and i%2==0:
        i=(i+1)
        my_list.append(i)
    elif type(i) is int and i%2!=0:
        my_list.append(i)
    elif type(i) is str:
        i=i.capitalize()
        my_list.append(i+"!") 
    elif type(i) is bool:
        my_list.append(not i)
print(my_list)    


"""6. Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.
See the below examples for a better understanding:
Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
string_pairs("edabit") ➞ ["ed", "ab", "it"]
string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty. """

my_list=[]
my_text=""

if len(my_text)%2==0:
    for i in range(0,len(my_text)-1,2):
        my_list.append(my_text[i]+my_text[i+1])
elif len(my_text)%2!=0:
    my_text+="*"
    for i in range(0,len(my_text)-1,2):
        my_list.append(my_text[i]+my_text[i+1])
print(my_list)        


"""
7. Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
Examples
stupid_addition(1, 2) ➞ "12"
stupid_addition("1", "2") ➞ 3
stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers. """
my_list=(1,9)


if len(my_list)==2 and  type(my_list[0])==type(my_list[-1])==str:
    print(my_list[0]+my_list[-1])
elif len(my_list)==2 and type(my_list[0])==type(my_list[-1])==int: 
    print(my_list[0]+my_list[-1])   
elif len(my_list)==2 and type(my_list[0])!=type(my_list[-1]):
    print("None")
else:
    print("The entered is not valid: ")        


"""8. Write a function that does the following operations: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge the variables will be defined for you. All you have to do is look at the variables, do some string to integer conversions, use some if conditionals, and combine them based on the operation.
The numbers and operation will be given as strings, and you should return the value as a string as well.
Examples
operation("1", "2", "add" ) ➞ "3"
operation("4", "5", "subtract") ➞ "-1"
operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as strings, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer. """

my_list=("91", "8", "divide")
my_list2=(int(my_list[0]),int(my_list[1]))
if my_list[-1]=="add":
    print(str(sum(my_list2)))
elif my_list[-1]=="subtract":
    print(str(my_list2[0]-my_list2[-1]))  
elif my_list[-1]=="divide":
    if my_list2[-1]==0:
        print("undefined")
    else:
        print(str(my_list2[0]//my_list2[-1]))    
else:
    print("Undefined")    

"""
9. Check if the given string consists of only letters and spaces and if every letter is in lower case.
Examples
letters_only("PYTHON") ➞ False
letters_only("python") ➞ True
letters_only("12321313") ➞ False
letters_only("i have spaces") ➞ True
letters_only("i have numbers(1-10)") ➞ False
letters_only("") ➞ False
Notes
Empty arguments will always return False.
Input values will be mixed (symbols, letters, numbers)."""

letters_only="i have"
print(letters_only.lower()==letters_only and (letters_only.isalpha() or ' ' in letters_only))

"""10. Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.
Examples
check([1, 2, 3]) ➞ "increasing"
check([3, 2, 1]) ➞ "decreasing"
check([1, 2, 1]) ➞ "neither"
check([1, 1, 2]) ➞ "neither"
Notes
The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
Input lists have a minimum length of 2. """

my_list=[5,4,6,3]

my_list2=list(set(my_list))
if my_list==sorted(my_list2):
    print("incrasing")
elif my_list==sorted(my_list2,reverse=True):
    print("decrasing")
elif len(my_list)==len(my_list2):
    print("neither")
else:
    print("neither")        
