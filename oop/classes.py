class MyClass:
    x=5

x=MyClass.x
# print("x:",x)

class Student:
    school="Egerton" #class property
    def __init__(self,fname,lname,course,dob,cf=0):
        self.fname=fname #Instance property
        self.lname=lname
        self.course=course
        self.dob=dob
        self.cf=cf
    def __str__(self):
        return f"Hello, i am {self.fname} {self.lname} taking {self.course}"
    def greet(self):
        print("Hello, {}".format(self.fname))
    def getMarks(self):
        return self.cf*4

student = Student("Richard","Kinyua","Comp Sci","15-05-2001",67)

student.greet()
student.lname="lsat"
print(student.school)
print("Marks: ",student.getMarks())
print(student)