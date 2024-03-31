# Multiple inheritance in python
class employee:

    # parameterized constructor of class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"{self.name} is {self.age} years old")

class programmer():
    def __init__(self,language):
        self.language = language
    
    def show(self):
        print(f"Programmer knowns {self.language} programming language")


class Person(employee,programmer):
    def __init__(self, name, age,language):
        self.name = name
        self.age = age
        self.language = language


p1 = Person("Shahid",21,"Python")
p1.show() # First we inherite employee class so it will call employee class show method
print(Person.mro())