class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)

stu1 = Student(90, 88, 85)
print(stu1.percentage)

stu1.math = 92
print(stu1.percentage)
