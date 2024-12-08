mLib = input("Input the mad lib text: ")
if mLib.find("V") != -1:
    verb = input("What's your verb?  ")
    mLib = mLib.replace("V", verb)
if mLib.find("N") != -1:
    noun = input("What's your noun?  ")
    mLib = mLib.replace("N", noun)
if mLib.find("U") != -1:
    num = input("What's your number? ")
    mLib.replace("U", num)
if mLib.find("A") != -1:
    adj = input("What's your adjective? ")
    mLib = mLib.replace("A", adj)

print()
print("Creating mad lib...")
print(mLib)