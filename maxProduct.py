# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example
# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) 
# Output: 63 (9*7)


# Time complexity is O(n^2)
def max_product1(arr):
    product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = max(product, arr[i]*arr[j])
    return product
        
print(max_product1([1,7,3,4,9,5]))

# Time complexity is O(nlogn)
def max_product2(arr):
    arr.sort()
    return arr[-1] * arr[-2]

print(max_product2([1,7,3,4,9,5]))

# Time complexity is O(n)
def max_product3(arr):
    max1 , max2 = 0 , 0 
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max1 * max2

print(max_product3([1,7,3,4,9,5]))