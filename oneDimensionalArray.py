from array import *

arr1 = array('i', [1,2,3,4,5])
print("Creating an Array and traversing")

for i in arr1:
    print(i)

print("Accessing individual elements through indexes")

for i in range(len(arr1)):
    print(arr1[i])

print("Appending any value of the array using append()")

arr1.append(6)
print(arr1)

print("Insert element using insert()")

arr1.insert(0,11)
print(arr1)

print("Extend array using extend()")

arr2 = array('i', [10,11,12])
arr1.extend(arr2)
print(arr1)

print("Add items from list into array using fromlist()")

tempList = [20,21,22]
arr1.fromlist(tempList)
print(arr1)

print("Remove element using remove()")

arr1.remove(11)
print(arr1)

print("Remove last array element using pop() method")

arr1.pop()
print(arr1)

print("Fetch any element through its index using index()")

print(arr1.index(11))

print("Reverse an array using reverse()")

arr1.reverse()
print(arr1)

print("Buffer information using buffer_info()")

print(arr1.buffer_info())

print("Number of occurances of an element using count()")

arr1.append(11)
print(arr1.count(11))

# print("Convert array to string using tostring()")

# strtemp = arr1.tostring()
# intstring = array('i')
# intstring.fromstring(strtemp)
# print(intstring)

print("Convert array into list using tolist()")

print(arr1.tolist())

print("Slice elements from an array")
print(arr1[1:4])
