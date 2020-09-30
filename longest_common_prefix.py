#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ""
        if len(strs) > 0:
            res = min(len(ele) for ele in strs)
        else:
            return prefix
        for i in range(res):
            letter = strs[0][i]
            for string in strs:
                if string[i] != letter:
                    return prefix
                else:
                    continue
            prefix += letter
        
        return prefix
