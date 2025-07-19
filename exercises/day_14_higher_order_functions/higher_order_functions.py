#Exercises: Day 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Exercises: Level 1
#1. Explain the difference between map, filter, and reduce.
'''
    - map - Applies a function to each element of an iterable 
           (like a list) and returns a new iterable (like a list or map object).
           - Syntax map(function, iterable)
    - filter -Applies a condition (a function that returns True or False) and 
              keeps only the elements that meet the condition.
             - Syntax filter(condition, iterable)
    - reduce (needs import from functools) - Takes all elements and reduces them to a 
              single value by applying a function cumulatively.
             - Syntax reduce(function, iterable)-
'''

#2. Explain the difference between higher order function, closure and decorator
'''
    - Higher-Order Function - A function that takes another function as an argument or returns a function as its result.
                            - Use case: Used for functional programming like map(), filter(), reduce(), or custom logic.
    - Closure - A function object that remembers values from its enclosing scope, even after that scope has finished execution.
              - Use case: Helps preserve state in a nested function.
    - Decorator - A special type of higher-order function used to modify or extend the behavior of another function without changing its code.
                - Use case: Logging, authentication, timing, etc.
                - Syntax shortcut: @decorator_name
'''
#3. Define a call function before map, filter or reduce, see examples.
'''
    - map(function, iterable)
        Purpose: Applies a function to each item in an iterable.
        Define function before using map:
        
        def square(x):
            return x * x
        
        numbers = [1, 2, 3, 4]
        result = map(square, numbers)  # map calls square(x) on each item
        print(list(result))  # [1, 4, 9, 16]
    -filter(function, iterable)
        Purpose: Filters items in an iterable using a function that returns True or False.
        Define function before using filter:
        
        def is_even(x):
            return x % 2 == 0
        
        numbers = [1, 2, 3, 4, 5]
        result = filter(is_even, numbers)
        print(list(result))  # [2, 4]
    - reduce(function, iterable)
        reduce() is from the functools module.
        
        Purpose: Applies a function cumulatively to reduce iterable to a single value.
        Define function before using reduce:
        
        from functools import reduce
        
        def multiply(x, y):
            return x * y
        
        numbers = [1, 2, 3, 4]
        result = reduce(multiply, numbers)  # ((((1*2)*3)*4))
        print(result)  # 24
'''

#4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
for name in names:
    print(name)

#6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)

#xercises: Level 2
#1. Use map to create a new list by changing each country to uppercase in the countries list
def to_uppercase(country_name):
    return country_name.upper()

changed_uppercase = map(to_uppercase, countries)
print(list(changed_uppercase))

#2. Use map to create a new list by changing each number to its square in the numbers list
def square(num):
    return num ** 2

squared_list = map(square, numbers)
print(list(squared_list))

#3. Use map to change each name to uppercase in the names list
def change_to_uppercase(name_value):
    return name_value.upper()

changed_to_upper = map(change_to_uppercase, names)
# reassigning new changed values to names list
names = list(changed_to_upper)
print(names)

#4. Use filter to filter out countries containing 'land'.
def find_country_with_land(country_value):
    if 'land' in country_value:
        return True
    else:
        return False

filter_country = filter(find_country_with_land, countries)
print(list(filter_country))
#5. Use filter to filter out countries having exactly six characters.
def country_with_6_char(country):
    if len(country) == 6:
        return True
    else:
        return False

country_with_6_char = filter(country_with_6_char, countries)
print(list(country_with_6_char))

#6. Use filter to filter out countries containing six letters and more in the country list.
def country_with_6_and_more_char(country):
    if len(country) >= 6:
        return True
    else:
        return False

country_with_6_more_char = filter(country_with_6_and_more_char, countries)
print(list(country_with_6_more_char))

#Use filter to filter out countries starting with an 'E'
def country_starting_with_e(country):
    if country.startswith('E'):
        return True
    else:
        return False

country_start_with_e = filter(country_starting_with_e, countries)
print(list(country_start_with_e))