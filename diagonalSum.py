# 2D Lists
# Given 2D list calculate the sum of diagonal elements.

# Example
# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

# diagonal_sum(myList2D) 
# Output 15

# Time complexity is O(n^2)
def diagonal_sum(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum += matrix[i][j]
    return sum

print(diagonal_sum([[1,2,3], [4,5,6], [7,8,9]]))

# Time complexity is O(n)
def diagonal_sum2(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

print(diagonal_sum2([[1,2,3], [4,5,6], [7,8,9]]))
