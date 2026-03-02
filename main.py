import mymodule as mm
import platform


print("Platform : ",platform.system())
x=dir(platform)
print("x",x)
mm.greeting("Richard")
name=mm.person["name"]
print("Name : ",name)