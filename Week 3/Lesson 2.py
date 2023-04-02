# """EXTRA Knowledge
# 1. Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.
# Examples
# sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
# // 2 & 3 are common in all 3 lists.
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
# // 2, 2 & 3 are common in all 3 lists.
# sum_common([1], [1], [2]) ➞ 0 """

# lst1=[1]
# lst2=[5]
# lst3=[7]
# sum_list=set(lst1).intersection(set(lst2)).intersection(set(lst3))
# print(sum(sum_list))

"""2. Write a function that takes a list of numbers and returns a list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
[1, 2, 3, 4, 5, 6] ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
[-1, -2, -3, -4, -5, -6] ➞ [-12, -9]
[0, 0] ➞ [0, 0]
Notes
Count 0 as an even number."""




# """3. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 } """

# top_note={ "name": "John", "notes": [3, 5, 4] }
# my_item=top_note.get("notes")
# top_note.update({"top_note":max(my_item)})
# top_note.pop("notes")
# print(top_note)


"""4. Write a function that takes a list of numbers and returns a list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
sum_odd_and_even([0, 0]) ➞ [0, 0]) """



# """
# 5. You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar.
# Examples
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796
# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }) ➞ 32411
# profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }) ➞ 44030  """
# print(2.77*8500-7.95*8500)

# profit=({
#  "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# })
# total_profit=profit.get("cost_price")*profit.get("inventory")-profit.get("sell_price")*profit.get("inventory")
# print(total_profit)

# """6. A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.
# Examples
# is_harshad(75) ➞ False
# # 7 + 5 = 12
# # 75 is not exactly divisible by 12
 
# is_harshad(171) ➞ True
# # 1 + 7 + 1 = 9
# # 9 exactly divides 171
 
# is_harshad(481) ➞ True
# is_harshad(89) ➞ False
# is_harshad(516) ➞ True
# is_harshad(200) ➞ True
# EXTRA Knowledge"""
# my_num="89"
# my_lst=list(my_num)

# listOfnum=list(map(int,my_lst))
# result=int(my_num)%sum(listOfnum)==0
# print(result)

# """7. Given an input string, reverse the string word by word.
# Examples
# "the sky is blue" ➞ "blue is sky the"
# "  hello world!  " ➞ "world! hello"
# "a good   example" ➞ "example good a"
# Notes
# A word is defined as a sequence of non-space characters.
# The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# Try to solve this in linear time.
# Extra Knowledge """
# my_text=input("Please write the string: ")
# my_lst=(my_text.split())
# print(" ".join(my_lst[::-1]))

# """8. Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).
# Examples
# word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"
# word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"
# word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit" """


# my_word=["n", "e", "r", "i", "n", "a"]
# my_index=  [0, 5, 2, 3, 4, 1]

# all=map(str,my_index)
# thisdict=(dict(zip(all,my_word)))
# lst=sorted(thisdict.items())
# sorted_dict=(dict(lst))
# print("".join(sorted_dict.values()))


# """9. Create a function to test if a string is a valid pin or not.
# A valid pin has:
# Exactly 4 or 6 characters.
# Only numerical characters (0-9).
# No whitespace.
# Examples
# valid("1234") ➞ True
# valid("45135") ➞ False
# valid("89abc1") ➞ False
# valid("900876") ➞ True
# valid(" 4983") ➞ False
# Notes
# Empty strings should return False when tested. """

# valid="900876"
# valid_list=list(valid)
# print(len(valid)==len(valid_list) and (len(valid)==4 or len(valid)==6) and valid.isdigit())

# """10. Return a new set of identical items from two sets
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30} """
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))


# """11. Write a Python program to return a new set with unique items from both sets by removing duplicates.
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 40, 10, 50, 20, 60, 30} """


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))


# """12. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
# Given:
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# Expected output:
# set1 {10, 30}
# EXTRA Knowledge """


# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set3=set1.intersection(set2)
# print(set1.difference(set3))

# """13. Given an input string, reverse the string word by word (reversed word also).
# Examples
# "the sky is blue" ➞ "eulb si yks eht"
# Notes
# A word is defined as a sequence of non-space characters.
# The input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# Try to solve this in linear time. """
# my_string=input("Please enter your text: ")
# lst=list(my_string)[::-1]
# print("".join(lst))