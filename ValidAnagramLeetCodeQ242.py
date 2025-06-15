# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if i not in t:
                return False
            else:
                t = t.replace(i, "", 1)
        return True

# Brute Force: If length of s and t are not equal, they cannot be anagrams.
# If all characters in s are found in t, we remove them one by one from t.
# If we can remove all characters from s, then t is an anagram of s.
# Time complexity: O(N^2), where N is the length of the string.
# Space complexity: O(1), since we are not using any extra space that grows with input size.

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

# Sorting: If length of s and t are not equal, they cannot be anagrams.
# If we sort both strings and they are equal, then t is an anagram of s.  
# Time complexity: O(N log N), where N is the length of the string.
# Space complexity: O(1), since we are not using any extra space that grows with input size.  



def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for  c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True


# HashMap: If length of s and t are not equal, they cannot be anagrams.
# We use a hashmap to count the frequency of each character in both strings.
# If the frequency of each character in s matches the frequency in t, then t is an anagram of s.
# Time complexity: O(N), where N is the length of the string.
# Space complexity: O(N), since we are using a 2 hashmap of size N.