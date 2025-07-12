import os
import sys
file_path = os.path.abspath('exercises/data/countries-data.py')
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    countries_data = eval(content)  # Safe here since you're reading your own data
# Exercises: Level 1
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum_of_two_numbers = num1 + num2
    return sum_of_two_numbers
#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    PI = 3.14
    area = PI*radius**2
    return area

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(degree_celsius):
    degree_fahrenheit = (degree_celsius*9/5) + 32
    return degree_fahrenheit
#5. Write a function called check-season, it takes a month parameter and returns the season:
#  Autumn, Winter, Spring or Summer.

def check_season(month):
    season = None
    season_dict = {'Autumn':['September', 'October', 'November'],
               'Winter':['December', 'January', 'February'],
               'Spring': ['March', 'April', 'May'],
               'Summer':['June', 'July', 'August']
               }
    for key in season_dict:
        months = season_dict[key]
        if month in months:
            season = key
            break
        else:
            continue
    return season
    
#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    if x2-x1 == 0:
        print("Slope is undefined which it is vertical line.")
    else:
        slope = (y2-y1)/(x2-x1)
    return slope

#7. Quadratic equation is calculated as follows: 
# ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    if b**2<4*a*c:
        return
    else:
        solution = [(-b+(b**-4*a*c)**0.5)/(2*a), (-b-(b**-4*a*c)**0.5)/(2*a)]
        return solution
#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list_parameter):

    for i in range(len(list_parameter)):
        print(list_parameter[i])
        

#9. Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reverse_list = []
    for i in range(len(array)-1, -1, -1):
        reverse_list.append(array[i])
    return reverse_list

#10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list_items):
    for i in range(len(list_items)):
        list_items[i] = str(list_items[i]).capitalize()
    return list_items  
#11.Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(list_parameter:list, item):
    list_parameter.append(item)
    return list_parameter

#12. Declare a function named remove_item. 
# It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(variable_list:list, item):
    if item in variable_list:
        variable_list.remove(item)
    else:
        print(f"{item} not found in the list.")
    return variable_list

#13.Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    i = 0
    sum_in_the_range_number = 0
    while i <= number:
        sum_in_the_range_number += i

    return sum_in_the_range_number

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    number = abs(number)  # Handle negative input safely

    if number == 0:
        return 0

    if number % 2 != 0:
        return number + sum_of_odds(number - 1)
    else:
        return sum_of_odds(number - 1)

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    number = abs(number)
    if number == 0:
        return 0
    if number%2 == 0:
        return number + sum_of_even(number-1)
    else:
        return sum_of_even(number-1)
# Exercises: Level 2
#1. Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(positive_integer):
    positive_integer = abs(positive_integer)
    odd_count = 0
    even_count = 0
    if positive_integer == 0:
        return 0
    for i in range(positive_integer+1):
        if i%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(whole_number):
    whole_number = abs(whole_number)
    if whole_number == 0:
        return 0
    elif whole_number == 1:
        return 1
    else:
        return whole_number*factorial(whole_number-1)
#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(bolean_parameter):
    if bolean_parameter == 0:
        return False
    else:
        return True
#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation). 
def calculate_mean(list_variable):
    sum_of_list = 0
    for i in range(len(list_variable)):
        sum_of_list += list_variable[i]
    return sum_of_list/len(list_variable)
