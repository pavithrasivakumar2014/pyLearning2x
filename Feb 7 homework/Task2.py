# 1. Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2
# ( Take pie as 3.14)


import math
π = 3.14
Radius = float(input("Please enter the radius of the given circle: "))
area_of_the_circle = π * Radius * Radius
print(" The area of the given circle is: ", area_of_the_circle)


# 2. Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

a = 10
b = 25
print(a > b)
print(a < b)
print(a == b)


# 3. Develop a Python script that calculates the square and cube of a given number.

a =int(input("Enter the value of a:"))
square = a * a
cube = a * a * a
print(square, cube)

