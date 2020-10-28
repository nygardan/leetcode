# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str):
        if len(needle) == 0:
            return 0
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            else: return -1
        if len(needle) > len(haystack):
            return -1

        for x in range(0, (len(haystack) - len(needle)+1)):
            comp_string = haystack[x:x+len(needle)]
            if comp_string == needle:
                return x
        return -1

# FINALLY succeeded on my 7th try with the above on 10-28-2020
# Also learned through the discussion about using "if needle in haystack:"
# instead of the above ('in' works on strings).
                       
            
                
                
