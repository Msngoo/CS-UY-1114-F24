def decode_part(message, start, end, step):
    decoded_msg = ""
    for ind in range(start, end, step):
        decoded_msg += message[ind]
    return decoded_msg

def decode_entire_msg(message):
    final_msg = ""
    total_letters = 0

    start = 1
    step = int(message[0])
    ind = 1
    while total_letters < 100 and ind < len(message):
        if message[ind].isdigit():
            decoded_msg = decode_part(message, start, ind, step)
            final_msg += decoded_msg
            start = ind + 1
            step = int(message[ind])
        elif message[ind].isalpha():
            total_letters += 1
        ind += 1
    return final_msg

def decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE):
    with open(ROMAN_FILE, 'r') as inFile:
        text = inFile.read()
    result = decode_entire_msg(text)
    with open(ROMAN_DECODED_FILE, 'w') as outFIle:
        outFIle.write(result)

def main():
    ROMAN_FILE = 'roman_code_msg.txt'
    ROMAN_DECODED_FILE = 'lab7_ q3_secret_msg.txt'
    decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE)
main()