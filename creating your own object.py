# Advanced Python Object Oriente Programming (OOP)


class Dog:
    # Constructors method
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running")


dax = Dog("Dax")
deogee = Dog("DOG")
brian = Dog("Brian")


print(dax.name)
dax.run()
# instantiate is calling a class to create an object.
