word = input("Please enter a message to numberify: ")

def numberify(word):
    uppCase = word.upper()
    for i in range(len(uppCase)):
        if uppCase[i] == "A":
            uppCase = uppCase.replace("A", "4")
        if uppCase[i] == "E":
            uppCase = uppCase.replace("E", "3")
        if uppCase[i] == "I":
            uppCase = uppCase.replace("I", "1")
        if uppCase[i] == "S":
            uppCase = uppCase.replace("S", "5")
        if uppCase[i] == "T":
            uppCase = uppCase.replace("T", "7")
        if uppCase[i] == "O":
            uppCase = uppCase.replace("O", "0")
    return uppCase

def main():
    result = numberify(word)
    print("Your numberified string is:", result)

main()