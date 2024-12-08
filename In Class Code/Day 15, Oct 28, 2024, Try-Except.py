# Problem 1: Writing a file
import random

def get_input():
    userInput = int(input("Enter a number between 500 and 1000 inclusive: "))
    if not(500<=userInput<= 1000):
        raise Exception("Value is not within range")
    else:
        return userInput

def get_file():
    fileName = input("Enter the name of the file which is 5 or more chars long (Be sure to include .txt): ")
    if len(fileName) < 5:
        raise Exception("FIle name is less than 5 characters")
    else:
        return fileName

def file_operations(fileName, userInput):
    outFile = open(fileName, 'w')
    outFile.write(userInput + "\n")
    for i in range(userInput - 1):
        outFile.write(str(random.randint(500, 1000)) + "\n")
    outFile.close()



def main():
    pass