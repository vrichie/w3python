import random


x = 5       #int
y= "John"   #string
z = 3.0
print(x)
print(y)

#Casting
r = str(3)
t = int(5)
u = float(8)

print(r,t,u)
print(type(r),type(t),type(u))

R = "case sensitivity"
print(f"R = {R} is not equal to r = {r}")

# naming styles
camelCase="Camel Case naming styles";
PascalCase="Pascal Case naming style";
snake_case="Snake case naming style"

# Multiple variables
x=y=z= "orange"
print(x)
print(y)
print(z)
fruits = ["apple","banana","cherry"];
f1,f2,f3=fruits;
print(f1)
print(f2)
print(f3)

# random numbers
print(random.randrange(1,10))