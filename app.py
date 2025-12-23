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

# Conditional Statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")

print("Done")

# Ternary Operator
age = 22

# This code block can be replaced with a single line using the ternary operator
if age >= 18:
    message = "Eligible"
else :
    message = "Not Eligible"

# This line uses the ternary operator to achieve the same result
message = "Eligible" if age >= 18 else "Not Eligible"

print(message)

# Logical Operators
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Short-circuit Evaluation
if high_income and good_credit and not student:
    print("Eligible for loan")

# Chaining Comparison Operators
# age >= 18 and age < 65
age = 22

if 18 <= age < 65:
    print("Eligible for loan")

# Quiz
if 10 == "10":
    print("A")
elif "bag" > "apple" and "bag" > "car":
    print("B")
else:
    print("C")

# For Loops
for number in range(3):
    print("Attempt", number + 1)

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2): # Start, Stop, Step
    print("Attempt", number, number * ".")

# For Else
successful= False 

for number in range(3):
    print("Attempt")

    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times and failed")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables
for x in range(5):
    print(x)

print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)    

for x in [1, 2, 3, 4]:
    print(x)

shopping_cart = ["apple", "banana", "orange"]

for item in shopping_cart:
    print(item)

# While Loops
number = 100

while number > 0:
    print(number)
    number //= 2

command = "quit"

while command != "quit":
    command = input(">")
    print("ECHO", command)

command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite Loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break   

# Exercise
total = 0

for evens in range(1, 10):
    if evens % 2 == 0:
        total += 1
        print(evens)

print(f"We have {total} even numbers")

# Functions
def greet():
    print("Hi there")
    print("Welcome aboard")

greet()

# Arguments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Tommy", "Tran")
greet("John", "Smith")

# Types of Functions
# 1 - Perform a task
# 2 - Return a value
def get_greeting(name):
    return f"Hi {name}" 

message = get_greeting("Tommy")
file = open("content.txt", "w")
file.write(message)

# Keyword Arguments
def increment(number, by):
    return number + by

result = increment(2, 1)
print(result)

print(increment(2, by=1))

# Default Arguments
def increment(number, by=1):
    return number + by

print(increment(2))
print(increment(2, 5))

# Xargs
def multiply(x, y):
    return x * y

multiply(2, 3)

def multiply(*numbers):
    total = 1

    for number in numbers:
        total *= number
    
    return total

print(multiply(2, 3, 4, 5))