# Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.

# You have to validate input:

# v can be anything (primitive or otherwise)
# if v is omitted, fill the array with undefined (None in Python, nil in Ruby)
# if n is 0, return an empty array
# if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
# When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.

# Code Examples

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

     prefill(3,1) --> [1,1,1]
    
     prefill(2,"abc") --> ['abc','abc']
    
     prefill("1", 1) --> [1]
    
     prefill(3, prefill(2,'2d'))
       --> [['2d','2d'],['2d','2d'],['2d','2d']]
      
     prefill("xyz", 1)
       --> throws TypeError with message "xyz is invalid"
       
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# My Solution
def prefill(n, v = None) -> list:
    is_int = isinstance(n, int) and not isinstance(n, bool)
    is_str = isinstance(n, str) and n.isdigit()
    
    if not (is_int or is_str):
        raise TypeError(f"{n} is invalid")
        
    n_int = int(n)
    
    if n_int < 0:
        raise TypeError(f"{n} is invalid")
        
    return [v] * n_int


# Best Solution
def prefill(n, v=None):
    if not str(n).isdigit():
        raise TypeError("{0} is invalid".format(n))
        
    return [v for i in range(0, int(n))]