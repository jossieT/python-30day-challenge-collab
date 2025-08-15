#Exercises: Day 9
#Exercises: Level 1
#1. Get user input using input(“Enter your age: ”).
#If user is 18 or older, give feedback:
#You are old enough to drive. If below 18 give
#feedback to wait for the missing amount of years. Output:
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print('You are old enough to learn to drive.')
else:
    remaining_age = 18 - user_age
    print(f'You need {remaining_age} more years to learn to drive.')

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
#Use input(“Enter your age: ”) to get the age as input. You can use a nested condition
#to print 'year' for 1 year difference in age, 'years' for bigger differences, and a
#custom text if my_age = your_age. Output:
my_age = 27
your_age = int(input('Enter your age: ')) 
if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f'You are {difference} year younger than me')
    else:
        print (f'You are {difference} years younger than me')
elif my_age == your_age:
    print(f'we both are {your_age} years old')
else:
    difference = your_age - my_age
    if difference == 1:
        print(f'You are {difference} year older than me')
    else:
        print (f'You are {difference} years older than me')

#3. Get two numbers from the user using input prompt.
#If a is greater than b return a is greater than b,
#if a is less b return a is smaller than b, else a is equal to b. Output:
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))
if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')
elif number_one == number_two:
    print(f'{number_one} is equal to {number_two}')
else:
    print(f'{number_one} is less than {number_two}')

#Exercises: Level 2
#1. Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
student_score = float(input('Enter your score: '))
grade = ''
if student_score >= 80 and student_score <= 100:
    grade = 'A'
elif student_score >= 70 and student_score <= 79:
    grade = 'B'
elif student_score >= 60 and student_score <= 69:
    grade = 'C'
elif student_score >= 50 and student_score <= 59:
    grade = 'D'
elif student_score >= 0 and student_score <= 49:
    grade = 'F'
else:
    grade = 'Invalid because of bad Input'
print(f'Dear student your grade is {grade}')

#2. Check if the season is Autumn, Winter, Spring or Summer.
#If the user input is: September, October or November, the season is Autumn.
#December, January or February, the season is Winter. March, April or May,
#the season is Spring June, July or August, the season is Summer
seasons = {
    'Autumn': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August'],
    }
month = input('Please enter Month name: ')
if month in seasons['Autumn']:
    print(f'Month {month} is in Autumn season')
elif month in seasons['Winter']:
    print(f'Month {month} is in Winter season')
elif month in seasons['Spring']:
    print(f'Month {month} is in Spring season')
elif month in seasons['Summer']:
    print(f'Month {month} is in Summer season')
else :
     print(f'Invalid input {month} please correct enter again')

#3. The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the
#fruit to the list and print the modified list. If the fruit exists
#print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit you want to check or add to the list: ') 
if fruit in fruits:
    print (f'{fruit} already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

#Exercises: Level 3
#1. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#1.1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    index = len(person['skills']) // 2
    print(f"The middle skill is {person['skills'][index]}")
#1.2 Check if the person dictionary has skills key, if so check if the person
#has 'Python' skill and print out the result.
keys = person.keys()
skill_values = person['skills']
print(skill_values)
if 'skills' in keys:
   if 'Python in skill_values':
       print(f'has Python skill')
#1.3 If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills
#has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
#Print('He is a fullstack developer'), else print('unknown title')
# for more accurate results more conditions can be nested!
skills = person['skills']
skills_set = set(skills)
frontend_set = {'JavaScript', 'React'}
backend_set = {'Node', 'Python', 'MongoDB'}
fullstack_set = {'React', 'Nide','MongoDB'}

if skills_set == frontend_set:
    print('He is a front end developer')
elif backend_set.issubset(skills_set):
    print('He is a backend developer')
    if fullstack_set.issubset(skills_set):
        print('He is a fullstack developer')
else:
    print('Unknown title')
#1.4 If the person is married and if he lives in Finland, print the information in the following format:
#Asabeneh Yetayeh lives in Finland. He is married.
first_name = person['first_name']
last_name = person['last_name']
country = person['country']
married = ''
if person['is_marred']:
    married = 'is married'
else:
    married = 'is not married'
print(f'{first_name} {last_name} lives in {country}. He {married}')