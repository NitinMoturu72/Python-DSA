# Encode and Decode Strings

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

def encode( strs):
    res = ""
    for i in strs:
        res += str(len(i)) + "#" + i
    # print(res)
    return res

def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        word_length = int(s[i:j])
        word = s[j+1 : j+1+word_length]
        res.append(word)
        i = j + 1 + word_length
    return res

print(decode(encode(["we","say",":","yes","!@#$%^&*()"])))


# Encode: 
# Iterate through each string in the list, concatenate its length and a delimiter '#' with the string itself, and return the concatenated result.
# Decode:
# Iterate through the encoded string, extract the length of each word using the delimiter '#', and then extract the word based on that length, appending each word to a result list.
# Time Complexity: O(n), where n is the total number of characters in the input strings and the encoded string.
# Space Complexity: O(n), where n is the total number of characters in the input strings