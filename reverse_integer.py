# Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        if x <= -2**31 or x >= 2**31-1:
            return 0
        else:
            rstring = str(x)
            if rstring[0] == '-':
                r = int(rstring[:0:-1]) * -1
            else:    
                rint = int(rstring[::-1])
            if rint <= -2**31 or rint >= 2**31-1:
                return 0
            else: return rint
