# https://launchschool.com/lessons/106644d9/assignments/dd68e036

# Q2 -------------------------------------------------------------------------
# def ends_with(string):
#     return string.endswith("!")


# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(ends_with(str1))
# print(ends_with(str2))

# Q3 -------------------------------------------------------------------------

# def four_score(string):
#     return "Four score and " + string

# famous_words = "seven years ago..."

# new_string = four_score(famous_words)

# # # or

# # famous_words = "seven years ago..."
# # four_score = "Four score and "

# # new_string = four_score + famous_words


# print(new_string)

# Q4 -------------------------------------------------------------------------

# munsters_description = "the Munsters are CREEPY and Spooky."
# new_string = munsters_description.capitalize()

# print(new_string)
# # => 'The munsters are creepy and spooky.'

# Q5 -------------------------------------------------------------------------

# def case_swap(string):
#     new_string = ""

#     for char in string:
#         if not char.isalpha():
#             new_string += char

#         elif char.islower():
#             new_string += char.upper()

#         elif char.isupper():
#             new_string += char.lower()

#     return new_string


# munsters = "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# print(case_swap(munsters))

# # or

# print(munsters.swapcase())

# Q6 -------------------------------------------------------------------------

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print("Dino" in str1)
# print("Dino" in str2)

# Q7 -------------------------------------------------------------------------

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)

# Q8 -------------------------------------------------------------------------

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# new_names = ["Dino", "Hoppy"]
# flintstones.extend(new_names)

# # # or

# # flintstones.extend(["Dino", "Hoppy"])

# print(flintstones)

# Q9 -------------------------------------------------------------------------

# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected output:
# # Few things in life are as important as

# advice = advice.split("house")[0]

# print(advice)

# Q10 ------------------------------------------------------------------------

advice = "Few things in life are as important as house training your pet dinosaur."

advice = advice.replace("important", "urgent")

print(advice)