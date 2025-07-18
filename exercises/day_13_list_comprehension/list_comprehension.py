# Exercises: Day 13
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
list_of_zeros_negative = [i for i in numbers if i <= 0]
print(list_of_zeros_negative)

#2. Flatten the following list of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = []
for i in range(len(list_of_lists)):
    for j in [0]:
        for k in range(len(list_of_lists)):
            flat_list.append(list_of_lists[i][j][k])

print(flat_list)

flattened_list_with_comp = [ number for row in list_of_lists for inner in row for number in inner]
print(flattened_list_with_comp)

#3. Using list comprehension create the following list of tuples:

'''[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)] '''

list_of_tuples = [(i, 1, i * i, i * i * i, i * i * i * i, i*i*i*i*i, i*i*i*i*i*i) for i in range(10)]
print(list_of_tuples)

#4. Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

'''output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]'''

flat_list = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for outer in countries
    for (country, capital) in outer
]
print(flat_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#5. Change the following list to a list of dictionaries:
'''output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]'''

list_of_dict = [
    {'country': country.upper(), 'city': capital.upper()}
    for outer in countries
    for(country, capital) in outer
]



#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

'''output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']'''

conc_strings = [
    firstname + ' ' + lastname
    for outer in names
    for(firstname, lastname) in outer
]

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x

x1, y1 = 2, 3
x2, y2 = 4, 7

m = slope(x1, y1, x2, y2)
b = y_intercept(x1, y1, m)

print("Slope:", m)
print("Y-Intercept:", b)