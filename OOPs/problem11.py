class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("sal =", self.sal)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "60000")

engg1 = Engineer("Rakesh Debnath", 26)
engg1.showDetails()