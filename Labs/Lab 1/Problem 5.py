roman1 = "I"
roman5 = "V"
roman10 = "X"
roman50 = "L"

input = int(input("Enter a number: "))
numL = input // 50
input = input % 50
numX = input // 10
input = input % 10
numV = input // 5
input = input % 5
numI = input // 1

print("Output:", numL*roman50 + numX*roman10 + numV*roman5 + numI*roman1)