# Container With Most Water
# Solved 
# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                water = min(heights[i], heights[j]) * (j-i)
                # print(water, heights[i], heights[j])
                max_water = max(max_water,water)
        return max_water
    
# BruteForce Solution
# This solution uses two nested loops to check all pairs of bars in the array.
# It calculates the area of water that can be contained between each pair and keeps track of the maximum area found.
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l = 0
        r = len(heights) -1 
        
        while (l<r):
            water = (r-l) * min (heights[l], heights[r])
            max_water = max(max_water, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
    
# Two Pointer Solution
# This solution uses two pointers, one at the start and one at the end of the array.
# It calculates the area of water that can be contained between the two pointers.
# If the height at the left pointer is less than the height at the right pointer, it moves the left pointer to the right.
# Otherwise, it moves the right pointer to the left.
# This way, it ensures that it always considers the maximum possible width while trying to find a taller bar.
# Time Complexity: O(n)
# Space Complexity: O(1)