#Exercises - Day 3
import math

my_age = 27
my_height = 1.81
complex_number = 3 + 4j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base  = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle = ", area)


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
# Calculate the perimeter of the triangle
perimeter = a + b + c
print("The perimeter of the triangle = ", perimeter)

#Get length and width of a rectangle using prompt. Calculate its area
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area = length * width
print("The area of the rectangle = ", area)
perimeter = 2 * (length + width)
print("The perimeter of the rectangle = ", perimeter)

#Get radius of a circle using prompt. Calculate the area and circumference of the circle
radius = float(input("Enter radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle = ", area)
circumference = 2 * math.pi * radius
print("The circumference of the circle = ", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print("The slope is: ", slope)
print("The y-intercept is: ", y_intercept)
print("The x-intercept is: ", x_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("The slope between (2, 2) and (6, 10) is: ", slope)
euclidean_distance = math.hypot(x2 - x1, y2 - y1)
print("The Euclidean distance between (2, 2) and (6, 10) is: ", euclidean_distance)

#Compare the slopes in the above exercises
print("The slope of the line y = 2x - 2 is: ", slope)
print("The slope between points (2, 2) and (6, 10) is: ", slope)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = float(input("Enter a value for x: "))
y = x**2 + 6*x + 9
print("The value of y for x =", x, "is:", y)

print(len("python") != len("dragon"))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on is found in python and dragon", "on" in "python" and "on" in "dragon")

print("jargon" in "I hope this course is not full of jargon")

#there is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "python")

#Find the length of the text python and convert the value to float and convert it to string
txt_len = len("python")
float_text = float(txt_len)
print("length in float ", float_text, type(float_text));
string_len = str(float_text)
print("length in string ", string_len, type(string_len));

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = int(input("Enter number to be checked: "))

if number % 2 == 0:
    print(number, "is Even number")
else:
    print(number, "is Odd number")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print( 7//3  == int(2.7))

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int('9.8') is equal to 10
print(int('9.8') == 10) #This will raise an error because '9.8' cannot be directly converted to int

##Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * per_hour;
print("Your weekly earning is ", weekly_earning)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))
seconds_per_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_per_year
print("You can live for ", total_seconds, "seconds in", years, "years")


print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")



