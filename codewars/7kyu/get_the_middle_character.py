# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.

# Code Examples

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# My Solution
def get_middle(s):
    if len(s) % 2 == 0:
        i = int(len(s) / 2)
        return f"{s[i - 1]}{s[i]}"
    else:
        return s[len(s) // 2]
    pass

# Best Solution
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]