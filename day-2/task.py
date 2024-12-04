# d2.14
# Subscripting
# print("Hello World"[-1])

# Strings
# print("123" + "456")  # Concatenation

# Integers = Whole Numbers
# print(123 + 456)

# Large Integers
# print(123_456 + 789)

# Float = Floating Point Number
# print(3.141592653589793)

# Boolean = True or False
# print(len('hello world'))

name = 'ryan'
large_number = 123_456_789
large_float = 123_456.123
boolean_value = True

# print(type(boolean_value))
# print(type(name))
# print(type(large_number))
# print(type(large_float))

# Type Conversion aka Type Casting
# print("123" + "456")
# print(int("123") + int("456"))
#
# print("Number of letters in your name: " + str(len(input("Enter your name"))))

# PEMDAS
# ( )
# **
# * OR /
# + OR -
print(2*(2+3))
print(3 * 3 + 3 / 3 - 3)

# bmi calculator
# bmi = weight / height (in meters) ** 2
weight = 214
height_in_inches = 68
bmi = (weight / height_in_inches ** 2) * 703
print(str(round(bmi, 2)) + '%')

# F strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, due to your {height}. Results for winning: {is_winning} ")
