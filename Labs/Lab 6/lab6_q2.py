def numberify(word):
    upperCase = word.upper()
    if len(upperCase) > 3:
        for i in range(len(upperCase)):
            if upperCase[i] == "A":
                upperCase[i] = '4'
            elif upperCase[i] == "E":
                upperCase[i] = '3'
            elif upperCase[i] == 'I':
                upperCase[i] = '1'
            elif upperCase[i] == 'S':
                upperCase[i] = '5'
            elif upperCase[i] == 'T':
                upperCase[i] = '7'
            elif upperCase[i] == 'O':
                upperCase[i] = '0'
    return 