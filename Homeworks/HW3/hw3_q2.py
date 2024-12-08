"""
Author: Christian Auguste
Assignment / Part: HW#3 - Q2
Date due: October 3, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""

day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))
total = 0

if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr":
    if 530 <= time <= 2100:
        total += (0.55 * duration)
    else:
        total += (0.35 * duration)
else:
    total += (0.1 * duration)
print("This call will cost $", end="")
print(round(total,1))