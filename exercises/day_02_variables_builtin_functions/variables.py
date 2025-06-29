#Day 02: 30 Days of python programming exercise
# Exercises: Level 1
first_name = "Johannes"
last_name = "Zewde"
full_name = "Johannes Zewde"
country = "Ethiopia"
city = "Addis Ababa"
age = 30
is_married = False
is_light_on = True
car_name,car_model,car_year = "Toyota", "Corolla", 2020

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_light_on))
print(type(car_name))
print(type(car_model))
print(type(car_year))

print(len(first_name))

if len(first_name) > len(last_name):
    print("First name is longer than last name")
else:
    print("Last name is longer than first name")


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

radius_in = input("Enter the radius of the circle: ")
radius_float = float(radius_in)
area = 3.14 * radius_float ** 2

user_name = input("Enter your name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print(help("keywords"))