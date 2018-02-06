class Cat(object):

    def __init__(self, name, age, fur_color):
        self.__name = name
        self.__age = age
        self.__fur_color = fur_color

    def meow(self):
        print("Meow!!!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return "Cat name: {0}, its age: {1} and its fur color: {2}".format(self.__name, self.__age, self.__fur_color)


tiger = Cat("tiger", 3, "black")
tiger.meow()
print(tiger.name)
tiger.name = "panther"
print(tiger.name)
print(tiger)
