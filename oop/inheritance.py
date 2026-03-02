class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printName(self):
        print(f"{self.fname} {self.lname}")

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationYear = year
    def __str__(self):
        return f"Hello, {self.fname} {self.lname} graduated in the year {self.graduationYear}"

student = Student("John","Doe",2024)
print(student)