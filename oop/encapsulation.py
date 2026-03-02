# private properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def __validate(self,num):
        if not isinstance(num,(int,float)):
            return False
        return True
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if self.__validate(age):
            self.__age=age
        else:
            print("This is not a valid number")


p1 =Person("Rich",34)
print("Name : ",p1.name)
print("Age : ",p1.get_age())
p1.set_age(45)
print("Updated age: ",p1.get_age())