def calculate_median(list_variable:list):
    list_variable.sort()
    median = 0
    if len(list_variable)%2 == 0:
        median = list_variable[list_variable/2-1:len(list_variable)+1]
    else:
        median = list_variable[len(list_variable)//2]
    return median
def calculate_mode(list_variable: list):
    mode_dict = {}
    for item in list_variable:
        if item in mode_dict:
            mode_dict[item] += 1
        else:
            mode_dict[item] = 1

    max_freq = max(mode_dict.values())

    if max_freq == 1:
        print("The list has no mode.")
        return []

    mode_list = [key for key, value in mode_dict.items() if value == max_freq]

    print(f"The mode(s): {mode_list}")
    return mode_list 

    
def calculate_range(list_variable):
    max_value = max(list_variable)
    min_value = min(list_variable)
    range = max_value-min_value
    return range
def calculate_variance(list_variable):
    mean = calculate_mean(list_variable)
    N = len(list_variable)
    variannce = sum((x - mean) ** 2 for x in list_variable) / N
    return variannce
def calculate_std(list_variable):
    standard_deviation = calculate_variance(list_variable) ** 0.5
    return standard_deviation
# Exercises: Level 3
#1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    count = 0
    for i in range(1, number):
        if number%2 == 0:
            count += 1
        else:
            continue
    if count == 1 or count == 2:
        return True
    else:
        return False
    
#2. Write a functions which checks if all items are unique in the list.
def are_all_items_of_the_list_unique(items_list):
    for i in range(len(items_list)):
        for j in range(i+1, len(items_list)):
            if items_list[i] == items_list[j]:
                return False
    return True

#3. Write a function which checks if all the items of the list are of the same data type.
def is_data_type_of_all_items_the_same(items_list):
    for i in range(len(items_list)):
        for j in range(i+1, len(items_list)):
            if type(items_list[i]) != type(items_list[j]):
                return False
    return True
#4. Write a function which check if provided variable is a valid python variable
def is_variable_valid_python_variable(input_variable:str):
    if input_variable.isidentifier():
        return True
    else:
        return False    
#5. Go to the data folder and access the countries-data.py file.
#. Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
#. Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_spoken_languages():

    language_counter = []
    languages_dict = {}
    for country in countries_data:
        languages = country['languages']
        for i in range(len(languages)):
            language_counter.append(languages[i])
    # Display the total number of languages in the data
    print(f'✅The total number of languages in the data are {len(language_counter)}')
    for i in range(len(language_counter)):
        if language_counter[i] in languages_dict:
            languages_dict[language_counter[i]] += 1
        else:
            languages_dict[language_counter[i]] = 1
    
    # Displaying the ten most spoken languages in the data
    sorted_languages = dict(sorted(languages_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_languages)
    print(f'✅The ten most spoken languages are: {list(sorted_languages.keys())[:10]}')
    
def most_populated_countries():
    countries_list = []
    population_list = []
    population_dict = {}
    for country in countries_data:
        nation = country['name']
        countries_list.append(nation)
        population = country['population']
        population_list.append(population)
    for i in range(len(countries_list)):
        population_dict[countries_list[i]] = population_list[i]
    
    sorted_populaton = dict(sorted(population_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_populaton)
    print(f'✅The ten most populated countries are: {list(sorted_populaton.keys())[:10]}')

if __name__ == '__main__':

    add_two_numbers(num1=3, num2=5)
    area_of_circle(3.5)
    print(add_all_nums(3, 4, 6, 7, 8, 9, 1, 8, 3, 8,3, 5))
    convert_celsius_to_fahrenheit(37)
    print(check_season("September"))
    print(calculate_slope(-2, 4, -3, -5))
    print(solve_quadratic_eqn(-2, -3, -4))
    print_list(['P', 'Y', 'T', 'H', 'O', 'N'])
    print(reverse_list(['P', 'Y', 'T', 'H', 'O', 'N']))
    print(capitalize_list_items(['python', 'mongodb', 'html', 'css', 'java', 'javascript']))
    print(add_item(['python', 'mongodb', 'html', 'css', 'java', 'javascript'], 'c++'))
    print(remove_item(['python', 'mongodb', 'html', 'css', 'java', 'javascript'], 'javascript'))
    print(f"Sum of all odd numbers in the given range is {sum_of_odds(-8)}")
    print(f"Sum of all even numbers in the given range is {sum_of_even(-8)}")
    print(f"The total number of evens and odds in the range of given integer are {evens_and_odds(100)}")
    print(calculate_mode([1,3,6,7,3,1,2,1,6,1,3,3, 4,2,1,2,2,2,6,6,6]))
    is_variable_valid_python_variable('my_variable')
    print(f"The mean of the list is {calculate_mean([1,2,3,4,5,6,7,8,9])}")
    print(f"The median of the list is {calculate_median([1,2,3,4,5,6,7,8,9])}")
    print(f"The range of the list is {calculate_range([1,2,3,4,5,6,7,8,9])}")
    print(f"The variance of the list is {calculate_variance([1,2,3,4,5,6,7,8,9])}")
    print(f"The standard deviation of the list is {calculate_std([1,2,3,4,5,6,7,8,9])}")
    print(f"The factorial of the number is {factorial(5)}")
    are_all_items_of_the_list_unique([1,2,3,4,5,6,7,8,9])
    is_prime(77)
    is_data_type_of_all_items_the_same([1,2,3,4,5,6,7,8,9])
    most_populated_countries()
    most_spoken_languages()