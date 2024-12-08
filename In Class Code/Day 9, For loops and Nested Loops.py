'''
for line in range(10):
	for asterisk in range(line + 1):
		print('*', end="")
	print()


for i in range(5): 
	for j in range(4)	
        print((i)*'.', end= '' )
'''

#Problem 2
for row in range(1,6):
    print(row, end="\t")
    for col in range(1,6):
        print(row * col, end="\t")
    print()

#Problem 3
'''
for row in range(1,10):
    for col in range(row + 1)
        print(firstNum + 1)
    
    print(" * 8 +", row, "=")
    for j in range(10):
        printj("1 * 8 +", j+1)
'''

#Depesquale's Code Problem 3
for row in range(1,10):

    for col in range(1, row+1):
        print(col, end="")
    print(" * 8 +", row, "=")
    for col in range(9, 9-row, -1):
        print(col, end="")
    print()

#Problem 4

