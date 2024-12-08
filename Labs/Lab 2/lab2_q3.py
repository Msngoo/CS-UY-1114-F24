import random
randNum = random.randint(0,1)

guess = int(input("Will the coin land on 0 (heads) or 1 (Tails)? "))
print("Coin flip result:", randNum)
correctGuess = randNum ==  guess
print("User guessed correctly:", correctGuess)