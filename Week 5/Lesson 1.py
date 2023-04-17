"""1. Create a function which returns the number of true values there are in an array.
Examples
countTrue([true, false, false, true, false]) ➞ 2
countTrue([false, false, false, false]) ➞ 0
countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false)."""

def countTrue(myList:list):
     return myList.count(True)
print(countTrue([]))



"""2. Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
Examples
intWithinBounds(3, 1, 9) ➞ true
intWithinBounds(6, 1, 6) ➞ false
intWithinBounds(4.5, 3, 8) ➞ false
Notes
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
Bounds will be always given as integers."""

def inWithinBounds(bounds:tuple):
    
    if isinstance(bounds[0],int) and isinstance(bounds[-1],int):
        if bounds[0]<bounds[-1]:
            return True
        else:
            return False
    else:
        return False

print(inWithinBounds((6,1,6)))    


""" 3. Create a function that takes three values:
h hours
m minutes
s seconds
Return the value that's the longest duration.
Examples
longestTime(1, 59, 3598) ➞ 1
longestTime(2, 300, 15000) ➞ 300
longestTime(15, 955, 59400) ➞ 59400"""
def longestTime(hours,minute,seconds):
    h=hours*60*60
    m=minute*60
    if m<seconds and h<seconds:
        return seconds
    elif m<h and seconds<h:
        return hours
    elif seconds<m and h<m:
        return minute
    else:
        return "Something is wrong"

    
    
print(longestTime(1,60,3598))


"""4. Create a function that takes the month and year (as integers) and returns the number of days in that month.
Examples
days(2, 2016) ➞ 28
days(4, 654) ➞ 30
days(2, 200) ➞ 28
days(2, 1000) ➞ 28
Notes
Don't forget about leap years!"""
def days(day:int,year:int):
    day_list1=[1,3,5,7,8,10,12]
    
    
    if day==2:
        if (2024-year)%4:
            return 28
        else:
            return 29 
    elif day in day_list1:
        return 31
    elif day not in day_list1:
        return 30
    else:
        "Not a valid day"  


print(days(4,654))        
    





"""5. Create a function that takes a string and censors words over four characters with *.
Examples
censor("The code is fourty") ➞ "The code is ******"
censor("Two plus three is five") ➞ "Two plus ***** is five"
censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word."""


def censor(text:str):
    text=text.split()
    my_list=[]
    for i in text:
        if len(i)<=4:
            my_list.append(i)
        elif len(i)>4:
            i=i.replace(i,len(i)*"*")
            my_list.append(i)
    return " ".join(my_list)


print(censor("aaaa aaaaa 1234 12345"))


"""6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". It should return the same string without any change if it doesn't have any "a".
Examples
absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
absolute("A man with no haters.") ➞ "An absolute man with no haters."
Notes
Watch for uppercase letters as shown in example #3."""
def absolute(text:str):
    mytext=text.split()
    for i in mytext:
        if i.lower()=="a":
            mytext[mytext.index(i)]=i+"n absolute"
            return " ".join(mytext)
        else:
            return text
def absolute(text:str):
    return text.replace("A ","An absolute ").replace("a ","an absolute ")
print(absolute("I am a champion"))        


# """7. Return an Array of Subarrays
# Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.
# x Number of subarrays contained within the main array.
# y Number of items contained within each subarray.
# z Item contained within each subarray.
# Examples
# matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
# matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
# matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
# Notes
# The first two arguments will always be integers.
# The third argument is either a string or an integer."""



"""8. Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiplyNums("2, 3") ➞ 6
multiplyNums("1, 2, 3, 4") ➞ 24
multiplyNums("54, 75, 453, 0") ➞ 0
multiplyNums("10, -2") ➞ -20
Notes
Bonus: Try to complete this challenge in one line!"""


def multiplyNums(numText:str):
    numList=numText.split(", ")
    x=list(map(int,numList))
    z=1
    for i in x:
        z*=i
    return z    


def multiplyNums(numText:str):            ## Is it the right one????? 
    z=numText.replace(", ","*")
    return eval(z)

print(multiplyNums("10, -2"))



"""9. Create a function that takes a string road and returns the car that's in first place. The road will be made of "=", and cars will be represented by letters in the alphabet.
Examples
firstPlace("====b===O===e===U=A==") ➞ "A"
firstPlace("e==B=Fe") ➞ "e"
firstPlace("proeNeoOJGnfl") ➞ "l"
Notes
Return "No car available" if there is no car on the road and "No road available" if there is no road."""


def firstPlace(text:str):
    z=text.replace("=","")
    if text.isalpha():
        return "No road available"
    elif len("="*len(text))==len(text):
        return "No car available"
    else:
        return z[-1]
    
print(firstPlace("======="))




"""10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The array of numbers will be unsorted (not in order).
Only one number will be missing."""

def missingNum(num_list:list):
    
    z=list(set(range(1,11)).difference(num_list))
    return z[0]
 
print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]))