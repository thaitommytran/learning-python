spacer = "------------------"
print(spacer)

# Print Statements
print("Welcome to Python 101!2")
print("Welcome to Python 101!")

print("Create hammer")
print("Create nails")
print("Use hammer and nails")
print(spacer)

# Variables and Type Casting
failed_subjects = 6
name = "John"

print("Dear Mrs Badger")
print("Your son " + name + " is failing " + str(failed_subjects) + " subjects.")
print(name + " will need to redo " + str(failed_subjects) + " courses.")

name = "Eric"

print(name + " is doing well in geography.")
print(spacer)

# Data Types
failed_subjects = 2.45
name = "John"
Boolean = True or False
a = "it's"
# b = 'it\'s'

print(type("hello"))
print(type(1))
print(type(1.64))
print(type(True))
print(spacer)

# Create appropriate Variables for Item name, the price
# and how many you have in stock
item_name = "Toy"
price = 3.50
stock = 77

is_in_inventory = True
print(item_name, price, stock)
print(spacer)

# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

customer_name = "Tommy"
number_of_passes = 7
tokens_per_pass = 100
price_per_pass = 5.99
tokens_required_per_game = 10

total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_required_per_game

print("Customer Name:", customer_name)
print("Passes Bought:", number_of_passes)
print("Total Tokens:", total_tokens)
print("Total Cost:", total_cost)
print("Games Available:", games_available)
print(spacer)

# User Input
name = input("What is your name?: ")
age = input("What is your age?: ")
print("Hello, " + name + "! You are " + age + " years old.")

num1 = input("Enter a digit: ")
num2 = input("Enter a second digit: ")
answer = float(num1) + float(num2)
print("The sum is:", answer)
print(spacer)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("What is your name: ")
distance_in_km = input("Enter distance in km: ")
distance_in_miles = float(distance_in_km) / 1.609
print(f"Hi {name.title()}! {distance_in_km} kilometers is equivalent to {round(distance_in_miles, 2)} miles.")