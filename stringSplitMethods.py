name="James"
name2="wandia"
statement = "this is a SIMPLE statement"
txt="For only {price:2f} dollars"
myDict=("this","is","a","sample","join")
mixed="y hdh 2323 hl"
x=name2.ljust(20)
print("Capitalize: ",name.capitalize())
print("casefold: ",statement.casefold())
print("center: ",name.center(20))
print("count: ",statement.count('t'))
print("encode: ",name.encode())
print("endswith: ",name.endswith('s'))
print("find: ",statement.find('a'))
print(txt.format(price=49))
print("index: ",statement.index("a"))
print("is alpha numerics: ",name.isalnum())
print("is alpha: ",name.isalpha())
print("joining: "," ".join(myDict))
print("lJust: ",x," testing ")
print("replace: ",statement.replace("statement","replaced"))
print("translate: ",name.translate({83:80}))