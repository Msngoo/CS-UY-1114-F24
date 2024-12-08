import random
random100 = random.randint(1, 100)
userAns = int(input("Guess a number 1 to 100: "))
Distance = abs(random100 - userAns)

print("Your Guess was", Distance,"away from the random number:", random100, "Did you guess correctly?", random100 == userAns)

