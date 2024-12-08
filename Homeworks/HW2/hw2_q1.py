"""
Author: Christian Auguste
Assignment / Part: HW#2 - Q1
Date due: September 26, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
import math 

numGuests = int(input("Enter the number of guests: "))
numSlices = int(input("Enter the number of pizza slices each person will eat: "))

slicesNeeded = numGuests * numSlices
numPiesNeeded = math.ceil((slicesNeeded /8))
slicesPerMin = numPiesNeeded*8

print("Minimum number of whole large pizzas required:", numPiesNeeded)
print("Total number of large pizza slices needed:", slicesNeeded)
print("Number of large pizza slices left over:", (slicesPerMin - slicesNeeded))
