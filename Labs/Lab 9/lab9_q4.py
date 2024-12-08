# lst =[(1, 2, 3), (5, 0, 9), (8, 1, 3, 2), (1, 8), (1, 1, 1, 1)]
# minSum = 0 
# maxSum = 0
# minIndex = 0
# maxIndex = 0
# for tup in lst:
#     tempSum = 0
#     for i in range(len(tup)): 
#         tempSum = sum(tup)
#         if i == 0:
#             minSum = tempSum
#             maxSum = tempSum
#             minIndex = i
#             maxIndex = i
#         else:
#             if tempSum <= minSum:
#                 minSum = tempSum
#                 minIndex = i
#             if tempSum >= maxSum:
#                 maxSum = tempSum
#                 maxIndex = i
# print("Smallest cluster is cluster", minIndex, "With a value of", minSum)
# print("Largest cluster is cluster", maxIndex, "With a value of", maxSum)

# V2
lst =[(1, 2, 3), (5, 0, 9), (8, 1, 3, 2), (1, 8), (1, 1, 1, 1)]
minSum = 10000 
maxSum = -10000
minIndex = 0
maxIndex = 0
index = 0 
for tup in lst: #Indexes each tuple in the list
    tempSum = sum(tup)
    if tempSum < minSum:
        minSum = tempSum
        minIndex = index
    if tempSum > maxSum:
        maxSum = tempSum
        maxIndex = index
    index += 1
print("Smallest cluster is cluster", minIndex, "With a value of", minSum)
print("Largest cluster is cluster", maxIndex, "With a value of", maxSum)
