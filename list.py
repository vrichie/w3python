fruits=["apple","Banana","cherry"] #ordered,
list2=list(("fruits","Food","party"))
num=[456,5,234,643,245,632,154,3,1]
biggerList= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(type(fruits))
# print(fruits)
# print(len(fruits))
# print(list2)


# accessing
# print(fruits[1])
# print(fruits[-1])
# print(fruits[::-1])
# print(biggerList)
# print(biggerList[:4])
# if "apple" in biggerList:
#     print("apples are present")

# changing elements
fruits[0]="updated"
list2[1:2]=["test"]
# print(fruits)
# print(list2)

# inserting
fruits.append("avocado")
fruits.insert(1,"pawpaw")
# print(fruits)

# extend the list with another
fruits2=["mangoes","peaches"]
fruits.extend(fruits2)
# print(fruits)

# remove items
fruits.remove("peaches")
# print(fruits)
fruits.pop(1) #removes the specified index
# print(fruits)
fruits.pop()  #removes the last item
# print(fruits)
del fruits[0] #works similar to pop with index
# print(fruits)
fruits.clear()
# print(fruits)

# looping a list
# for f in list2:
#     print(f)

# for i in range(len(list2)):
#     print(list2[i])

# i=0
# while i < len(list2):
#     print(list2[i]," index ",i)
#     i+=1


# list comprehension
# newlist=[]

# for x in list2:
#     if 's' in x:
#         newlist.append(x)
# newlist =[expression for item in iterable if condition == True]
newlist=   [x for x in list2 if 's' in x]

# print(newlist)

# sorting
# print(list2)
# list2.sort()
# print(list2)
# list2.sort(key=str.upper)
# print(list2)
# print(num)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)

# copying
newFruits=list2.copy()
newNum=list(num)
newNum1=num[:]
# print(newFruits)
# print(newNum)
# print(newNum1)

# joining
joinedList=num+list2
print(joinedList)