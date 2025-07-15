 #1. Filter only negative and zero in the list using list comprehension
def num_fileter():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    negatives_and_zero = [k for k in numbers if k<=0]
    print(negatives_and_zero)
#2. Flatten the following list of lists of lists to a one dimensional list :
def flatten_list():
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    flattend_lists = [inner1 for outer in list_of_lists for inner in outer for inner1 in inner]
    return flattend_lists

#3. Using list comprehension create the following list of tuples:
"""

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

"""
def create_tuples():
    list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
    return list_of_tuples


#4. Flatten the following list to a new list:
def flatten_list_of_tuples():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    """output:
    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
    """
    flattened_countries = [[count[0].upper(), count[0][:3].upper(), count[1].upper()] for country in countries for count in country]
    return flattened_countries

#5. Change the following list to a list of dictionaries:
def list_to_dictionary():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    """output:
        [{'country': 'FINLAND', 'city': 'HELSINKI'},
        {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
        {'country': 'NORWAY', 'city': 'OSLO'}]
    """
    countries_dict = [{'country': count[0], "city": count[1]} for country in countries for count in country]
    return countries_dict


#6. Change the following list of lists to a list of concatenated strings:
def lists_to_strings():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    """output
    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""
    list_of_strings = [name[0] + " " + name[1] for name_list in names for name in name_list]
    return list_of_strings

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_function = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)

if __name__ == "__main__":
    num_fileter()
    print(flatten_list())
    print(create_tuples())
    print(flatten_list_of_tuples())
    print(list_to_dictionary())
    print(lists_to_strings())

    print(f"The slope of linear equuation is {linear_function(3,6, 12,3)}")
 
