dict1={
    "name":"james",
    "age":23,
}
person={
"name":"Richard Kinyua",
"age":24,
"nationality":"kenyan"
}
print("Dictionary : ",dict1)
# print("Name : ",dict1["name"])
print("length : ",len(dict1))
print("type : ",type(dict1))


print("\n=============accessing elements===============\n")
#normal way using key
print("Get name : ",dict1["name"])#gives error if the key does not exist
# using the get method
print("Get age : ",dict1.get("age"))# better incase no key exists no error
#get all the keys
print("Get all the keys before : ",dict1.keys())
dict1["newKey"]="new"
print("Get all the keys after : ",dict1.keys())

#get all the values
print("Get all the values before : ",dict1.values())
dict1["marks"]=59
print("Get all the values after : ",dict1.values())

#get items method
print("Get all items before: ",dict1.items())
dict1["grade"]='A'
print("Get all the items after : ",dict1.items())


# check if a ket exists
if "age" in dict1:
    print("age is in the dict1")


# modifying a value
print("Age before : ",dict1["age"])
dict1["age"]=56
print("After update : ",dict1["age"])
# using update
print("Original dict : ",dict1)
dict1.update({"name":"Rich"})
print("After update : ",dict1)

#removing and item
dict1.pop("age")
print("After pop age : ",dict1)
dict1.popitem()
print("After popItem : ",dict1)
# del
del dict1["marks"]
# del dict1---this deletes the entire dict
print("After deleting the marks : ",dict1)
#clear
dict1.clear()
print("After clearing : ",dict1)


print("\n==================looping===============\n")
for x in person:
    print("key:",x)
    print("value:",person[x],"\n")

#getting all the values
for x in person.values():
    print(x)

#gettind all the keys
for k in person.keys():
    print(k)

#getting all the items
for x,y in person.items():
    print("key, value : ",x,y)



print("\n==================copy=================\n")
copy_of_dict = person.copy()
copy_of_dict2 =dict(person)
print("Copy of person : ",copy_of_dict)
print("Copy 2 of person : ",copy_of_dict2)


print("\n===================nested dict==============")
child1={"name":"jake","age":12}
child2={"name":"jane","age":23}
child3={"name":"Julie","age":26}
children={"child1":child1,"child2":child2,"child3":child3}
print("Nested dict : ",children)
print("Name of second child : ",children["child2"]["name"])