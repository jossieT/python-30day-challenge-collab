# Exercises: Level 1
import sys
import os
from functools import reduce
# Add the path to the 'data' folder
sys.path.append(os.path.abspath('exercises/data'))
# Full or relative path to the file
file_path = os.path.abspath('exercises/data/countries-data.py')
with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        countries_data = eval(content)  # Safe here since you're reading your own data
# Now import the countries list
from countries import countries
from collections import Counter
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1. Explain the difference between map, filter, and reduce.
# Map applies a function to each item in an iterable and returns a new iterable with the results.
# Filter applies a function to each item in an iterable and returns a new 
# iterable with only the items that pass a certain condition.
# Reduce applies a function to the items in an iterable and reduces them to a single cumulative value.
#2. Explain the difference between higher order function, closure and decorator
# Higher order functions are functions that can take other functions as arguments or return them as results.
# A closure is a function that captures the local variables from its enclosing scope, 
# allowing it to access them even when called outside that scope.
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
#3. Define a call function before map, filter or reduce, see examples.
def call(values):
    for value in values:
        print(value)

def exercise_level_1():
    #1. Use for loop to print each country in the countries list.
    print("Countries in the countries list:")
    call(countries)
    #2. Use for to print each name in the names list.
    print("Names in the names list:")
    call(names)
    #3. Use for to print each number in the numbers list.
    print("Numbers in the numbers list:")
    call(numbers)


# Exercises: Level 2
def exercise_level_2():
    #1. Use map to create a new list by changing each country to uppercase in the countries list
    countries_upper = list(map(lambda country: country.upper(), countries))    
    #2. Use map to create a new list by changing each number to its square in the numbers list
    numbers_squared = list(map(lambda number: number**2, numbers))
    #3. Use map to change each name to uppercase in the names list
    names_upper = list(map(lambda name: name.upper(), names))
    #4. Use filter to filter out countries containing 'land'.
    country_with_land = list(filter(lambda country: 'land' in country, countries))
    #5. Use filter to filter out countries having exactly six characters.
    county_six_lettered_country = list(filter(lambda country: len(country) == 6, countries))
    #6. Use filter to filter out countries containing six letters and more in the country list.
    county_six_and_more_lettered_country = list(filter(lambda country: len(country) >= 6, countries))
    #7. Use filter to filter out countries starting with an 'E'
    country_starting_With_letter_E = list(filter(lambda country: country.startswith("E"), countries))
    return countries_upper, numbers_squared, names_upper, country_with_land, county_six_lettered_country, county_six_and_more_lettered_country, country_starting_With_letter_E
#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(list_parameter):
    return [element for element in list_parameter if type(element) == str]
#10. Use reduce to sum all the numbers in the numbers list.
sum_of_numbers = reduce(lambda num1, num2: num1+num2, numbers)
#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concatenated_countries = reduce(lambda country1, country2: country1 + ", " + country2, countries[:-1])
sentence = concatenated_countries + ", and " + countries[-1] + " are north European countries."
print(sentence)
#12. Declare a function called categorize_countries that returns a list of countries with some common 
# pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries():
    land_countries = list(filter(lambda country: 'land' in country, countries))
    ia_countries = list(filter(lambda country: 'ia' in country, countries))
    island_countries = list(filter(lambda country: 'island' in country, countries))
    stan_countries = list(filter(lambda country: 'stan' in country, countries))
    
    return {
        'land': land_countries,
        'ia': ia_countries,
        'island': island_countries,
        'stan': stan_countries
    }

#13. Create a function returning a dictionary, where keys stand for starting letters of 
# countries and values are the number of country names starting with that letter.

def starting_letter_counts():
    letter_count = {}
    for country in countries:
        if country[0] in letter_count:
            letter_count[country[0]] += 1
        else:
            letter_count[country[0]] = 1
    return letter_count
    


#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the 
# countries.js list in the data folder.

def get_first_ten_countries():
    return list(filter(lambda country: country, countries[:10]))

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return list(filter(lambda country: country, countries[-10:]))
# Exercises: Level 3
#1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 
# file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort by name
def countries_data_operator():
    countries_by_name = sorted(countries_data, key=lambda x: x['name'])
    # Sort by capital (some countries may not have a capital)
    countries_by_capital = sorted(countries_data, key=lambda x: x.get('capital'))

    # Sort by population (descending)
    countries_by_population = sorted(countries_data, key=lambda x: x.get('population'), reverse=True)

    # Sort out the ten most spoken languages by location.

    all_languages = []
    for country in countries_data:
        all_languages.extend(country.get('languages', []))
    language_counts = Counter(all_languages)
    most_spoken_languages = language_counts.most_common(10)
    # Sort out the ten most populated countries.
    ten_most_populated_countries = countries_by_population[:10]
    # Print results
    print("Countries by name (first 5):", [c['name'] for c in countries_by_name[:5]])
    print("Countries by capital (first 5):", [c['name'] for c in countries_by_capital[:5]])
    print("Countries by population (first 5):", [c['name'] for c in countries_by_population[:5]])
    print("Ten most spoken languages:", most_spoken_languages)
    print("Ten most populated countries:", [c['name'] for c in ten_most_populated_countries])

# Decorators
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper





if __name__ == "__main__":
    # Print results from Level 1 exercises
    print("Exercise Level 1:")
    exercise_level_1()
    # Print results from Level 2 exercises
    countries_upper, numbers_squared, names_upper, country_with_land, \
    county_six_lettered_country, county_six_and_more_lettered_country, country_starting_With_letter_E = \
    exercise_level_2()
    print(f"Countries in uppercase: {countries_upper}")

    # Print categorized countries
    print(f"Countries categorized by suffixes: {categorize_countries()}")
    # Print starting letter counts
    print(f"Starting letter counts: {starting_letter_counts()}")
    # Print first ten countries
    print(f"First ten countries: {get_first_ten_countries()}")
    # Print last ten countries
    print(f"Last ten countries: {get_last_ten_countries()}")
    # Call the function to sort countries data
    countries_data_operator()

# Decorate the greeting function
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']








