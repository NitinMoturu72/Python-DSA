# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict()
        l = 0

        r = 0

        length = 0
        longest = 0

        while(r<len(s)):
            if s[r] in m:
                l = max(m[s[r]]+1, l)
            m[s[r]] = r
            length = r - l + 1
            longest = max(longest, length)
            r += 1
        return longest
    

    # Sliding Window Approach:
    # We use a sliding window to keep track of the current substring without repeating characters.
    # We maintain a dictionary to store the last index of each character.
    # If we encounter a character that is already in the current substring, 
    # we move the left pointer of the window to the right of the last occurrence of that character 
    # or keep it there depending on whichever is greater.
    # We update the length of the longest substring found so far.
    # Time Complexity: O(n), where n is the length of the string s.
