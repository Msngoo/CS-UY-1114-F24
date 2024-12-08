def squared_numbers(filename, outFile):
    with open(filename, 'r') as inFile:
        with open(outFile, 'w') as outFile:
            for line in inFile:
                num = int(line)
                squared = num ** 2
                outFile.write(str(squared) + "\n")

def main():
    squared_numbers("lab7_q2_ptA.txt", "lab7_q2_ptB_squared.txt")

main()
