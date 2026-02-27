tuples=("apple","banana","cherry")
otherTuple=tuple((23,"new","test data"))
# print(type(tuples),tuples,len(tuples))
notTuple=("apples")
# print(type(notTuple),notTuple,len(notTuple))
temp=list(tuples)
temp[1]="kiwi"
# print(tuples[2])
temp.append("mangoes")

# print(tuple(temp))

# packing tuple
fruits = ("yes","no","maybe")
languages = ("py","ts","js","css","Html")
# unpacking
(a,b,c) = fruits
(x,*y,z) = languages
# print(a,b,c)
# print(x,y,z)
print("==============Enumerate============")
for i,f in enumerate(fruits):
    print(i,f)

print("=============For Loop=============")
for i in range(len(languages)):
    print(languages[i])

print("==============While loop=============")
i=0
while i<len(fruits):
    print(i,fruits[i])
    i+=1

print("===============Join tuples============")
tuple3=fruits+languages
print("Joining two : ",tuple3)
multTuple = fruits *3
print("Multiply by 2 : ",multTuple)


print("=================Tuple methods==============")
print("count : ",multTuple.count("yes"))
print("index : ",multTuple.index("yes"))