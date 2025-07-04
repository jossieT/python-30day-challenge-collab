#Exercise Level 1
#1. Declare an empty list
my_list = []

#2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6]

#3. Find the length of your list
print(len(my_list))

#4. Get the first item, the middle item and the last item of the list
print(my_list[0])
print(my_list[len(my_list) // 2])
print(my_list[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John Doe', 30, 5.9, 'Single', '123 Main St']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[0] = 'Facebook Inc.'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Spotify')
print(it_companies)

it_companies = it_companies[2].upper()
print(it_companies)

#14. Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

#15. Check if a certain company exists in the it_companies list.
print('Google' in it_companies)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
print(it_companies[:3])

#19. Slice out the last 3 companies from the list
print(it_companies[-3:])

#20. Slice out the middle IT company or companies from the list
if len(it_companies) % 2 == 1:
    print(it_companies[len(it_companies) // 2])
else:
    print(it_companies[len(it_companies) // 2 - 1:len(it_companies) // 2 + 1])

#21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 1:
    it_companies.pop(len(it_companies) // 2)
else:
    it_companies = it_companies[:len(it_companies) // 2 - 1] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)

#23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

# Exercises: Level 2
#28. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
#. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
#. Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 1:
    median_age = ages[len(ages) // 2]
else:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
#. Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
#. Find the range of the ages (max minus min)
age_range = max_age - min_age
#. Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
#1. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
if len(countries) % 2 == 1:
    middle_country = countries[len(countries) // 2]
else:
    middle_country = countries[len(countries) // 2 - 1:len(countries) // 2 + 1]
#2. Divide the countries list into two equal lists if it is even or one middle country if it is odd.
if len(countries) % 2 == 1:
    first_half = countries[:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]
else:
    first_half = countries[:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
ch, ru, us, *scandic_countries = countries