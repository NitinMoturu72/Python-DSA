# Minimum Window Substring

# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                
                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
# Brute Force Solution:
# We check if the required string is empty, if it is, we return an empty string. 
# We then create a dictionary to count the occurrences of each character in t. 
# We initialize a result variable to store the indices of the minimum window substring 
# and a variable to store the length of that substring. 
# We then iterate through each character in s and for each character, 
# we iterate through the remaining characters to check if we can form a valid substring that contains all characters from t. 
# If we find such a substring, we update our result and length variables accordingly. 
# Finally, we return the substring if found, otherwise an empty string.
# Time Complexity: O(n^2 * m), where n is the length of s and m is the length of t.
# Space Complexity: O(m), where m is the length of t, for the countT dictionary.