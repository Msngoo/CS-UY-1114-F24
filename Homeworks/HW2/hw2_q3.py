"""
Author: Christian Auguste
Assignment / Part: HW#2 - Q3
Date due: September 26, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
import math 
import random 

rand = random.randint(1,20)
sqrtRand = round(math.sqrt(rand), 2)
areaCircle = round((sqrtRand**2)*(math.pi),2)

print("Random integer(1-20):", rand)
print("Square root of ", rand, "is:", sqrtRand)
print("Area of a circle with radius", sqrtRand, "is:", areaCircle)
