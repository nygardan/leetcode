class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }
        result, i = 0, 0
        while i < (len(s) - 1):
            if mapping[s[i + 1]] > mapping[s[i]]:
                result += (mapping[s[i + 1]] - mapping[s[i]])
                i += 2
            else:
                result += mapping[s[i]]
                i += 1
        
        if i >= len(s):
            return result
        else:
            return result + mapping[s[i]]
            
