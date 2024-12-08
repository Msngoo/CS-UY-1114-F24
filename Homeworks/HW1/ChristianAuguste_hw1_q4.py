"""
Author: Christian Auguste
Assignment / Part: HW#1 - Q4
Date due: September 19, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""

amtDollars = int(input("Enter amount of dollars: "))
amtCents = int(input("Enter amount of cents: "))
print(amtDollars, "dollars and", amtCents, "cents are:")
total = amtDollars + (amtCents / 100)
amtQ = total // .25
total %= .25
amtD = total // .1
total %= .1
amtN = total // .05
total %= .05
amtP = total / .01
print(int(amtQ), "quarters,", int(amtD), "dimes,", int(amtN), "nickles and", int(amtP), "pennies")
