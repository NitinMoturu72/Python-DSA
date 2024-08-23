myList = ['a','b','c','d','e','f']
myList[0:2] = ['x','y']
print(myList[:])

 
myList.pop()
print(myList)

del myList[3]

print(myList)


myList.remove('e')

print(myList)


new_List = [10,20,30,40,50,60,70,80,90]

# In operator 

target = 500

if target in new_List:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")


# Linear Search

def linearSearch(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linearSearch(new_List, 90))

print('Concatenation')

a = [1,2,3]
b = [4,5]

c = a+b
print(c)

d = a * 5
print(d)

print('Length of a list')
print(len(a))

print('Max element of a list')
print(max(a))

print('Min element of a list')
print(min(a))

print('Sum of a list')
print(sum(a))


print('Exercise')

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)


data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")