integers = [1,2,3,4]
stringlist = ['Milk', 'Cheese', 'Butter']
mixlist = [1, 1.5, 'spam']
nestedlist = [1,2,4,5,[1,2,3]]

print(integers)
print(stringlist)
print(mixlist)
print(nestedlist)

print("Traversing the list")

shoppinglist = ['Milk','Cheese','Butter']

for i in shoppinglist:
    print(i)

for i in range(len(shoppinglist)):
    shoppinglist[i] = shoppinglist[i] + "+"
    print(shoppinglist[i])

print("Accessing elements")

print(shoppinglist[-1])


print("Update / Insert in list")

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)

print("Insertion of Elements")

myList.insert(0,11)
print(myList)


myList.append(55)
print(myList)

myList.extend([1,2,3,4])
print(myList)
