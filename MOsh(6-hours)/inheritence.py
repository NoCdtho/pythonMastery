class Mammals:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def walk(self):
        print(f"{self.name} is walking {self.mood}")


class Dog(Mammals):
    pass


class Cat(Mammals):
    pass


dog = Dog("floock", "mysteriously")
cat = Cat("gigi", "slick")

dog.walk()
cat.walk()

# Generating random values

