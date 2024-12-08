"""
Author: Christian Auguste
Assignment / Part: HW#3 - Q4
Date due: October 3, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
import math

a = float(input("Please enter the value of a: "))
b = float(input("Please enter the value of b: "))
c = float(input("Please enter the value of c: "))

discriminant = ((b**2) - 4*a*c)

if a == 0 and b == 0 and c == 0:
    numSolutions = "infinite"
elif discriminant < 0:
    numSolutions = 0
elif discriminant == 0:
    numSolutions = 1
else: 
    numSolutions = 2

if numSolutions == 0:
    print("This equation has no Solution")
elif numSolutions == 1:
    x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
    print("This equation has 1 solution: x =", x1)
elif numSolutions == 2:
    x1 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    print("This equation has 2 solutions: x =", x1, "and x =", x2)
else:
    print("This equation has infinite solution")

