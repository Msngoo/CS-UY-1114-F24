# let = "NYU"
# let = let.lower()
# let.startswith("co")

#Problem 1
ans = input("Say Something: ")
changed = 0
numLetters = 0
space = 0
unchanged = 0
nonAlpha = 0

print()
print(ans.lower()) 
for chr in ans:
    if chr.isalpha():
        numLetters += 1
        if chr.isupper():
            changed += 1
    elif chr.isspace():
        space += 1
    elif not(chr.isalpha()):
        nonAlpha += 1
nonAlpha += space
print("Number of changed letters:", changed)
print("Number of unchanged letters:", (numLetters - changed))
print("Number of whitespace characters:", space)
print("Number of non-alphabetic characters:", nonAlpha)

