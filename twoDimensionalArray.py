import numpy as np

twoArray = np.array([[11,12,13,14], [15,16,17,18], [19,20,21,22], [23,24,25,26]])
print(twoArray)


print("Insertion of elements")

newarr2 = np.insert(twoArray, 0, [[1,2,3,4]], axis = 0)
print(newarr2)

newarr3 = np.append(twoArray, [[1,2,3,4]], axis = 0)
print(newarr3)

print("Accessing an element of 2D Array")

def accessElements(array, r, c):
    if r >= len(array) and c >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[r][c])

accessElements(newarr2, 1, 2)

print("Traversing through 2d array")

def traversal2dArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversal2dArray(newarr2)

print("Searching a 2d Array")

def search2dArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value  is located at the index " +str(i)+ " "+ str(j)
    return "Element is not found"
            
print(search2dArray(newarr2, 20))

print("Deletion in 2d Array")

new2darr = np.delete(newarr2, 0, axis=0)
print(new2darr)