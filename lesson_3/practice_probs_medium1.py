# Q1 -------------------------------------------------------------------------

# My code
# def flintstones_rock(text):
#     spaces = ""
#     for _ in range(10):
#         print(f'{spaces}{text}')
#         spaces += " "

# flintstones_rock("The Flintstones Rock!")

# Better code
# def flintstones_rock():
#     for spaces in range(10):
#         print(" " * spaces + "The Flintstones Rock!")

# flintstones_rock()

# Q2 -------------------------------------------------------------------------

# # If you wanted factors for negatives as well
# def factors(number):
#     divisor = abs(number)
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)

#         divisor -= 1

#     return result

# print(factors(-100))

# # If you simply wanted positives
# def factors(number):
#     divisor = abs(number)
#     result = []
#     while divisor != 0:
#         if number % divisor > 0:
#             result.append(number // divisor)

#         divisor -= 1

#     return result

# print(factors(-100))

# Q3 -------------------------------------------------------------------------

# # mutates the original list represented by buffer
# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# # creates a new list and returns it
# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# Q4 -------------------------------------------------------------------------

# print(0.3 + 0.6) # .899999999999
# print(0.3 + 0.6 == 0.9) # False

# import math

# i = -0.3
# while i < 10:
#     print(i + 0.3)
#     i += 0.1

# print(math.isclose(0.3 + 0.6, 0.9)) # True

# Q5 -------------------------------------------------------------------------

# nan_value = float("nan")

# print(nan_value == float("nan"))

# import math

# nan_value = float("nan")

# print(math.isnan(nan_value))

# Q6 -------------------------------------------------------------------------

# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8)

# Q7 -------------------------------------------------------------------------

# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }
# # demo_dict starts off pointing to the munsters object. As a result, the
# # changes made within the function directly affect the munsters dictionary.
# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# mess_with_demographics(munsters)
# print(munsters)

# Q8 -------------------------------------------------------------------------

# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
#         return "rock" if fist2 == "rock" else "scissors"

# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# Q9 -------------------------------------------------------------------------

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# param == "no" evaluates to False since param is "yes".
# Due to the and operator, foo() is not executed because the first part of the
# and expression is already False.

# Since the left side of the or (the result of the and expression) is False,
# Python evaluates and returns the right side of the or, which is "no".
print(bar(foo())) # no

# Q10 ------------------------------------------------------------------------

# a = 42
# b = 42
# c = a

# # a and c reference the same object in memory, so their ids are the same.
# # b will, in this case, have the same id as a and c due to interning.
# # Therefore, the code will output True.
# print(id(a) == id(b) == id(c)) # True