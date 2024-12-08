"""
Author: Christian Auguste
Assignment / Part: HW#1 - Q2
Date due: September 26, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""
import math 

freq = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))
ampSpec = (2 * math.sin(freq*duration)) / freq

print("The amplitude spectrum of this Fourier transform is:", round(ampSpec, 3))
