# Search in Rotated Sorted Array

# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

# You may assume all elements in the sorted rotated array nums are unique,

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:

# Input: nums = [3,4,5,6,1,2], target = 1

# Output: 4
# Example 2:

# Input: nums = [3,5,6,0,1,2], target = 4

# Output: -1
# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -1000 <= target <= 1000


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (r >= l):
            mid = (r+l)//2
            print(mid, l, r)

            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid -1
        
        return  -1

# Binary Search Solution:
# We use binary search to find the target in the rotated sorted array. 
# The key is to determine which half of the array is sorted 
# Then decide whether to search in that half or the other half based on the target value.
# We return the index of the target if found, otherwise -1.
# The time complexity is O(log n) due to the binary search approach.    
# The space complexity is O(1) since we are using a constant amount of space.