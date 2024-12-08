import random

sepVal = 9
octVal = 10
novVal = 11
decVal = 12


monthRange = random.randint(9, 12)
dayRange = random.randrange(3, 31, 3)


print("Hello! Welcome to the Doctor's office!")
if monthRange == 9: 
    selectedMonth = "September"
elif monthRange == 10:
    selectedMonth = "October"
elif monthRange == 11:
    selectedMonth = "November"
else:
    selectedMonth = "December"

print("Your appointmnent is on", selectedMonth, dayRange, end= "!" )
print(" Have a great day!")
