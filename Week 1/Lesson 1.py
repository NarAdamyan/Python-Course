"""1. For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13"""
x=45 
summ=x%10+x//10
print(summ)


"""2. A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False"""

x=44
print(x%10==x//10)


"""3. Write a function that takes an integer minutes and converts it to seconds.
5 ➞ 300
2 ➞ 120"""
var=5
min=60
seconds=var*min
print(seconds)


"""4. Create a function that takes the age in years and returns the age in days.
65 ➞ 23725
0 ➞ 0
20 ➞ 7300"""

age=65
days=365
ageByDays=age*days
print(ageByDays)


"""5. Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200"""
var=1.3
bySeconds=var//1*60*60+(var%1*10*60)
print(bySeconds)


"""6. Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet."""
x=0
inchByfeet=1/12
feet=x*inchByfeet
print(feet)

"""7. Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers."""

var=10
res=((var**2)**(1/2))%2==False
print(res*"Even"+(not res) *'Odd')

