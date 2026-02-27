def hello_world():
    print("Hello world")

def greetings(name):
    return f"Good afternoon {name}"

def theme(selected="light"):
    return f"Your theme is {selected}"

def fontSize(size,/):
    print(f"the preferred font size is {size}")

def accentColor(*,color):
    print(f"The preferred color is {color}")

def profile(name,age,/,*,bio,location):
    print(f"Hello i am {name} and i am {age} years old. \nI am from {location}\n\t {"Bio".center(5)} \n {bio}")

name="Richard"
print(greetings(name))
print(theme())
print(theme("dark")) #positional arguement
print(theme(selected="system")) #key based arguement
fontSize(13)
# fontSize(size=34) this fails due to ,/ in the parathensis
accentColor(color="blue")
# accentColor("red") this fails as only keyword is allowed
profile("Richard",24,bio="""I love programming
right now i am learning python
I'm polishing actually
             """,location="Nakuru")






print("\n===================*args **kwargs==============\n")
#*args used as arbitrary parameters when input arguements are not known and it saves them as tuple
def getMarks(*marks):
    my_list=list(marks)
    my_list.sort()
    print(f"The highest mark from {marks} is {my_list[-1]}")

getMarks(12,3,32,545,234,5,23,4)

#**kwargs used for arbitrary parameters, it saves the input as dictionary

def comment(**name):
    print(f"in as much as your name is {list(name.values())}")
    print(f"let's call you mr {name.get("surname")}")

comment(firstName="James",middleName="doe",surname="theodor")


#unpacking arguements
print("\n==============unpacking==================")
def adding(a,b,c):
   return a+b+c

nums=(23,54,2)
print("Unpacking the *args",adding(*nums))

def your_names(fname,mname,lname):
    print(f"first name is :{fname}\nmiddle name:{mname} \nlast name: {lname}")

person={"fname":"Rich","mname":"King","lname":"none"}
your_names(**person)