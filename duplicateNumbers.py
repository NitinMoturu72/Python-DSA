# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

# Time Complexity O(n)
def remove_duplicates(arr):
    seen = []
    for i in arr:
        if i not in seen:
            seen.append(i)
    return seen