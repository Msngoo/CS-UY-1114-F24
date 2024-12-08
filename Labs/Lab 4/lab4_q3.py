toPrint = input("Enter a string to be printed (in the format [text]-[text]...) \n")
print("Printing:")
run = True
count = 0
length = len(toPrint)

while count < length:
    for i in toPrint:
        if i != "-":
            print(toPrint[count], end="")
            count += 1
        else:
            print()
            count += 1





#     for i in == "-" in toPrint:
#         for i in toPrint:
#             if i != "-":
#                 count += 1
#                 print(toPrint[:count])
#                 index = index(i)
#                 print(toPrint[:index])
# # toPrintfind("")
# for i in toPrint:
#    while i != "-":
       
