class car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")

class ToyotaCar(car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortunar")
car2 = ToyotaCar("prius")

print(car1.color)
print(car1.start())