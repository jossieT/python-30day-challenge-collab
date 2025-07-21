"""#SyntaxError
#Example 1: SyntaxError
print 'hello world' # Missing parentheses

#NameError
#Example 1: NameError
print(age) #age is not defined

#IndexError
#Example 1: IndexError
numbers = [1, 2, 3, 4, 5]
numbers[5] # list index out of range

#ModuleNotFoundError
#Example 1: ModuleNotFoundError
import maths #No module named 'maths'

#AttributeError
#Example 1: AttributeError
import math
math.PI # module 'math' has no attribute 'PI'

#KeyError
#Example 1: KeyErrorKeyError
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['county'] #KeyError: 'county'

#TypeError
#Example 1: TypeError
print(4 + '3') #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#ImportError
#Example 1: TypeError
from math import power #ImportError: cannot import name 'power' from 'math'

#ValueError
int('12a') # ValueError: invalid literal for int() with base 10: '12a'

#ZeroDivisionError
1 / 0 #ZeroDivisionError: division by zero

"""
