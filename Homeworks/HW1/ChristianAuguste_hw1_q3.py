"""
Author: Christian Auguste
Assignment / Part: HW - Q3
Date due: September 19, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""

print("Enter number of coins:")
numQuarters = int(input("Number of quarters: "))
numDimes = int(input("Number of dimes: "))
numNickels = int(input("Number of nickels: "))
numPennies = int(input("Number of pennies: "))
valQ = 0.25
valD = 0.1
valN = 0.05
valP = 0.01
total = valQ*numQuarters + valD*numDimes + valN*numNickels + valP*numPennies
totalDollars = int(total // 1)
totalCents = int(((total % 1) * 100) // 1)
print("The total is", totalDollars, "dollar(s) and", totalCents, "cent(s)")

