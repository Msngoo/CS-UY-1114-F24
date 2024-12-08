my_str = input("Enter a string:")
length = len(my_str)
print([my_str[x] for x in range(length)] * 2)