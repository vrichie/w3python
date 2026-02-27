a=23
b=238
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("a is less than b")


#validate username
username="james"
if len(username)>0:
    print(f" welcome {username}")
else:
    print("Enter the username")


#shorthand if
if a>b : print("a is greater")

# shorthand if else
print("a is equal to b") if a==b else print("Not equal")

#shorthand if else while assigning
bigger=a if a>b else b
print("The bigger number is ",bigger)


# chaining conditions
is_weekend=False
is_raining=True
temp=34

if (not is_raining and temp>20) or is_weekend:
    print("Go out")
else:
    # print("Not today")
    pass