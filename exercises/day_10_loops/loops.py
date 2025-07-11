from countries import countries
import json

#Exercises: Day 10
#Exercises: Level 1
#1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11): # using for
    print(i)

count = 0
while count < 11: # using while
    print(count)
    count += 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
counter = 10
while counter >= 0: #using while
    print(counter)
    counter -= 1

for i in range(10, -1, -1): #using for loop
    print(i)

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle
for i in range(7):
        print(i * '#')

#4. Use nested loops to create the following:
for i in range(8):
    print('\n')
    for n in range(8):
        print('#', end = ' ')

#5. Print the following pattern:
print() #new line
for i in range(11):
    print(f' {i} * {i} = {i * i}')

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language, end=',')

#7. Use for loop to iterate from 0 to 100 and print only even numbers
print() #new line
for number in range(101):
    if number % 2 == 0:
        print(number, end= ' ')
print() #new line
for number in range(101):
    if number % 2 != 0:
        print(number, end= ' ')

#Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total = total + i
print() #new line
print(f'The sum of all numbers is {total}')

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print() #new line
sum_even = 0
sum_odd = 0
for number in range(101):
    if number % 2 == 0:
      sum_even = sum_even + number
    else:
      sum_odd = sum_odd + number
print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.')

#Exercises: Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for name in countries:
    if 'land' in name:
        print(name)
#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
reversed_fruit = list()
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruit.append(fruits[i])
print(reversed_fruit)

#3. Go to the data folder and use the countries_data.json file.
#  Find the total number of languages in the data

with open('exercises/day_10_loops/countries_data.json', 'r', encoding='utf-8') as f:
    countries_data = json.load(f)

total_number_of_languages = 0
for country in countries_data:
    total_number_of_languages += len(country['languages'])

print('Total number of languages:', total_number_of_languages)

# Find the ten most spoken languages from the data using only for loop
most_spoken_languages = {}
for country in countries_data:
    for language in country['languages']:
        if language in most_spoken_languages:
            most_spoken_languages[language] += 1
        else:
            most_spoken_languages[language] = 1

language_counts = list(most_spoken_languages.items())
for i in range(len(language_counts)):
    for j in range(i + 1, len(language_counts)):
        if language_counts[j][1] > language_counts[i][1]:
            language_counts[i], language_counts[j] = language_counts[j], language_counts[i]
most_spoken_languages = language_counts[:10]
print('Most spoken languages:', most_spoken_languages)


# Find the 10 most populated countries in the world
most_populated_countries = {}
for country in countries_data:
    most_populated_countries[country['name']] = country['population']

population_counts = list(most_populated_countries.items())
for i in range(len(population_counts)):
    for j in range(i + 1, len(population_counts)):
        if population_counts[j][1] > population_counts[i][1]:
            population_counts[i], population_counts[j] = population_counts[j], population_counts[i]
most_populated_countries = population_counts[:10]
print('Most populated countries:', most_populated_countries)
