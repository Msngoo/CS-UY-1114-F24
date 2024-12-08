width = int(input("Enter the width of the message: "))
for row in range(width):
    for column in range(width):        
        if row == column or row + column == width -1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

for row in range(width):
    for column in range(width):
        if row == 0 or column == width -1:
            if 
            print(" ", end="")
        else:
            print("O", end="")
        