class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name of Employee is: {self.name}")
        print(f"Age of that Employee is: {self.age}")

emp1 = Employee("Shahid",21)
emp1.show()
emp2 = Employee("Python",32)
emp2.show()