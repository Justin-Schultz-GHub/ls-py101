# Q1 -------------------------------------------------------------------------

# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first()) # {'prop1': 'hi there'}
# print(second()) # None

# Q2 -------------------------------------------------------------------------

# # Since num_list is a reference to the original list in dictionary,
# # appending to num_list modifies the list. Thus, the original dictionary is
# # also updated.
# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# # Doesn't change dictionary
# dictionary = {"first": [1]}
# num_list = dictionary["first"].copy()
# num_list.append(2)

# # Also doesn't change dictionary
# dictionary = {"first": [1]}
# num_list = dictionary["first"][:]
# num_list.append(2)

# print(num_list)
# print(dictionary)

# Q3 -------------------------------------------------------------------------

# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# # In this case, the mess_with_vars function modifies the content of the lists
# # directly. Since lists in Python are mutable and passed by reference, the
# # changes are reflected outside the function.
# print(f"one is: {one}")     # two
# print(f"two is: {two}")     # three
# print(f"three is: {three}") # one

# Q4 -------------------------------------------------------------------------

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     print(dot_separated_words)

#     if len(dot_separated_words) != 4:
#         return False

#     while dot_separated_words:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False

#     return True

# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# print(is_dot_separated_ip_address("1.4.5.11"))

# Q5 -------------------------------------------------------------------------

# if False:
#     greeting = "hello world"

# print(greeting) # NameError

# def append_to(str1, str2):
#     for char in str2:
#         str1 += char

#     return str1


# lst1 = ["a", "b", "c"]
# lst2 = "d"
# append_to(lst1, lst2)
# print(lst1)

# continue studying from here - What Code Does
# https://launchschool.com/lessons/1318de4f/assignments/ff1c7aa8

