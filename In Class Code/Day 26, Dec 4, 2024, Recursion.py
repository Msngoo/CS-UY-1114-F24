# def power(base, exponent):
#     if exponent == 1:
#         return base
#     elif exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent - 1)
    
# print(power(4, 1))
# print(power(4, 2))
# print(power(4, 3))

# #Count Vowels

# def count_vowels(str):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     length = len(str)
#     count = 0 
#     index = 0
#     if index < len - 1:
#         pass

# DePasquale's Solution

def count_vowels(data):
    data = data.lower()
    if len(data) == 0:
        return 0
    else:
        if data[0] in 'aeiou':
            return 1 + count_vowels(data[1:])
        else:
            return count_vowels(data[1:])

print(count_vowels(""))
print(count_vowels("XYZ"))
print(count_vowels("This is a test"))
