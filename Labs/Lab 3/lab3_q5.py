import random

print("Welcome to Blackjack!")

dealerSum = random.randint(2,21)
plrSum = random.randint(1,11)
randCard = random.randint(1,11)
gameRun = True


print("Your current card sum is:", plrSum)
while gameRun:
    plrAction = input("What would you like to do next?: (DEAL, STAND) ")
    if plrAction == "DEAL":
        plrSum += randCard
        print("Your current card sum is:", plrSum)
        if plrSum > 21:
            print("You lost! Your card sum was", plrSum, "and the dealer's was", dealerSum)
            gameRun = False
    else:
        if plrAction == "STAND":
            if plrSum == dealerSum:
                print("You tied! Your card sum was the same as the dealer.")
                gameRun = False
            else:
                if (21 - plrSum) < (21- dealerSum):
                    print("You won! Your card sum was", plrSum, "and the dealer's was", dealerSum)
                    gameRun = False