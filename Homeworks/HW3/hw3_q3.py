"""
Author: Christian Auguste
Assignment / Part: HW#3 - Q3
Date due: October 3, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
xp = float(input("Enter this user's current XP: "))

if 0<= xp < 15.0:
    print("Level 1 Player (XP: ", xp,")",sep="")
elif 15 <= xp <= 24.9:
    print("Level 2 Player (XP: ", xp,")",sep="")
elif 25 <= xp <= 29.9:
    print("Level 3 Player (XP: ", xp,")",sep="")
elif 30 <= xp <= 39.9:
    print("Level 4 Player (XP: ", xp,")",sep="")
elif 40 <= xp <= 60.0:
    print("Level 5 Player (XP: ", xp,")",sep="")
else:
    print("ERROR: Please enter a valid XP value")