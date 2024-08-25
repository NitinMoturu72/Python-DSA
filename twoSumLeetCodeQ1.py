# Two Sum LeetCode Q1

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums, target):
        seen =  {}
        for i, value in enumerate(nums):
            reqnum = target - value
            if  reqnum in seen:
                return [seen[reqnum], i]
            else:
                seen[value] = i


print(twoSum([3,2,4], 6))