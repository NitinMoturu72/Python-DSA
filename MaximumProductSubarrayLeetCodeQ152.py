# 152. Maximum Product Subarray

# Medium

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


def maxProduct(nums):
    res = max(nums)
    max_prd, min_prd = 1,1

    for i in nums:
        tmp = i* max_prd
        max_prd = max(i*max_prd, i*min_prd, i)
        min_prd = min(tmp, i*min_prd, i)
        res = max(max_prd, min_prd, res)

    return res

print(maxProduct([2,3,-2,4]))
