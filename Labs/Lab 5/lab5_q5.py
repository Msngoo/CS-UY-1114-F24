# phrase = input("Enter a phrase: ")
# combined = ""
# split = phrase.split()

# for word in split:
#     if word.isdigit():
#         for chr in word:
#             digit = word.replace(word, "X")
#             combined += digit
#         combined += " "
#     else: 
#         combined += word + " "
# print(combined.strip()) 

# TA's Solution
text = input("enter a phrase")
output = ""
currentWord = ""

for char in text:
    if char != " ":
        currentWord += char
    else:
        if currentWord.isdigit():
            output += "X" * len(currentWord) + " "
        else:
            output += ""
        currentWord = " "

print(output)