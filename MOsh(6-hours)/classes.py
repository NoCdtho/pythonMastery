class Person:

    # constructor to create the new instance of this type
    def __init__(self, name, age):
        self.name = name
        self.age = age
    """In self.name is a instance variable or attribute created which can be accessed
        from anywhere in this file of this class. That is assigned to the 
        name(parameter) of init method/constructor of the class Person 
    """

    # ehh is just a parameter
    def talk(self):
        print(f"hello! my name is {self.name} and age is {self.age}")
        """ we can directly use current instances inside the method of the class.
            Here the self reference to current object which is person.
        """


person = Person("Rohit", 0)
person.talk()
