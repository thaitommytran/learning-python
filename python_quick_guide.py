# Multiple assignments
n, m = 0, "abc"
n, m, z = 0, "abc", False

# Increment
n = n + 1  # good
n += 1  # bad
# n++ # bad

# None is null (absense of value)
n = None
print("n =", n)

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
