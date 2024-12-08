# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a second number: "))
# num3 = float(input("Enter a third number: "))

# if num1 >= num2 and  num3 <= num1: 
#     print(num1, "is the largest.")
# elif num2 >= num1 and  num3 <= num2:
#     print(num2, "is the largest.")
# else: 
#     print(num3, "is the largest.")


# if num1 >= num2:
#     if num3 <= num1:
#         print(num1, "is the largest.")

# elif num2 >= num1:
#         if num3 <= num2:
#             print(num2, "is the largest.")
# else:
#     print(num3, "is the largest.")

citizenship = input("Are you a citizen? Enter Y or N ")

if citizenship == "Y":
    validAge = input("Are you 18 years or older? Enter Y or N ")
    if validAge == "Y":
        isRegistered = input("Are you registered to vote? Enter Y or N ")
        if isRegistered == "Y":
            print("You are able to vote.")
        else: 
            print("You are unable to vote because you aren't registered.")
    else:
        print("You are unable to vote because you aren't old enough.")
else:            
    print("You are unable to vote because you are not a citizen.")
    
    
painExtrem = input("Do you have pain in extremities? Y or N ")

if painExtrem == "Y":
    painArm = input("Do you have pain in your arms? Y or N ")