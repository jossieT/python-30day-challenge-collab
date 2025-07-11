import math
import keyword
import json
#Exercises: Day 11
#Exercises: Level 1
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(4,9))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r, PI = 3.14):
    area = PI * r * r
    return area
print(area_of_circle(5))

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types.
#If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == str:
            return num, 'is not number in the list cannot perform addition'
        else:
            total += num
    return total
print('total sum of nums is ', add_all_nums(3,5,4,5,6,5)) #28
print('total sum of nums is ', add_all_nums(3,'s',5,6,5)) # displays message

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#Write a function which converts °C to °F,convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(cels):
    fahrenheit = (cels *(9/5)) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(30))

#5. Write a function called check-season, it takes a month parameter and
#returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    seasons = {
    'Autumn': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August'],
    }

    if month in seasons['Autumn']:
        return 'Autumn'
    elif month in seasons['Winter']:
        return 'Winter'
    elif month in seasons['Spring']:
        return 'Spring'
    elif month in seasons['Summer']:
        return 'Summer'
    else :
        return f'Invalid input {month} please correct enter again'
    
print(check_season('November'))
print(check_season('June'))

#6, Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print('slope = ', calculate_slope(x1 = 1, y1 = 2, x2 = 4, y2 = 8)) 
    
#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a
#function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    d = (b * b) - (4*a*c)
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return f"Two real roots: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2*a)
        return f"One real root: x = {x}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-d) / (2 * a)
        return f"Two complex roots: x1 = {real_part}+{imaginary_part}i, x2 = {real_part}-{imaginary_part}i"

print(solve_quadratic_eqn(1, -3, 2))

#8. Declare a function named print_list. It takes a list as a
#parameter and it prints out each element of the list.
def print_list(lst):
    if type(lst) != list:
        return 'The entered data is not a List'
    c = 1
    for l in lst:
        print(f"Item {c}: {l}")
        c += 1

print_list([7,4,5,5,3,4,5])

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns
#the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = list()
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

print(reverse_list([4,7,4,6,2,8,9]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it
#returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_words = []
    for i in range(0,len(lst)):
        capitalized_words.append(lst[i].capitalize())
    return capitalized_words

print(capitalize_list_items(["python", "javaScript", "react", "nodeJS"]))

#11. Declare a function named add_item. It takes a list and an item parameters.
#It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
    

#12. Declare a function named remove_item. It takes a list and an item parameters.
#It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
    
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

#13. Declare a function named sum_of_numbers.
#It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    total = 0
    for num in range(number + 1):
        total += num
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))

#14. Declare a function named sum_of_odds.
#It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i%2 != 0:
            total += i
    return total
print(sum_of_odds(10))
print(sum_of_odds(20))

#15. Declare a function named sum_of_even.
#It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(n):
    total = 0
    for i in range(n+1):
        if i%2 == 0:
            total += i
    return total
print(sum_of_even(10))
print(sum_of_even(20))

#Exercises: Level 2
#1. Declare a function named evens_and_odds . It takes a
#positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even = 0
    odd = 0
    for i in range(n+1):
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return f'number of odds are {odd} \nnumber of evens are {even}'

print(evens_and_odds(100))

#Call your function factorial, it takes a whole number as a parameter and it
#return a factorial of the number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))

#2. Call your function is_empty,
#it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if not value:
        return True
    else:
        return False

print(is_empty({}))
print(is_empty(' '))

#Write different functions which take lists. They should calculate_mean, calculate_median,
#calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def calculate_mode(numbers):
    frequency = {}
    
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]

    return modes if len(modes) > 1 else modes[0]

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

data = [1, 2, 2, 3, 4, 5, 6]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

#Exercises: Level 3

#1. Write a function called is_prime, which checks if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n% i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(11))
print(is_prime(15))

#2. Write a functions which checks if all items are unique in the list.
def is_items_unique(lst):
    set_items = set(lst)
    if len(set_items) == len(lst):
        return True
    else:
        return False

print(is_items_unique([1, 2, 3, 4]))            
print(is_items_unique(['a', 'b', 'c']))
print(is_items_unique(['a', 'b', 'a'])) 

#3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(items):
    intial_type = type(items[0])
    for item in items:
        if type(item) != intial_type:
            return False
    return True

print(same_data_type([1, 2, 3]))
print(same_data_type([1, 'a', 3]))

#4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_variable("my_var"))     
print(is_valid_variable("2nd_var")) 
print(is_valid_variable("for"))   

#4. go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 
#10 or 20 most spoken languages in the world in descending order
countries = []
with open('exercises/day_10_loops/countries_data.json', 'r', encoding='utf-8') as f:
    countries_data = json.load(f)
    countries = countries_data['countries']

def most_spoken_languages(countries):
    most_spoken_languages = {}
    for country in countries:
        for language in country['languages']:
            if language in most_spoken_languages:
                most_spoken_languages[language] += 1
            else:
                most_spoken_languages[language] = 1
        else:
            most_spoken_languages[language] = 1

    language_counts = list(most_spoken_languages.items())
    for i in range(len(language_counts)):
        for j in range(i + 1, len(language_counts)):
            if language_counts[j][1] > language_counts[i][1]:
                language_counts[i], language_counts[j] = language_counts[j], language_counts[i]
    most_spoken_languages = language_counts[:10]
    return most_spoken_languages



#Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries):
    most_populated_countries = {}
    for country in countries:
        most_populated_countries[country['name']] = country['population']

    population_counts = list(most_populated_countries.items())
    for i in range(len(population_counts)):
        for j in range(i + 1, len(population_counts)):
            if population_counts[j][1] > population_counts[i][1]:
                population_counts[i], population_counts[j] = population_counts[j], population_counts[i]
    most_populated_countries = population_counts[:10]
    return most_populated_countries