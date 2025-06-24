# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    print([nums[i], nums[j], nums[k]])
                    if nums[i]+nums[j]+nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
        return res
    

# BruteForce Solution
# This solution uses three nested loops to check all combinations of triplets in the array.
# It checks if the sum of the triplet is zero and ensures that the triplet is not already in the result list to avoid duplicates.
# Time Complexity: O(n^3)
# Space Complexity: O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                # print(i,l,r)
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
        return res


# 2 Pointers:
# This solution uses a two-pointer technique after sorting the array.
# It iterates through the array and uses two pointers to find pairs that, together with the current element, sum to zero.
# We skip duplicates to ensure unique triplets by checking if the current element is the same as the previous one while iterating.
# while the left pointer is less than the right pointer, it checks the sum of the triplet.
# if the sum is zero, it adds the triplet to the result and moves both pointers inward(left) while skipping duplicates.
# if the sum is less than zero, it moves the left pointer to the right to increase the sum.
# if the sum is greater than zero, it moves the right pointer to the left to decrease the sum.
# returns the list of unique triplets that sum to zero.
# Time Complexity: O(n^2)
# Space Complexity: O(n)