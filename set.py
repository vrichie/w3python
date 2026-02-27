myset = {"blue","green","black","black",True,1}
set1=set((1,2,3,4,5))
list1=list(("james","jane"))
print(set1)
print("Sets : ",myset)
print("Len : ",len(myset))

print("===============accessing============")
for i,t in enumerate(myset):
    print(i,t)

# checking it it exists
print("If blue exists : ","blue" in myset)
print("If red is not existing : ","red" not in myset)


print("==================add set items===============")
myset.add("red")
print("After adding red : ", myset)
set1.update(myset)
print("After updating set1 with set1 : ",set1)
print("List 1 : ",list1)
set1.update(list1)
print("After updating with the list : ", set1)

print("==================remove item=================")
set1.remove("black") #get's error incase the item is missing
print("after removing black : ",set1)
set1.discard("james") #no error incase  an item is missing
print("After removing james : ",set1)
removed_item=set1.pop() #removes a random element
print("After removing ",removed_item," : ",set1)
set1.clear()
print("Cleared the list : ",set1)
del set1
# print("Deleting the set : ",set1)


print("==================Joining the sets===============")
set1={"a","b","c","d"}
set2={1,2,3}
set1duplicate={"b","c"}
# union
set3= set1.union(set2)
print("Union : ",set3)
# multiple union
set4=set1.union(set2,set3)
print("Multi join : ",set4)
# union with a set
setUnion=set1.union(set1)
print("Join set + tuple : ",setUnion)
# update set
print("Before update : ",set1)
set1.update(set2)
print("After update : ",set2)
# intersection
setInter=set1.intersection(set1duplicate)
            # setInter = set1 & set1duplicate; same as intersection
print("Intersection : ",setInter)
# difference
setDiff=set1 - set1duplicate
print("Set difference : ",setDiff)
# symmetric difference








print("============================Frozenset====================")
x=frozenset({"eggs","peas","apples"})
print("Frozen set: ",x)
print("Type : ",type(x))