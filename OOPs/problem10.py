class Circle:
    def __init__(self, redius):
        self.redius = redius 

    def area(self):
        return (22/7) * self.redius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.redius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())