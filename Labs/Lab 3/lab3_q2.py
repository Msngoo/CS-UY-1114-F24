rarity = input('Welcome to Pokemon card price calcultaor! \n Is your card of a special rarity? (Y/N)  ')
price = 5

if rarity == 'Y':
    uncommon = input("Is your card uncommons? (Y/N) ")
    if uncommon == "Y":
        price += 5
    else: 
        rare = input("Is your card rare? (Y/N) ")
        if rare == "Y":
            price += 15


holographic = input("Is your card holographic? (Y/N) ")
if holographic == "Y":
    revHolo = input("Is your card reverse holo? (Y/N) ")
    if revHolo == "Y":
        price += 10
    else:
        holo = input("Is your card a holo? (Y/N) ")
        if holo == "Y":
            price += 15
        else: 
            fullHolo = input("Is your card a full holo? (Y/N) ")
            if fullHolo == "Y": 
                price += 20
            else:
                price += 0


special = input("Is your card of a special pokemon? (Y/N) ")
if special == "Y":
    starter = input("Is your card of a starter? (Y/N) ")
    if starter == "Y":
        price += 5
    else:
        legendary = input("Is your card of a legendary? (Y/N) ")
        if legendary == "Y":
            price += 30

print("Your card has a final resale price of:", price)