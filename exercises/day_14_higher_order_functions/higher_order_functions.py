#Exercises: Day 14
from functools import reduce
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
import countries as countries_list

import json
from collections import Counter

with open('countries_data.json', 'r', encoding='utf-8') as file:
    countries_items = json.load(file)

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

#7. Use filter to filter out countries starting with an 'E'
def country_starting_with_e(country):
    if country.startswith('E'):
        return True
    else:
        return False

country_start_with_e = filter(country_starting_with_e, countries)
print(list(country_start_with_e))
#8.  Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
'''scenario - Converts all  names to uppercase.
              Filters the names that start with the letter "A".
              Reduce the result to a single string, joined with a dash (-).'''
def name_to_upper(name):
    return name.upper()


def filter_name_starts_with_a(name):
    if name.startswith('A'):
        return True
    else:
        return False

#Using Chain of two or more list iterators
chained_list = reduce(lambda x,y: x + '-' + y, filter(filter_name_starts_with_a, map(name_to_upper, names)))

#9. Declare a function called get_string_lists which takes a list as a parameter and then
# returns a list containing only string items.
lst = ['Asabeneh',  1, 'Lidiya', True, 'Ermias', 9.8, 'Abraham']
def string_checker(list_item):
    if type(list_item) == str:
        return True
    else:
        return False

def get_string_lists(list_items):
    string_list = list(filter(string_checker, lst))
    return string_list

print(get_string_lists(lst))

#10. Use reduce to sum all the numbers in the numbers list.

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

#11. Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def string_add(x, y):
    if x == 'Iceland' or y == 'Iceland':
        return x + ' and ' + y
    else:
        return x + ',' + y

reduced_with_comma = reduce(string_add, countries)
print(reduced_with_comma)

def complete_string(string):
    complete_str = string + ' are north European countries'
    return complete_str

print(complete_string(reduced_with_comma))

#12. Declare a function called categorize_countries that returns a list of countries
# with some common pattern (you can find the countries list in this repository as
# countries.js(eg 'land', 'ia', 'island', 'stan')).

def categorize_countries(country):
    if 'land' in country:
        return True
    return False
print(list(filter(categorize_countries, countries_list)))

#13. Create a function returning a dictionary, where keys stand for starting letters of
# countries and values are the number of country names starting with that letter.
def countries_by_starting_letter(countries):
    new_dictionary = {}
    first_letters = map(lambda country: country[0], countries)
    first_letters_list = list(first_letters)

    for char in first_letters_list:
        value = len(list(filter(lambda country: country.startswith(char), countries)))
        new_dictionary[char] = value


    return new_dictionary

print(countries_by_starting_letter(countries_list))

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the
# countries.js list in the data folder.
def get_first_ten_countries(countries):
    first_ten = list(countries[0:10])
    return first_ten
print(get_first_ten_countries(countries_list))

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
    last_ten = list(countries[-10:])
    return last_ten
print(get_last_ten_countries(countries_list))

#Exercises: Level 3
'''1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
    Sort countries by name, by capital, by population
    Sort out the ten most spoken languages by location.
    Sort out the ten most populated countries.
'''

by_name = sorted(countries_items, key=lambda x: x['name'])

# Sort by capital
by_capital = sorted(countries_items, key=lambda x: x['capital'])

# Sort by population (ascending)
by_population_asc = sorted(countries_items, key=lambda x: x['population'])

# Sort by population (descending)
by_population_desc = sorted(countries_items, key=lambda x: x['population'], reverse=True)

print("First 5 countries sorted by name:")
for country in by_name[:5]:
    print(country['name'])

print("\nFirst 5 countries sorted by capital:")
for country in by_capital[:5]:
    print(country['capital'])

print("\nTop 5 most populous countries:")
for country in by_population_desc[:5]:
    print(country['name'], "-", country['population'])

language_counts = Counter()

for country in countries_items:
    for language in country.get("languages", []):
        language_counts[language] += 1

# Get the 10 most common languages
most_spoken_languages = language_counts.most_common(10)

# Print results
print("Top 10 Most Spoken Languages by Number of Countries:")
for lang, count in most_spoken_languages:
    print(f"{lang}: {count} countries")

sorted_by_population = sorted(countries_items, key=lambda c: c.get('population', 0), reverse=True)

# Get the top 10 most populated countries
top_10_populated = sorted_by_population[:10]

# Print the results
print("Top 10 Most Populated Countries:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']:,} people")

