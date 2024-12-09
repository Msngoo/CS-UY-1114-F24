def word_counter(text):
    words = text.split #creates a list of all the words; spliting the elements by the space character
    word_count = 0
    for word in words:
        if word.isalpha():
            word_count += 1
    return word_count