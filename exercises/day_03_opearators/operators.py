# Age declaration as an integer
age = int(input("Enter your age:"))
# Height declaration as a float
height = float(input("Enter your height:"))
# Complex number declaration
complex_number = complex(input("Enter a complex number (e.g., 1+2j): "))
# Inputing Accepting base of the triangle
base_of_triangle = input("Enter the base of the triangle: ")
# Inputing height of the triangle
height_of_triangle = input("Enter the height of the triangle: ")
# Calculating area of the triangle
area_of_triangle = 0.5 * float(base_of_triangle) * float(height_of_triangle)
print("The area of the triangle is:", area_of_triangle)
# Inputing three sides of a triangle
side_a_of_triangle = input("Enter the ide a of triangle:")
side_b_of_triangle = input("Enter the side of triangle:")
side_c_of_triangle = input("Enter the side c of triangle:")
# Calculating perimeter of a triangle
perimeter_of_triangle = float(side_a_of_triangle)+float(side_b_of_triangle)+float(side_c_of_triangle)
print(f"The perimeter of the given triangle is {perimeter_of_triangle}")
# Getting length and width of a reactangle
length = input("Enter the length of a reactangle:")
width = input("Enter the width of a reactangle:")
# Calculating Area of a Reactangle
area_reactangle = float(length)*float(width)
# Calculating Perimeter of a Reactangle
perimeter_reactangle = 4*float(length)*float(width)

# Getting the radius of a circle to calculate its  area and perimeter
radius = input("Enter radius of the circle:")
PI = 3.14
area_circle = PI*float(radius)**2
cercumference = 2*PI*float(radius)
"""Calculate the slope, x-intercept and y-intercept of y = 2x -2
    This equation is in the form of y = mx+b where m = 2 and b = -2"""
# slope 
slope = 2
# y intercept is point where the given line crosses y-axis
y_intercept = -2
# x intercept is a point where the given line crosses x-axis
x_intercept = -y_intercept/slope 
print(f"slope: {slope}, x intercept: {x_intercept}, y intercept: {y_intercept}")
# Given given points in the x,y coordinate
p1 = (2, 2)
p2 = (6, 10)
# slope of a line that passes through these points
slope1 = (p2[1]-p1[1])/(p2[0]-p1[0])
# The euclidean distance between two points
euclidian_distance = ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

if slope == slope1:
    print("The two slopes are equal.")
else:
    print("The slopes are different.")

"""Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is going to be 0.
This equation is in the form of y = ax^2 + bx + c
"""
# To find the zero of y we use (-b+-(b^2-4ac)**2)/2a
x1 = (-6+(6**2-4*1*9)**0.5)/2*1
x2 = (-6-(6**2-4*1*9)**0.5)/2*1
zero_of_y = [x1, x2]
y_1 = zero_of_y[0]**2 + 6*zero_of_y[0] + 9
y_2 = zero_of_y[1]**2 + 6*zero_of_y[1] + 9
if y_1 == y_2 == 0:
    print(f"{x1} and {x2} are the zeros of y.")
elif y_1 == 0 and y_2 != 0:
    print(f"{x1} is zero of y but {x2} is not.")
elif y_2 == 0 and y_1!=0:
    print(f"{x2} is the zero of y but {x1} is not.")
else:
    print(f"{x1} and {x2} are not zero's of y.")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len("python") < len("dragon"):
    print(True)
else:
    print(False)
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "dragon":
    print(True)
else:
    print(False)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if "jargon" in "I hope this course is not full of jargon.":
    print(True)
else:
    print(False)

# There is no 'on' in both dragon and python

print('on' in 'dragon' and 'on' in 'python')

# Find the length of the text python and convert the value to float and convert it to string
text_length = len("python")
text_length_float = float(text_length)
text_length_str = str(text_length_float)
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = float(input("Enter a number:"))
if num/2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if 7//3 == int(2.7):
    print(True)

else:
    print(False)

# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print(True)
else:
    print(False)

# Check if int('9.8') is equal to 10
if int(float('9.8')) == 10:
    print(True)
else:
    print(False)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
number_of_hours = input("Enter the number of hours you worked per week:")
rate_per_hour = input("Enter the rate per hour you will get paid:")
pay = float(number_of_hours) * float(rate_per_hour)

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = input("Enter the number of years you have lived:")
seconds_in_a_year = 365 * 24 * 60 * 60
age_in_seconds = float(number_of_years) * seconds_in_a_year
print(f"You have lived for {age_in_seconds} seconds.")


# Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)

# This code is for advanced table using nested loop
"""for i in range(1, 6):
    print(i, end= "\t")
    for j in range(0,4):
        print(i**j, end="\t")
    print()"""
