# # Problem 1

# import random 
# num = random.randint(500, 1000)
# fileName = input("Enter the file name: ")

# with open(fileName, 'w') as outfile:
#     outfile.write(str(num) + '\n')

#     for line in range(num):
#         rand2 = random.randint(250, 1000)
#         outfile.write(str(rand2) + '\n')

# Problem 2
fileName = input("Enter the file name: ")

with open(fileName, 'r') as infile:
        line1 = infile.readline()
        numLines = int(line1)
        print(numLines)

        for lineNum in range(1, numLines + 1):
            if lineNum % 2 != 0:
                  line = infile.readline().strip()
                  print(line)
            else:
                line = infile.readline()