#Exercises: Day 8
#1. Create an empty dictionary called dog
dog = {}
dog_one = dict()

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'], dog['color'], dog['breed'], dog['age']  = 'Jackie', 'black', 'germany', 5
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country,
#city and address as keys for the dictionary
student = {
    'first_name': 'Yisak',
    'last_name': 'Abebe',
    'gender': 'Male',
    'age': 26,
    'maritial status': 'Single',
    'skills': ['nodejs', 'python', 'C++', 'Java'],
    'country': 'Ethioia',
    'city': 'Addis Ababa',
    'Adress': {
        'street': 'yeka kotebe, 202',
        'zipcode': 1001
        }
    }
print(student)

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

#6. Modify the skills values by adding one or two skills
student['skills'].extend(['DevOps', 'Linux'])
print(student['skills'])

#7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

#8. Get the dictionary values as a list
values = student.values()
print(values)

#9. Change the dictionary to a list of tuples using items() method
student_list = list(student.items())
print(student_list)

#10. Delete one of the items in the dictionary
student.pop('city')
print(student)

#11. Delete one of the dictionaries
del dog


