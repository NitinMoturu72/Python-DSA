# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList) 
# Output [2,3]

# Time complexity O(n-1) => O(n)
def middle(lst):
    lst.pop(0)
    lst.pop(-1)
    return lst

print(middle([1,2,3,4,5]))

# Time complexity O(n)
def middle2(lst):
    return lst[1:-1]

print(middle2([1,2,3,4,5]))