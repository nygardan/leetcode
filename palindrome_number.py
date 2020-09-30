# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
# -121 would be false because backward it is 121-

# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else: return False

# Solved 9/29/2020 with no help from 'Discussion' or 'Solution'.
