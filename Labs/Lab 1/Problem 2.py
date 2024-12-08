#These are the amount per the recipe in cups for 10 scones, divided to get the per scone amt
amtButter = (1/3)/10
amtFlour = (7/3)/10
amtMilk = (3/4)/10


amtScones = int(input("Enter how many scones you want: "))
print("To make", amtScones, "use", amtButter*amtScones, "cups of buttter,", amtFlour*amtScones, "cups flour", "and", amtMilk*amtScones, "cups milk." )