# List Exercises – Day 5
# Level 1
# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'mango', 'grape', 'kiwi']
print('Fruits:', fruits)
print('-' * 40)

# 3. Find the length of your list
print('Number of fruits:', len(fruits))
print('-' * 40)

# 4. Get the first, middle, and last items
print('First fruit:', fruits[0]) # First item
print('Middle fruit:', fruits[len(fruits)//2]) # Middle item
print('Last fruit:', fruits[-1]) # Last item
print('-' * 40)

# 5. Declare a list called mixed_data_types
mixed_data_types = ['Yosef', 28, 1.75, 'Addis Ababa', True]
print('Mixed data types:', mixed_data_types)
print('-' * 40)

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('IT Companies:', it_companies)
print('-' * 40)

# 7. Print the list using print()
print(it_companies)
print('-' * 40)

# 8. Print the number of companies
print('Number of IT companies:', len(it_companies))
print('-' * 40)

# 9. Print the first, middle, and last company
print('First company:', it_companies[0])
print('Middle company:', it_companies[len(it_companies)//2])
print('Last company:', it_companies[-1])
print('-' * 40)

# 10. Modify one of the companies
it_companies[0] = 'Meta'
print('After modification:', it_companies)
print('-' * 40)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')
print('After appending:', it_companies)
print('-' * 40)

# 12. Insert an IT company in the middle
it_companies.insert(len(it_companies)//2, 'Twitter')
print('After inserting in the middle:', it_companies)
print('-' * 40)

# 13. Change one of the companies to uppercase
it_companies[1] = it_companies[1].upper()
print('After uppercase:', it_companies)
print('-' * 40)

# 14. Join the companies with a string '#'
print('Companies joined:', ' # '.join(it_companies))
print('-' * 40)

# 15. Check if a company exists
print('Is Google in the list?', 'Google' in it_companies) # prints True or False
print('-' * 40)

# 16. Sort the list
it_companies.sort()
print('Sorted companies:', it_companies)
print('-' * 40)

# 17. Reverse the list
it_companies.reverse()
print('Reversed companies:', it_companies)
print('-' * 40)

# 18. Slice out the first 3 companies
print('First 3 companies:', it_companies[:3])
print('-' * 40)

# 19. Slice out the last 3 companies
print('Last 3 companies:', it_companies[-3:])
print('-' * 40)

# 20. Slice out the middle company or companies
mid = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print('Middle companies:', it_companies[mid-1:mid+1])
else:
    print('Middle company:', it_companies[mid])
print('-' * 40)

# 21. Remove the first company
it_companies.pop(0)
print('After removing first:', it_companies)
print('-' * 40)

# 22. Remove the middle company
mid = len(it_companies)//2
it_companies.pop(mid)
print('After removing middle:', it_companies)
print('-' * 40)

# 23. Remove the last company
it_companies.pop()
print('After removing last:', it_companies)
print('-' * 40)

# 24. Remove all companies
it_companies.clear()
print('After clearing:', it_companies)
print('-' * 40)

# 25. Delete the list
del it_companies  # delete company


# 26. Join front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print('Full stack:', full_stack)
print('-' * 40)

# 27. Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print('Full stack after insert:', full_stack)
print('-' * 40)

# Level 2 Exercises

# 1. List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('Ages:', ages)
print('-' * 40)

# 2. Sort the list and find min and max age
ages.sort()
print('Sorted ages:', ages)
print('Min age:', min(ages))
print('Max age:', max(ages))
print('-' * 40)

# 3. Add min and max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print('Ages after adding min and max again:', ages)
print('-' * 40)

# 4. Find the median age
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]

print("Median age:", median)
print('-' * 40)

# 5. Find the average age
average = sum(ages) / len(ages)
print('Average age:', average)
print('-' * 40)

# 6. Find the range of the ages
age_range = max(ages) - min(ages)
print('Range of ages:', age_range)
print('-' * 40)

# 7. Compare (min - average) and (max - average)
min_diff = abs(min(ages) - average)
max_diff = abs(max(ages) - average)
print('Min - average:', min_diff)
print('Max - average:', max_diff)
print('-' * 40)

# 8. Find the middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
if len(countries) % 2 == 0:
    print('Middle countries:', countries[mid-1:mid+1])
else:
    print('Middle country:', countries[mid])
print('-' * 40)

# 9. Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid+1]
    second_half = countries[mid+1:]
print('First half:', first_half)
print('Second half:', second_half)
print('-' * 40)

# 10. Unpack the first three countries and the rest as scandic countries
china, russia, usa, *scandic = countries
print('China:', china)
print('Russia:', russia)
print('USA:', usa)
print('Scandic countries:', scandic)
print('-' * 40)
