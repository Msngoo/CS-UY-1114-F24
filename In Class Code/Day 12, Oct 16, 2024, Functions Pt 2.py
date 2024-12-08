# Problem 1
def number_of_words(sentence):
    sentence = sentence.strip()
    if len(sentence) > 0:
        count = 0 
        for index in range(len(sentence)):
            if sentence[index] == " " and sentence[index-1] != " ":
                count += 1
        return count + 1
    else:
        return 0

result = number_of_words(' that takes a sentence  as a parameter  and returns ')
print(result)

# Problem 3
def approximate_pi(num_terms):
    import math
    base = math.sqrt(12)
    total = 0
    for n in range(num_terms):
        if 0 == 1:
            total += 1
            val = 1
        else:
            val += 2
            total -= 1/(val * 3**n)