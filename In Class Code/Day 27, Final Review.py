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