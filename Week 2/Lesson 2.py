# """1. Create a function that takes a list containing only numbers and return the first element.
# Examples
# [1, 2, 3] ➞ 1
# [80, 5, 100] ➞ 80
# [-500, 0, 50] ➞ -500 """

# my_list=[1,2,3,4]
# print(my_list[0])

# """2.  Create a function that takes a list of numbers. Return the largest number in the list.
# Examples
# [4, 5, 1, 3] ➞ 5
# [300, 200, 600, 150] ➞ 600
# [1000, 1001, 857, 1] ➞ 1001 """

# my_list=[1,24,6,7,89,9]
# print(max(my_list))

# """3. Create a function that takes a list of numbers and returns the smallest number in the list.
# Examples
# [34, 15, 88, 2] ➞ 2
# [34, -345, -1, 100] ➞ -345
# [-76, 1.345, 1, 0] ➞ -76
# [0.4356, 0.8795, 0.5435, -0.9999] ➞ -0.9999
# [7, 7, 7] ➞ 7 """

# my_list=[7,7,7]
# print(min(my_list))

# """4. Create a function that takes a list and returns the difference between the biggest and smallest numbers.
# Examples
# [10, 4, 1, 4, -10, -50, 32, 21] ➞ 82
# # Smallest number is -50, biggest is 32.
# [44, 32, 86, 19] ➞ 67
# # Smallest number is 19, biggest is 86. """

# my_list=[10, 4, 1, 4, -10, -50, 32, 21]
# print(f"The diference is {max(my_list)-min(my_list)} ")

# """ 5. Create a function to concatenate two integer lists.
# Examples
# [1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]
# [7, 8], [10, 9, 1, 1, 2] ➞ [7, 8, 10, 9, 1, 1, 2]
# [4, 5, 1], [3, 3, 3, 3, 3] ➞ [4, 5, 1, 3, 3, 3, 3, 3]"""

# first_list,second_list=[1,23,5],[3,45,67,8]
# joined_list=first_list+second_list
# print(f"The concotenated list is {joined_list}")

# """6. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.
# Examples
# [5, 57] ➞ True
# [77, 30] ➞ False
# [0] ➞ True """

# my_list=[0]
# print(sum(my_list)<100)

# """7. Given a list of integers, determine whether the sum of its elements is even or odd.
# The return value should be a string "odd" or "even".
# If the input list is empty, consider it as a list with a zero [0].
# Examples
# [0] ➞ "even"
# [1] ➞ "odd"
# [] ➞ "even"
# [0, 1, 5] ➞ "even" """

# my_list=[0]
# summm_list=sum(my_list)%2==0
# print((not summm_list)* "odd"+(summm_list)*"even")

# """8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# Examples
# "11/12/2019" ➞ "20191211"
# "12/31/2019" ➞ "20193112"
# "01/15/2019" ➞ "20191501"
# EXTRA Knowledge """

#my_string="22/12/2019"

# #First method

# my_date=my_string.replace("/","")
# print((my_date[len(my_date)-4:])+(my_date[len(my_date)-6:len(my_date)-4])+my_date[:2])

# #second method

# my_date=my_string.split("/")
# my_date="".join(my_date[::-1])
# print(my_date)

# """9. Create a function that takes two numbers as arguments num, length and returns a list of multiples of num until the list length reaches length.
# Examples
# 7, 5 ➞ [7, 14, 21, 28, 35]
# 12, 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# 17, 6 ➞ [17, 34, 51, 68, 85, 102] """
# list_lengh=int(input("Please enter the lengh of list: "))
# list_start=int(input("Please enter the first element of the list: "))
# my_list=list(range(list_start,list_start*(list_lengh+1),list_start))
# print(my_list)


# """10. Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.
# Examples
# [4, 3, 2, 1], "Asc"  ➞ [1, 2, 3, 4]
# [7, 8, 11, 66], "Des" ➞ [66, 11, 8, 7]
# [1, 2, 3, 4], "None" ➞ [1, 2, 3, 4] """

# my_list=[1,2,67,34]
# rules=input("Please enter the type: ")
# second_list=sorted(my_list)
# print(second_list*(rules=="Asc")+((second_list[::-1])*(rules=="Des"))+(my_list*(rules=="None")))

