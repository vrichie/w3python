i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
else:
    print(" loop is done")

fruits=["apple","berry","cherry","dates","egg fruit"]
for fruit in fruits:
    if fruit=="dates":
        # break
        continue
    print(fruit)