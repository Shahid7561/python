# Single inheritance in python
class employee:

    # parameterized constructor of class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"{self.name} is {self.age} years old")

class programmer(employee):
    def __init__(self, name, age,language):
        super().__init__(name, age)
        self.language = language
    
    def show(self):
        print(f"{self.name} is {self.age} years old and he knows {self.language} programming language")

# creating object of class emplyee

emp1 = employee("Shahid",21)
emp1.show() #Printing values of employee class object 

prog1 = programmer("Shahid",21,"Python")
prog1.show() #Printing values of programmer class object 