'''Problem 1: Create a list of random numbers

Create a program that starts with a list of 100 numbers in the range from 1 to 100. They don't need to be random or sorted, 
but you are welcome to do so
'''

lst = [x for x in range(101)]
print(lst)
print()
data = [0 for val in range(1, 27)]
# print(data)

'''
    The following are examples of using list comprehension


import random

data = [round(random.uniform(0, 100.0), 1) for val in range(1, 27)]
print(data)

data = [f'{random.uniform(0, 100.0):.2f}' for val in range(1, 27)]
print(data)

data = [float(f'{random.uniform(0, 100.0):.2f}') for val in range(1, 27)]
print(data)
'''




'''
Problem 2: Remove even numbers
'''

def odd_nums(lst):
    new_lst = [num for num in lst if num % 2 == 1]
    return new_lst

print(odd_nums(lst))


'''
Problem 3: Find All Words <= 4
'''

long_string = 'On a summer day somner smith went swimming in the sun and his red skin stung'
def words_4_less(string):
    words = string.split()
    FourOrLess = [word for word in words if len(word) <= 4]

#DePasquale's Solution
# "On a summer day somner smith went swimming in the sun and his red skin stung"
def small_words(data):
    phrase = data.split()
    #return [word for word in phrase is len(word) < 5] 
    return { len(word) : word for word in phrase if len < 5}


user_str = input("Enter a string: ")
print(small_words(user_str))


#DePasquale Example
import random
data = [random.randint(0, 1000) for value in range(10000)]

print(len([value for value in data if value > 600]))
# Alternative: Makes a list of 1s and counts the amount over 600
print(len([1 for value in data if value > 600]))

'''
Problem 4: Only Word Numbers in String
'''
# In 1984 there were 13 instances of a protest with over 1000 people attending.

phrase = input("Enter a sentence: ")
seperated = phrase.split()


#DePasquale's SOlution
# On a summer day somner smith went swimming in the sun and his red skin stung
my_string_list = mystring.split() 
number_words = []

'''
Problem 4 (HARD!) String Manipulation with List Comprehension
'''
