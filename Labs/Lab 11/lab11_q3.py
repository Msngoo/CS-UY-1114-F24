'''
def read_file(filename):
    try:
       with open(filename, "r") as inFile:
           return inFile.read()
    except FileNotFoundError:
        return {}


def count_vowels(filename):
    VOWELS = ["A", "E", "I", "O", "U"]

    contents = read_file(filename)
    if contents == {}:
        return contents 
    
    vowel_counts = {}

    for char in contents:
        if char.upper() in VOWELS:
            if char.upper() not in vowel_counts:
                vowel_counts[char.upper()] = 0
            vowel_counts[char.upper()] += 1

    return vowel_counts

def main():
    result = count_vowels("sample_text.txt")
    print(result)

main()
'''

def read_file(filename):
    try:
       with open(filename, "r") as inFile:
           return inFile.read()
    except FileNotFoundError:
        return {}


def count_vowels(filename):
    VOWELS = ["A", "E", "I", "O", "U"]

    contents = read_file(filename)
    if contents == {}:
        return contents 
    
    vowel_counts = {char.upper() : }

    for char in contents:
        if char.upper() in VOWELS:
            if char.upper() not in vowel_counts:
                vowel_counts[char.upper()] = 0
            vowel_counts[char.upper()] += 1

    return vowel_counts

def main():
    result = count_vowels("sample_text.txt")
    print(result)

main()