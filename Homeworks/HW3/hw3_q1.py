"""
Author: Christian Auguste
Assignment / Part: HW#3 - Q1
Date due: October 3, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""

print("Welcome to the Lemonade Stand Profit Calculator!")
szn = input("Enter the current season (summer/other): ")
small = int(input("Enter the number of small cups of lemonade sold: "))
medium = int(input("Enter the number of medium cups of lemonade sold: "))
large = int(input("Enter the number of large cups of lemonade sold: "))

#Cost varibles for Cups during summer (from small to large)
sCost = 1.00
mCost = 1.25
lCost = 1.50

#Price variables for cups during summer (from small to large)
sPrice = 2.00
mPrice = 2.50
lPrice = 3.00

if szn == "summer":
    total = (small * (sPrice - sCost)) + (medium * (mPrice - mCost)) + (large * (lPrice - lCost))
    print("Total profit for the day in the summer : $",total, sep="")
else:
    total = (small * ((sPrice - 0.5) - (sCost -0.25))) + (medium * ((mPrice - 0.5) - (mCost -0.25))) + (large * ((lPrice - 0.5) - (lCost -0.25)))
    print("Total profit for the day in the rest of the year : $", total, sep="")

