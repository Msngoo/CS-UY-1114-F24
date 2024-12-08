import random

def randNums():
    numbers = []
    counts = {}

    for i in range(1000):
        numbers.append(random.randint(1, 500))
    for num  in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    print(len(numbers))
    print("Counts of random numbers: ")


def main():
    randNums()

main()

# DePasquale Solution
import random
def main():
    counter_dictionary = {}
    # for value in range (1,501):
    #     counter_dictionary[value] = 0

    #Generate random number from 1 to 500, increment
    for rand_num in range(1, 1001):
        key = random.randint(1, 500):
        if key not in counter_dictionary:
            counter_dictionary[key] = 1
        else:
            counter_dictionary[key] += 1

    # for key in  

main()

# Problem 2
grades_list = [["Emily Kaldwin", "ek12345", 88, 90], ["Sakura Kinomoto", "sk12345", 98, 98], ["Maximilien Robespierre", "mr12345", 76, 89], ["Emily Kaldwin", "ek12345", 100, 100]]
def convert_grades_to_dictionary(grades_list):
    student_dict = {}
    for i in range(len(grades_list)):
        for name in lst:
            name = lst[0]
            student_vals = {}
            student_vals["NetId"] = name
            student["Name"] = nested[0]
            student["NetId"] = nested[1]
            student["Midterm"] = nested[2]
            student["Final"] = nested[3]