# Valid Palindrome

# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        left = 0
        right = len(s)-1
        while (left < right):
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    

# 2 pointers:
# Remove all non-alphanumeric characters from the string. 
# Initialize two pointers, one at the start (left) and one at the end (right) of the string.
# Compare characters from both ends of the string, moving towards the center.
# if the characters at the two pointers are not equal, return False.
# If all characters match, return True.
# Time Complexity: O(n)
# Space Complexity: O(1) if we ignore the space used by the regex operation, otherwise O(n) for the new string created by re.sub.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while (left < right):
            while left < right and not self.check(s[left]):
                left += 1
            
            while left < right and not self.check(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def check (self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
# 2 pointers:
# Create a helper function to check if a character is alphanumeric.
# The aplhanumeric characters are defined as letters (A-Z, a-z) and numbers (0-9). 
# The helper function checks if the character falls within the ASCII range of alphanumeric characters.
# Initialize two pointers, one at the start (left) and one at the end (right) of the string.
# Move the left pointer to the right until it points to an alphanumeric character.  
# Move the right pointer to the left until it points to an alphanumeric character.
# Compare characters from both ends of the string, moving towards the center.
# If the characters at the two pointers are not equal, return False.
# If all characters match, return True.
# Time Complexity: O(n)
# Space Complexity: O(1) since we are not using any extra space for the string.