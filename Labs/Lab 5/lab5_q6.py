# msg = input("Please enter your message: ")
# combined = ""
# split = msg.split()

# for word in split:
#     for chr in word:
#         for i in len(word):
#             if chr[0].isupper():
#                 count = 1
#                 if chr
#         if chr[0].isupper() != False:
 
#             combined += chr
# print("Your secret message is: ", combined.strip())

# msg = input("Please enter your message: ")
# length = len(msg)
# split = msg.split()

# for chr in msg:
#     for i in range(length)
#         if chr[0]
#     index = msg.find(" ")
#     if 

text = input("enter a phrase")
output = ""
currentWord = ""

for char in text:
    if char != " ":
        currentWord += char
    else:
        if currentWord == currentWord.capitalize():
            output += currentWord[0]
        currentWord = ""
print(output)