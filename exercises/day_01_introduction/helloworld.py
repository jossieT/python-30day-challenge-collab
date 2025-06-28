import sys
import math

# First day exersises

print("My current Python Version is :", sys.version)

print("Sum of 3 and 4 is :", 3 + 4) 
print("3 - 4 is :", 3 - 4) 
print("3 * 4 is :", 3 * 4)
print("3 % 4 is :", 3 % 4)
print("3 / 4 is :", 3 / 4)
print("3 ** 4 is :", 3 ** 4)
print("3 // 4 is :", 3 // 4)

# Print String

print("Yosef")
print("Teshome")
print("Ethiopia")
print("I am enjoying 30 Days of python challenge")

# Print types of the following

print(type(10))  # Integer
print(type(9.8))  # Float
print(type(3.14))  # Float
print(type(4 - 4j))  # Complex
print(type(['Yosef', 'Teshome']))  # List
print(type("Yosef"))  # String
print(type("Teshome"))  # String
print(type("Ethiopia"))  # String

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")