# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        seen = dict(sorted(seen.items(), key= lambda item: item[1], reverse = True))
        
        # print(seen)
        final = []
        for i in seen:
            final.append(i)
        return final[0:k]

# Brute force solution:
# Count the frequency of each element in the array using a dictionary.
# Sort the dictionary by frequency in descending order.
# Extract the keys of the sorted dictionary and return the first k elements.
# Time complexity O(n log n) due to sorting, where n is the number of distinct elements in nums.
# Space complexity O(n) for storing the frequency count in a dictionary.


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =[[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        # print(count)
        for i, c in count.items():
            freq[c].append(i)
        
        res =[]
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                
# Bucket sort solution:
# Count the frequency of each element in the array using a dictionary.
# Create a list of empty lists (buckets) where the index represents the frequency. This will ensure the size of the list is len(nums) + 1.
# For each unique element, append it to the corresponding bucket based on its frequency.
# Iterate through the buckets in reverse order and collect elements until we have k elements.
# Time complexity O(n), where n is the number of elements in nums.
# Space complexity O(n) for storing the frequency count in a dictionary and the buckets.  
