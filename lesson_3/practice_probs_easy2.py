# https://launchschool.com/lessons/106644d9/assignments/73bff7e2

# Q1 -------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
# numbers.reverse()

# print(numbers)

# or

# i = -1
# for number in numbers:
#     i += 1
#     numbers.insert(i, numbers.pop(-1))

# print(numbers)

# or

# reversed_numbers = numbers[::-1] # best

# or

reversed_numbers = list(reversed(numbers))

# Q2 -------------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# Q3 -------------------------------------------------------------------------

# print(100 >= 42 >= 10)        # True
# print(100 >= 100 >= 10)       # True
# print(100 >= 101 >= 10)       # False

# # or (better)

# 42 in range(10, 101)          # True
# 100 in range(10, 101)         # True
# 101 in range(10, 101)         # False

# Q4 -------------------------------------------------------------------------

# lst = [1, 2, 3, 4, 5]
# del lst[2]

# print(lst)

# Q5 -------------------------------------------------------------------------

# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# # preferred
# print(isinstance(numbers, list))  # True
# print(isinstance(table, list))    # False

# # # bad
# # print(type(numbers) == list)
# # print(type(table) == list)

# # also bad
# # print(type(numbers) is list)      # True
# # print(type(table) is list)        # False

# Q6 -------------------------------------------------------------------------

# title = "Flintstone Family Members"

# title = title.center(40)

# print(title)

# Q7 -------------------------------------------------------------------------

# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# print(statement1.count("t") + statement2.count("t"))

# Q8 -------------------------------------------------------------------------

# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# print("Spot" in ages)


# Q9 -------------------------------------------------------------------------

ages = {
    'Herman': 32,
    'Lily': 30,
    'Grandpa': 402,
    'Eddie': 10,

}


additional_ages = {
    'Marilyn': 22,
    'Spot': 237,

}

ages.update(additional_ages)
print(ages)























