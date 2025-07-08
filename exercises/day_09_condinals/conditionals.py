# Exercise: Level 1
#1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
"""Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""
age = int(input("Enter your age:"))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f'You need {18-age} more years to learn to drive.')
#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age.
"""Output:
Enter your age: 30
You are 5 years older than me."""
my_age = 28
your_age = int(input("Enter your age:"))
if your_age > my_age:
    print(f'You are {your_age-my_age} years older than me.')
elif your_age < my_age:
    print(f'You are {my_age - your_age} years younger than me.')
else:
    print("We're age-mates.")
#3. Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
"""Output
Enter number one: 4
Enter number two: 3
4 is greater than 3"""
a = int(input("Enter first number:"))
b = int(input("Enter the second number:"))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less {b}")
else:
    print(f"{a} is equal to {b}")
# Exercise: Level 2
#1. Write a code which gives grade to students according to theirs scores:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
score = int(input("Enter your score between 0-100:"))
if 80<=score<=100:
    print("A")
elif 70<=score<=89:
    print("B")
elif 60<=score<=69:
    print("C")
elif 50<=score<=59:
    print("D")
elif 0<=score<=49:
    print("F")
else:
    print("You entered incorrect score.")

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
# September, October or November, the season is Autumn. December, January or February, the season is Winter.
#  March, April or May, the season is Spring June, July or August, the season is Summer
month_input = input("Enter a month that you want to know its season:")
season_dict = {'Autumn':['September', 'October', 'November'],
               'Winter':['December', 'January', 'February'],
               'Spring': ['March', 'April', 'May'],
               'Summer':['June', 'July', 'August']
               }

if month_input in season_dict['Autumn']:
    print(f"The {month_input} you entered belongs to Autumn")
elif month_input in season_dict['Winter']:
    print(f"The {month_input} you entered belongs to Winter")
elif month_input in season_dict['Spring']:
    print(f"The {month_input} you entered belongs to Spring")
elif month_input in season_dict['Summer']:
    print(f"The {month_input} you entered belongs to Summer")
else:
    print("Incorrect input.")

#3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
""""
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')"""
user_fruit = input("Enter a fruit:")
if user_fruit in fruits:
    print(f'fruit {user_fruit} already exist in the list')
else:
    fruits.append(user_fruit)
    print(fruits)
# Exercises: Level 3
#1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
""" 
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
 """
if 'skills' in person and isinstance(person["skills"], list) and person["skills"]:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(middle_skill)
    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    if 'Node' and 'Python' and 'MongoDB' in skills:
        print('He is a backend developer')
    if 'React'and 'Node'and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

    if person.get('is_married') and person.get('country') == 'Finland':
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

