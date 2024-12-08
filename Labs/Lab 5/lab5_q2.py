# A
age = 20
name = "Oleg"

print(f"My Name is {name}, and I'm {age} years old.")
print("My Name is {}, and I'm {} years old.".format(name, age))
print()
# B
friday_steps = 2400
saturday_steps = 5630
sunday_steps = 1094
print(f"I walked a total of {friday_steps + saturday_steps + sunday_steps} steps this weekend!")
print("I walked a total of {} steps this weekend!".format(friday_steps + saturday_steps + sunday_steps))
print()

# C
exam1 = 65
exam2 = 85
final = 80
print(f"I averaged a {(exam1 + exam2 + final)/3} across all my exams!")
print("I averaged a {} across all my exams!".format((exam1 + exam2 + final)/3))
print()

# D
Wk1_temp = 81
wk2_temp = 75
print(f"Last week it was {Wk1_temp} degrees, and this week it's {wk2_temp} degrees.")
print(f"That's a {Wk1_temp - wk2_temp} degree difference!")
print("Last week it was {} degrees, and this week it's {} degrees.".format(Wk1_temp, wk2_temp))
print("That's a {} degree difference!".format(Wk1_temp - wk2_temp))