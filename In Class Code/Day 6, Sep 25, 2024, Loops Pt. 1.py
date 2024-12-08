'''
Problem 1
'''

# start_val = 100
# val2 = 8
# num  = 5


# while num < 50:
#     print(start_val - num, ":", val2 % 3)
#     num += 5
#     val2 += 5
    
'''
Problem 2
'''

char = '*'
counter = 0

while counter < 9:
    if counter == 0 or counter == 3 or counter == 5 or counter == 8:
        print(char*3)
    elif counter == 1 or counter == 4 or counter == 6:
        print(char, char, char)
    else:
        print(char)
    counter += 1

'''
Problem 3
'''

