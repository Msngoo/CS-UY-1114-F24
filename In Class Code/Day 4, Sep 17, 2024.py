import random
import math

length = random.uniform(2.5, 5.0)
width = random.uniform(0.1, 0.3)
height = random.uniform(0.1, 0.3)
appliedLoad = random.randint(1000, 5000)

momentOfInertia = (width * (height ** 3)) / 12
distanceFromNeutralAxis = height / 2
maxStress = (appliedLoad * distanceFromNeutralAxis) / momentOfInertia

yieldStrength = 200 * math.pow(10, 3) #Yield strengthof material in pascals

if (maxStress <= yieldStrength):
    print("safe")
else:
    print("fail")

print("length:", length, "width:", width, "height", height, "applied load:", appliedLoad, "max stress", maxStress, "yield strength", yieldStrength)