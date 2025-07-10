# Exercises: Level 1
#1. Iterate 0 to 10 using for loop, do the same using while loop.
# for loop
print('Iterate 0 to 10 using for loop.')
for i in range(0, 11, 1):
    print(i)
# while loop
i = 0
print('Iterate 0 to 10 using while loop.')
while i < 11:
    print(i)
    i += 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
# for loop
print('Iterate 10 to 0 using for loop.')
for i in range(10, -1, -1):
    print(i)
# while loop
print('Iterate 10 to 0 using while loop.')
i = 10
while i >= 0:
    print(i)
    i -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""  
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
print('Triangular shape')
for i in range(7):
    print('  '+'#'*i)
    print('')

print('')


#4. Use nested loops to create the following:
"""  
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
print('Rectangular shape')
for i in range(8):
    print('#  '*8)
    print('')

#5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
print('square of a natural number.')
for i in range(11):
    print(f'{i} x {i} = {i*i}')
#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
tech_skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in tech_skills:
    print(skill)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
print("Print only even numbers 0 to 100.")
for i in range(101):
    if i%2 ==0:
        print(i)
    else:
        continue

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("Print only odd numbers 0 to 100.")
for i in range(101):
    if i%2 !=0:
        print(i)
    else: continue


# Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""The sum of all numbers is 5050."""
print('Print the sum of all numbers 0 to 100.')
sum = 0
for i in range(101):
    sum += i
print(f'✅Sum of all numbers 0 to 100 is {sum}')

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
"""The sum of all evens is 2550. And the sum of all odds is 2500."""
print('Print the sum of all even and odd numbers 0 to 100.')
sum_of_all_odd_numbers = 0
sum_of_all_even_numbers = 0
for number in range(101):
    if number % 2 != 0:
        sum_of_all_odd_numbers += number
    else:
        sum_of_all_even_numbers += number

print(f'✅Sum of all odd numbers 0 to 100 is {sum_of_all_odd_numbers} \n✅Sum of all even numbers 0 to 100 is and {sum_of_all_even_numbers}')



# Exercises: Level 3
#1. Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

import sys
import os

# Add the path to the 'data' folder
sys.path.append(os.path.abspath('exercises/data'))
# Now import the countries list
from countries import countries
# Print countries containing 'land'
for country in countries:
    if 'land' in country:
        print(country)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reverse_fruit_list = []
for i in range(len(fruit_list) - 1, -1, -1):
    reverse_fruit_list.append(fruit_list[i])

print(reverse_fruit_list)
    
#3. Go to the data folder and use the countries_data.py file.
#i. What are the total number of languages in the data
#ii. Find the ten most spoken languages from the data
#iii. Find the 10 most populated countries in the world

# Full or relative path to the file
file_path = os.path.abspath('exercises/data/countries-data.py')

# Read the content and evaluate it as Python list
try:   
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        countries_data = eval(content)  # Safe here since you're reading your own data

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
    # Displaying the total number of unique languages in the data    
    print(f'✅The total number of unique languages in the data are: {len(languages_dict)}')

    # Displaying the ten most spoken languages in the data
    sorted_languages = dict(sorted(languages_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_languages)
    print(f'✅The ten most spoken languages are: {list(sorted_languages.keys())[:10]}')

    unique_languages = set()
    for country in countries_data:
        unique_languages.update(country['languages'])

    print("✅ Total number of unique languages:", len(unique_languages))
except FileNotFoundError:
    print(f"File not found: {file_path}")
    


    




