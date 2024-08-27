# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) 
# Output 90 87


# Time Complexity O(n^2)
def first_second(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    
    new_list.sort()
    return new_list[-1], new_list[-2]

print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))

# Time Complexity O(n)
def first_second1(my_list):
    max1 = 0
    max2 = 0 
    for i in my_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max1, max2 

print(first_second1([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))