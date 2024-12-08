class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



def main():
    person1 = Person("Elijah", 18)
    person2 = Person("Rachelle", 18)

    print(person1)
    print(person2)



main()


# Changes made below:



# Can use init variable to establish default values for the object, once it is called
class Person:
    def __init__(self, personname, age=0):
        self.name = personname
        self.age = age
        self.eye_color = ""
        self.gender = "Female"
        self.ethnicity = ""
        self.status = "sitting"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and is also a {self.gender}"

    def set_gender(self, new_gender):
        self.gender = new_gender
    
    def get_gender(self):
        return self.gender
    
    def standup(self):
        if self.status == "sitting":
            self.status == "sitting"

#Can have a defaualt instance variable
def main():
    person1 = Person("Elijah", 18)
    person2 = Person("Rachelle")

    print(person1)
    print(person2)
    print()

    person1.set_gender("Male")

    print(person1)
    print(person2)

    print(person1.get_gender())

main()