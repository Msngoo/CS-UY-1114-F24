numVals = int(input("Please enter how many positive values you want to consider: "))
print("Enter your values: ")
firstVal = float(input(""))
greatest = 0
secondVal = float(input(""))
if firstVal >= secondVal:
    greatest = firstVal
else:
    greatest = secondVal

for i in range(numVals-2):
    val = float(input(""))
    if val >= greatest:
        greatest = val
print("The largest of these values is", greatest)