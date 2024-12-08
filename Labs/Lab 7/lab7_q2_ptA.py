def decreasing_numbers(filename, n):
    with open(filename, "w") as outFile:
        for i in range(n, 0,-1):
            outFile.write(str(i) + "\n")

def main():        
    decreasing_numbers("lab7_q2_ptA.txt", 5)

main()