# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :
# Input: nums = [1,2,3,1]
# Output: true

# Time Complexity O(n)
def contains_duplicate(nums):
    uniquelist = set()
    for i in nums:
        if i in uniquelist:
            return True
        else:
            uniquelist.add(i)
    return False


print(contains_duplicate([1,2,3,1]))