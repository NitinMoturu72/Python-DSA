# Longest Repeating Character Replacement

# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = [0]*26
        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1

            while ((r-l+1) - max(count) > k):
                count[ord(s[l]) - 65] -= 1
                l += 1
            longest = max(longest, (r-l+1))
        return longest
    

# Sliding Window Approach:
# The idea is to maintain a sliding window that contains the longest substring with at most k replacements.
# We use two pointers, l and r, to represent the left and right ends of the window.
# We also maintain a count array to keep track of the frequency of each character in the current window.
# As we expand the right pointer r, we update the count of the current character.
# If the size of the window minus the maximum frequency of any character in the window exceeds k, we shrink the window from the left by moving l to the right.
# We also reduce the count of the character at the left pointer as we move it.
# Finally, we update the longest substring length found so far.
# Time complexity is O(n) where n is the length of the string s
# Space complexity is O(1) since the count array has a fixed size of 26 (for uppercase English letters).