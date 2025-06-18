# 238. Product of Array Except Self

# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_index = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_index.append(i)
                zero_count += 1
        # print(zero_index)
        if not (zero_index):
            res = [1] * len(nums)
            for i in range(len(res)):
                res[i] = int(product/nums[i])
        else:
            res = [0] * len(nums)
            if zero_count == 1:
                for i in zero_index:
                    res[i] = product
        return res

# Division:
# Calculate the product of all elements in the array. 
# If there are no zeros, divide the total product by each element to get the result. 
# If there is one zero, set the index of that zero to the total product, and all other indices to zero. 
# If there are two or more zeros, all indices will be zero.
# return the result array.
# Time complexity: O(n), where n is the length of the input array.
# Space complexity: O(n), since we are using a constant amount of extra space for variables.



def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1

    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

print(productExceptSelf([1,2,3,4]))

# Prefix & Postfix:
# This approach uses two passes through the array:
# 1. The first pass calculates the prefix product for each element.
# 2. The second pass calculates the postfix product and multiplies it with the prefix product to get the final result.
# # Time complexity: O(n), where n is the length of the input array.
# Space complexity: O(n), since we are using a constant amount of extra space for the 