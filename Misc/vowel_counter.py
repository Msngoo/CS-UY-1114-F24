#For further context feel free to read Lab 10 question 3, Under Lab Instructions
def count_vowels(text):
    VOWELS = ["A", "E", "I", "O", "U"]

    vowel_counts = {}

    for char in text:
        if char.upper in VOWELS:
            if char.upper() not in vowel_counts:
                vowel_counts[char.upper()] += 0
            vowel_counts[char.upper()] += 1
        
    return vowel_counts