"""
Author: Christian Auguste
Assignment / Part: HW#3 - Q5
Date due: October 3, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
import math 
import random 
ball = random.randint(1,255)
hpMax = int(input("Enter the max health of this Pokémon: "))
currentHp = random.randint(1,hpMax)
rand = random.randint(0,255)

f = math.floor((hpMax*255*4)/(currentHp*ball))

if f > rand:
    print("You've caught the Pokémon")
else:
    print("Oh no! The Pokémon broke free!")