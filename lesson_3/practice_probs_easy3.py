# Q1 -------------------------------------------------------------------------

numbers = [1, 2, 3, 4]

# for index in range(len(numbers)):
#     numbers.pop() # set numbers to an empty list, but it doesn't clear the original list.

# # or

# numbers.clear()

# or

# while numbers:
#     numbers.pop() # sets numbers to an empty list, but it doesn't clear the original list.

# print(numbers)

# Q2 -------------------------------------------------------------------------

# print([1, 2, 3] + [4, 5]) # lists can be concatenated with a + operator in python

# Q3 -------------------------------------------------------------------------

# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

# Q4 -------------------------------------------------------------------------

# # *** Shallow copy vs deep copy
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

# Q5 -------------------------------------------------------------------------

# def is_color_valid(color):
#     return color == "green" or color == "blue"

# or

# def is_color_valid(color):
#     return "green" in color or "blue" in color

# or

def is_color_valid(color):
    return color in ["blue", "green"]

print(is_color_valid("green"))