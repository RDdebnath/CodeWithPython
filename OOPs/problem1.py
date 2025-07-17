class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your Avg Score is: ", sum/3)


s1 = Student("RD", [87, 90, 88])
s1.get_avg()