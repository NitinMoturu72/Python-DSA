# Valid Parentheses

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"}":"{", "]":"[", ")":"("}

        for i in range(len(s)):
            if s[i] in m:

                if stack and stack[-1] == m[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            
        return True if not stack else False
    

# Stack Solution:
# We use a dictionary to map closing brackets to their corresponding opening brackets.
# We use a stack to keep track of the opening brackets. 
# When we encounter a closing bracket, we check if it matches the top of the stack. 
# If it does, we pop the stack; if not, we return False. 
# At the end, if the stack is empty, it means all brackets were matched correctly.
# We return True if the stack is empty, otherwise False.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for the stack in the worst case when all characters are opening