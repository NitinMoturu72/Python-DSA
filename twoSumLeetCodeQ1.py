# Two Sum LeetCode Q1

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Brute force solution:
# Iterate through the array with two nested loops to check every pair of numbers.
# Return the indices of the two numbers that add up to the target.
# Time complexity O(n^2) 






def twoSum(nums, target):
        seen =  {}
        for i, value in enumerate(nums):
            reqnum = target - value
            if  reqnum in seen:
                return [seen[reqnum], i]
            else:
                seen[value] = i


print(twoSum([3,2,4], 6))

# HashMap solution:
# Use a dictionary to store the indices of the numbers as we iterate through the list.
# For each number, check if the complement (target - number) exists in the dictionary.
# If it does, return the indices of the current number and its complement.
# Else add the current number and its index to the dictionary.
# Time complexity O(n)  
# Space complexity O(n) as we store the indices in a new dictionary.