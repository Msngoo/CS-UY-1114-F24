import random

def get_item():
    fusion_components = ["cat", 5, 4, "fish", 7, 9, "dog"]
    rand_1 = fusion_components[random.randint(0, 6)]
    rand_2 = fusion_components[random.randint(0, 6)]
    return rand_1,rand_2

def fuse():
    # rand_1, rand_2 = get_item()
    # status = input("Hit enter to continue and Q to quit perfoming fusion: ")
    # if status == "":
    #     statusBool = True
    # else:
    #     statusBool = False
    statusBool = True
    status = ""
    while status != "Q":
        rand_1, rand_2 = get_item()
        status = input("Hit enter to continue and Q to quit perfoming fusion: ")
        if status == "":
            statusBool = True
        else:
            statusBool = False
            continue

        operation = input("Enter the fusion operation (+, *): ")
        while operation != "+" and operation != "*":
            print("Invalid Operation. Try again")
            operation = input("Enter the fusion operation (+, *): ")

        if operation == '+':
            result = rand_1 + rand_2 
            print("The result of addition with", rand_1, "and", rand_2, "is:", result)
        else:
            result = rand_1 * rand_2
            print("The result of multiplication with", rand_1, "and", rand_2, "is:", result)
    
def main():
    try:
        fuse()
    except TypeError:
        print("Fusing those two will produce an error! Try another combination")
        fuse()

main()






'''
import random

def get_item():
    fusion_components = ["cat", 5, 4, "fish", 7, 9, "dog"]
    rand_1 = fusion_components[random.randint(0, 6)]
    rand_2 = fusion_components[random.randint(0, 6)]
    return rand_1, rand_2

def fuse():
    status = ""
    while status != "Q":
        rand_1, rand_2 = get_item()
        status = input("Hit enter to continue and Q to quit performing fusion: ")
        continue
        if status == "Q":
            continue
        else:
            operation = input("Enter the fusion operation (+, *): ")
            while operation != "+" and operation != "*":
                print("Invalid Operation. Try again")
                operation = input("Enter the fusion operation (+, *): ")

            try:
                if operation == '+':
                    result = rand_1 + rand_2
                    print("The result of addition with", rand_1, "and", rand_2, "is:", result)
                else:
                    result = rand_1 * rand_2
                    print("The result of multiplication with", rand_1, "and", rand_2, "is:", result)
            except TypeError:
                print("Fusing those two will produce an error! Try another combination.")

def main():
    fuse()

main()
'''
