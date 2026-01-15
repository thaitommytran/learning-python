# Multiple assignments
n, m = 0, "abc"
n, m, z = 0, "abc", False

# Increment
n = n + 1  # good
n += 1  # bad
# n++ # bad

# None is null (absense of value)
n = None
print("n =", n)  # returns n = None

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
    print(n)  # returns 0 1 2 3 4
    n += 1

# For loops
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)  # returns 0 1 2 3 4

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)  # returns 2 3 4 5

# Looping from i = 5 to i = 1
for i in range(5, 0, -1):
    print(i)  # returns 5 4 3 2 1

# Division is decimal by default
print(5 / 2)  # returns 2.5

# Double slash rounds down
print(5 // 2)  # returns 2

# CAREFUL: most languages round towards 0, but not python
# negative numbers will be rounded down
print(-3 // 2)  # returns -2

# A workaround for rounding towards 0 is to use decimal division first
print(int(-3 / 2))  # returns -1

# Modulo similar to most languages
# except for negative numbers
print(10 % 3)  # returns 1
print(-10 % 3)  # returns 2

# Math helpers
import math  # noqa: E402

print(math.fmod(-10, 3))  # returns -1
print(math.floor(3 / 2))  # returns 1
print(math.ceil(3 / 2))  # returns 2
print(math.sqrt(2))  # returns 1.4142135623730951
print(math.pow(2, 3))  # returns 8

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200) < float("inf"))  # returns True

# Lists (similar to arrays in other languages)
arr = [1, 2, 3, 4, 5]
print(arr)  # returns [1, 2, 3, 4, 5]

# Can be used as stack
arr.append(6)  # returns [1, 2, 3, 4, 5, 6]
arr.pop()  # returns [1, 2, 3, 4, 5]

# Can be used as queue
arr.insert(0, 0)  # returns [0, 1, 2, 3, 4, 5]
arr.pop(0)  # returns [1, 2, 3, 4, 5]

# Assignment
arr[0] = 10
arr[3] = 0
print(arr)  # returns [10, 2, 3, 0, 5]

# Initialize list of size n with default value of 0
n = 10
arr = [0] * n
print(arr)  # returns [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(len(arr))  # returns 10

# CAREFUL: -1 is not out of bounds, it's the last element
print(arr[-1])  # returns 0

# Indexing at -2 is the second to last element, etc.
print(arr[-2])  # returns 5

# Sublist (aka slicing)
arr = [1, 2, 3, 4, 5]
print(arr[1:4])  # returns [2, 3, 4]

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # returns 1 2 3

# Looping through lists
nums = [1, 2, 3]

for i in range(len(nums)):  # Using index
    print(nums[i])  # returns 1 2 3

for num in nums:  # Using value
    print(num)  # returns 1 2 3

for i, n in enumerate(nums):  # Using index and value
    print(i, n)  # returns 0 1 1 2 2 3

# Looping through multiple lists simultaneously
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)  # returns 1 2 3 4 5 6

# Reversing a list
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # returns [5, 4, 3, 2, 1]

# Sorting a list
arr = [5, 4, 7, 3, 8]

arr.sort()
print(arr)  # returns [3, 4, 5, 7, 8]

arr.sort(reverse=True)
print(arr)  # returns [8, 7, 5, 4, 3]

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)  # returns ["alice", "bob", "doe", "jane"]

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)  # returns ["bob", "doe", "alice", "jane"]

# List Comprehensions
arr = [i for i in range(5)]
print(arr)  # returns [0, 1, 2, 3, 4]

arr = [i + i for i in range(5)]
print(arr)  # returns [0, 2, 4, 6, 8]

# 2D lists
arr = [[0] * 5 for _ in range(5)]
print(
    arr
)  # returns [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Strings (similar to arrays)
s = "abc"
print(s[0:2])  # returns "ab"

# Valid numeric strings can be converted
print(int("123") + int("123"))  # returns 246

# Numbers can be converted to strings
print(str(123) + str(123))  # returns "123123"

# In rare case you need ASCII values
print(ord("a"))  # returns 97
print(ord("A"))  # returns 65

# Combine a list of strings (with an empty string delimiter)
print("".join(["ab", "cd", "ef"]))  # returns "abcdef"

# Queues (double ended queue)
from collections import deque  # noqa: E402

queue = deque()

queue.append("a")
queue.append("b")
queue.append("c")
print(queue)  # returns deque(["a", "b", "c"])

queue.popleft()
print(queue)  # returns deque(["b", "c"])

queue.appendleft("z")
print(queue)  # returns deque(["z", "b", "c"])

queue.pop()
print(queue)  # returns deque(["z", "b"])
