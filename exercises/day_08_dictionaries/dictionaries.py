#1. Create an empty dictionary called dog
dct = {}
#2. Add name, color, breed, legs, age to the dog dictionary
dct = {'name': 'John', 'color':'red', 'breed':'sheep', 'age': 23}
#3.Create a student dictionary and add first_name, last_name, gender, 
# age, marital status, skills, country, city and address as keys for the dictionary
student = {'first':'John', 'last_name':'Zekarias', 'gender':'male', 'age':24, 'martial': 'single', 'skills': ['Python', 'C++', 'HTML', 'CSS', 'IoT', 'Raspberry Pi'], 'country': 'Ethiopia', 'city':'Addis Ababa', 'address': 'King George VI Street'}
#4. Get the length of the student dictionary
print(len(student))
#5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
#6. Modify the skills values by adding one or two skills
student['skills'].extend(['JavaScript', 'Java'])
print(student)
#7. Get the dictionary keys as a list
keys = student.keys()
print(keys)
#8. Get the dictionary values as a list
values = student.values()
print(values)
#9.Change the dictionary to a list of tuples using items() method
dictionary_list = student.items()
#10. Delete one of the items in the dictionary
del student['age']
#11. Delete one of the dictionaries
del dct