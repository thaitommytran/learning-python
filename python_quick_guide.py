# Multiple assignments
import _typeshed.importlib

n, m = 0, "abc"
n, m, z = 0, "abc", False

# Increment
n = n + 1  # good
n += 1  # bad
# n++ # bad

# None is null (absense of value)
n = None
print("n =", n)  # n = None

# If statements don't need parentheses or curly braces
n = 1

if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions
# (python) and = && (javascript)
# (python) or = || (javascript)
n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1

# While loops are similar (no parentheses or curly braces)
n = 0
while n < 5:
    print(n)  # 0 1 2 3 4
    n += 1

# For loops
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)  # 0 1 2 3 4

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)  # 2 3 4 5

# Looping from i = 5 to i = 1
for i in range(5, 0, -1):
    print(i)  # 5 4 3 2 1

# Division is decimal by default
print(5 / 2)  # 2.5

# Double slash rounds down
print(5 // 2)  # 2

# CAREFUL: most languages round towards 0, but not python
# negative numbers will be rounded down
print(-3 // 2)  # -2

# A workaround for rounding towards 0 is to use decimal division first
print(int(-3 / 2))  # -1

# Modulo similar to most languages
# except for negative numbers
print(10 % 3)  # 1
print(-10 % 3)  # 2

# Math helpers
import math

print(math.fmod(-10, 3))
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))
