# Longest Consecutive Sequence

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9

def longestConsecutive(self, nums: List[int]) -> int:   
    if len(nums) == 0:
            return 0
    s = set()
    for i in nums:
        if i not in s:
            s.add(i)
    l = list(s)
    print(s)
    l.sort()
    print(l)
    max_count = 1
    count = 1
    for i in range(len(l)-1):
        if l[i+1] == l[i] +1:
            print(l[i], l[i+1])
            count += 1
            print(count)

        else:
            print("reseting here" + str(i))
            max_count = max(max_count, count)
            count = 1
        max_count = max(max_count, count)
    return max_count


# Sorting:
# if the length of the array is 0, return 0.
# create a set to store unique elements, to avoid duplicates.
# now have max count and count both set to 1.
# for each element in the sorted list, check if the next element is equal to the current element + 1. increment count if it is, else reset count to 1.
# finally return the max count.
# Time Complexity: O(n log n) due to sorting, where n is the number of unique elements in the input list.
# Space Complexity: O(n) for the set to store unique elements.