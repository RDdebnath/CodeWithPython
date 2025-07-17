class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")

class ToyotaCar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Fortuner", "petrol")
print(car1.type)

