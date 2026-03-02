# range(start, stop, step)
x=range(0,10,2)
print("One arguement: ",list(x))
print("Two argurment: ",list(range(3,10)))
print("Three arguement: ",list(range(3,10,2)))

for i in x:
    print(i)

# slicing
print("slicing index 2: ",x[2])
print("slice end 3 : ",x[:3])

# checking membership
print("check if 3 is in x: ",3 in x)

# length
print("Length : ",len(x))