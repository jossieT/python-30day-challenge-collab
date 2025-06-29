# Day 2: 30 Days of python programming
# Exercises: Level 1
first_name = "Jossy"
last_name = "Teshome"
Full_name = first_name + " " + last_name
country = "Ethiopia"
city = "Addis Ababa"
age = 30
year = 2023
is_married = False
is_true = True
is_light_on = False

first_name, last_name, Full_name, country, city, age, year, is_married, is_true, is_light_on = "Jossy", "Teshome", "Jossy Teshome", "Ethiopia", "Addis Ababa", 30, 2023, False, True, False
# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print("Variables:", type(first_name), type(last_name), type(Full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on))
len_first = len(first_name) # Find the length of your first name
len_last = len(last_name) # Find the length of your last name
print(len_first == len_last) # Compare the length of your first name and your last name
num_one, num_two = 5, 4 # Declare two variables num_one and num_two
total = num_one + num_two # Add num_one and num_two and assign the result to a variable total
diff = num_one-num_two # Subtract num_two from num_one and assign the result to a variable diff
product = num_one * num_two # Multiply num_one and num_two and assign the result to a variable product
division = num_one / num_two # Divide num_one by num_two and assign the result to a variable division
remainder = num_two%num_one # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp = num_one**num_two # Calculate num_one to the power of num_two and assign the value to a variable exp
floor_division = num_one // num_two # Use floor division to find num_one divided by num_two and assign the value to a variable floor_division
radius = 30
pi = 3.14
area_of_circle = pi*radius**2
circum_of_cir = 2*pi*radius
radius_input = input("Enter the radius of the circle.")
area_of_circle_new = pi*float(radius_input)**2
first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ")
age_input = input("Enter your age: ")
country_input = input("Enter your country: ")