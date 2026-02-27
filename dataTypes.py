"""
"""
# String
name = "  John Ndirangu  "
a="Hello"
b="World"
print(f"name = {name}, length = {len(name)} type = {type(name)}")
# print(name[1])
############## slicing
print(name[2:5])
print(name[:5])
print(name[2:])
print(name[-5:-2])
############## string modification
print(name.upper())
print(name.lower())
print(name.strip())
print(name.split(" "))
############## string concatenation
print(a+b)
############# Escape characters
print("This is the \' you who \'")

# for l in name:
#     print(l)

#multiline string
bio = """This is a
multiline string
it spans across multiple lines"""
# print(bio)
# print("it" in bio)
# if ("it" in bio):
#     print(" it is present")
# if ("java" not in bio):
#     print("Java is not present")



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# numerical
numInt=19
numFloat=1.4
numComplex=1j
# print(f"numInt = {numInt} , type = {type(numInt)}")
# print(f"numInt = {numFloat} , type = {type(numFloat)}")
# print(f"numInt = {numComplex} , type = {type(numComplex)}")

#Boolean
isActive = True

#bytes
by = bytes(4)
byteArray = bytearray(6)
# print(f"byte: {by}, type = {type(by)}")
# print(f"ByteArray: {byteArray}, type = {type(byteArray)}")

#memoryview
mmview = memoryview(by)
# print(f"Memory view = {mmview}, type = {type(by)}")

# sequence types
listFruits = ["apples","berry","cherry"] #lists
tupleFruits = ("apples","berry","cherry") #tuple
rangeNum = range(5)
# print("List of fruits: ",listFruits)
# print("Tuple of fruits: ",tupleFruits)
# print("Range of numbers: ",rangeNum)

# Mapping type
dictStudent = {"name":"John","age":35,"grade":'A'}
# print(f"Student dictionary : {dictStudent} , type : {type(dictStudent)}")

# sets
setFruits = {"apples","berry","cherry"}
frozenSetFruits = frozenset({"apples","berry","cherry"})
# print("Set of fruits : ",setFruits)
# print("Frozen set of fruits : ",frozenSetFruits)