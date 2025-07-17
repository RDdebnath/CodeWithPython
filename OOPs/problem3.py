class Person:
    name = "RD"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

s1 = Person()

print(s1.welcome())