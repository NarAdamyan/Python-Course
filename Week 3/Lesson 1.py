"""1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).
Check the examples for a better understanding.
Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8] """


my_list=[1,2,3,4,5]
last_int=[my_list.pop()]
my_list[0:0]=last_int
print(my_list)


"""2. Create a function that inverts the rgb values of a given tuple.
Examples
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.
color_invert((0, 0, 0)) ➞ (255, 255, 255)
color_invert((165, 170, 221)) ➞ (90, 85, 34)
Notes
Must return a tuple.
255 is the max value of a single color channel. """


color_invert=(165,170,221)
rgb_values=255-(color_invert[0]),255-(color_invert[1]),255-(color_invert[-1])
print(rgb_values,type(rgb_values))





"""4. Given a list of numbers, write a function that returns a list that...
Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7] """


my_list=[1,2,3,4,5,5,2,2,6,9,8]
my_list=list(set(my_list))
print(sorted(my_list))


"""5. Given two strings, create a function that returns the total number of unique characters from the combined string.
Examples
count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
"sore", "zebra" ➞ 7
"a", "soup" ➞ 5 """


a,b="apple","play"
print(len(set(a+b)))


"""6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
Examples
{
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
} ➞ ["Becky", "John", "Steve"] """



my_dict={
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}

my_list=sorted(list(my_dict.values()))
print(my_list)

"""7. Create a function that returns a list of strings sorted by length in ascending order.
Examples
sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
sort_by_length([]) ➞ []
Notes
Strings will have unique lengths, so don't worry about comparing two strings with identical length.
Return an empty array if the input array is empty """

my_list=([])
my_list.sort(key=len)
print(my_list)

"""8. Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]
dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)] """

dict_to_list=({
  "D": 1,
  "B": 2,
  "C": 3
})


my_list=list(dict_to_list.items())
first_item=[my_list.pop(0)]
print(my_list+first_item)


"""
9. Print the value of key ‘history’ from the below dict"""
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
} 
print(sampleDict["class"]["student"]["marks"]["history"])

"""
10. Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.
Given: """
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'} 

sample_dict["country"] = sample_dict.pop("city")
print(sample_dict)
