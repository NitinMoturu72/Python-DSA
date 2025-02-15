A= [7,2,3,3,4,9]

b= []
max1 = A[0]
max2 = A[1]
max3 = A[2]
string = str(A[0]) + str(A[1]) + str(A[2])
print(string)
for i in A[3:]:
    if i > max1:
        max3 = max2
        max2= max1
        max1 = i
        b.append(A.index(i))
    elif i < max1 and i > max2:
        max3 = max2
        max2 = i
        b.append(i)
    elif i<max2 and i>max3:
        max3 =i
        b.append(i)
sum = max3*100 + max2*10 + max1
print(A.index(max1))
print(max1,max2,max3)