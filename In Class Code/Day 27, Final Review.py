'''
class Cake:
    def __init__(self, flavor, size, color):
        self.flavor = flavor
        self.size = size
        self.color = color
    
    def __str__(self):
        return f"This is a cake that is: {self.size} inches and is {self.flavor}"
    # Priority is human readable and usually provides information about the data of the object
    
    def __repr__(self): #The goal is to a return a string that looks like a call to the object constructor
        return f'Cake("{self.flavor}", {self.size}, "{self.color}")'


def main():
    c1 = Cake('chocolate', 10, "white")
    print(c1) #Bc theres a string method it will print the string returned by __str__
    print(c1.__str__())

    print()
    print(c1.__repr__())
    print(repr(c1))
    c2 = eval(c1.__repr__())
    print(c2)
main()
'''
class Cake:
    def __init__(self, flavor, size, color, cupcake=None):
        self.flavor = flavor
        self.size = size
        self.color = color
        self.cupcake = cupcake

    def setCupcake(self, cc):
        self.cupcake = cc
    
    def __str__(self):
        return f"This is a cake that is: {self.size} inches and is {self.flavor}" + \
        f' and has {self.cupcake} in it.'
    # Priority is human readable and usually provides information about the data of the object
    
    def __repr__(self): #The goal is to a return a string that looks like a call to the object constructor
        return f'Cake("{self.flavor}", {self.size}, "{self.color}")'
class Cupcake:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'

cake1 = Cake("Peach", 12, "orange")
cup1 = Cupcake("Mike")
cake1.setCupcake(cup1) #Puts cupcake inside of cake
print(cake1)