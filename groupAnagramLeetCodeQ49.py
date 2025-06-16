# Group Anagrams

# Solved 

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_arr = {}
        for i in strs:
            sort_str = "".join(sorted(i))
            if sort_str in sort_arr:
                # print(sort_arr[sort_str])
                sort_arr[sort_str].append(i)
                # print(sort_arr)
            else:
                sort_arr[sort_str] = []
                sort_arr[sort_str].append(i)
        # print(sort_arr)
        final = []
        for i in sort_arr:
            final.append(sort_arr[i])
        # print(final)
        return final

# Sorting:
# Sort each string in the input list and use the sorted string as a key in a dictionary.
# If the sorted string already exists in the dictionary, append the original string to the list of anagrams.
# If it does not exist, create a new entry in the dictionary with the sorted string as the key and the original string as the first element of the list.
# Finally, return the values of the dictionary as a list of lists. 
# Time complexity O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space complexity O(n * k) for storing the anagrams in the dictionary.


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_Map = defaultdict(list)

        for i in strs:
            key = tuple(sorted(i))
            anagram_Map[key].append(i)

        return list(anagram_Map.values())

# Defaultdict solution:
# Use a defaultdict to store lists of anagrams. 
# For each string, sort it to create a key and append the original string to the list corresponding to that key.
# Finally, return the values of the defaultdict as a list of lists. 
# Time complexity O(n * k log k) where n is the number of strings and k is the maximum length of a string.
# Space complexity O(n * k) for storing the anagrams in the defaultdict.


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_Map = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c)-ord("a")] += 1
            
            key = tuple(count)
            anagram_Map[key].append(i)

        return list(anagram_Map.values())

# Count solution:
# Use a defaultdict to store lists of anagrams.
# For each string, create a count of characters (using a list of size 26 for lowercase letters) and use it as a key.
# Append the original string to the list corresponding to that key. 
# Finally, return the values of the defaultdict as a list of lists.
# Time complexity O(n * k) where n is the number of strings and k is the maximum length of a string.
# Space complexity O(n * k) for storing the anagrams in the defaultdict.