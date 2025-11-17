# Import math module
import math

# Python Basics
print("Hello World 😁")
print("*" * 10)

# Arithmetic Operators
2 + 3

# Variables
x = 1
y = 2
unit_price = 3

# Data Types
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)

# String Methods
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# Escape Sequences
course = "Python \"Programming"
print(course)

course = "Python \'Programming"
print(course)

course = "Python \\Programming"
print(course)

course = "Python \nProgramming"
print(course)

# Formatted Strings
first = "Tommy"
last = "Tran"
full = f"{first} {last}"
print(full)

# String Methods
course = " python programming "
print(course.upper())  # Converts the string to uppercase
print(course.lower())  # Converts the string to lowercase
print(course.title())  # Converts the string to title case

print(course.strip())  # Removes the whitespace from both sides of string
print(course.lstrip())  # Removes the whitespace from left side of string
print(course.rstrip())  # Removes the whitespace from right side of string

print(course.find("pro"))  # Finds index of first occurrence of substring
print(course.find("Pro"))  # Case sensitive, returns -1 if not found

print(course.replace("p", "j"))  # Replaces all occurrences of substring with new substring
print("pro" in course)  # Checks if substring is present in string, returns True or False
print("swift" not in course)  # Checks if substring is not present in string, returns True or False

# Numbers
x = 1
x = 1.1
x = 1 + 2j  # a + bi

# Arithmetic Operators
print(10 + 3)  # Addition
print(10 - 3)  # Subtraction
print(10 * 3)  # Multiplication
print(10 / 3)  # Division
print(10 // 3)  # Floor Division
print(10 % 3)  # Modulus
print(10 ** 3)  # Exponentiation

# Comparison Operators
print(10 > 3)
print(10 < 3)
print(10 >= 3)
print(10 <= 3)
print(10 == 3)
print(10 != 3)

# Math Functions
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))  # Rounds up to nearest integer
print(math.floor(2.2))  # Rounds down to nearest integer


print(math.comb(5, 2))  # Calculates number of ways to choose 2 items from 5 without repetition
print(math.factorial(5))  # Calculates factorial of 5
print(math.gcd(10, 20))  # Calculates greatest common divisor of 10 and 20
print(math.isqrt(16))  # Calculates square root of 16
print(math.lcm(10, 20))  # Calculates least common multiple of 10 and 20
print(math.perm(5, 2))  # Calculates number of ways to choose 2 items from 5 without repetition and with order

# Type Conversion
x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

int(x)  # Converts x to an integer
float(x)  # Converts x to a float
bool(x)  # Converts x to a boolean
str(x)  # Converts x to a string

# Falsy Values
# "" # Empty string
# 0 # Zero
# None # None
# [] # Empty list
# {} # Empty dictionary
# () # Empty tuple
# False # False

# Truthy Values
# "Hello" # Non-empty string
# 1 # Non-zero number
# True # True
