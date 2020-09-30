# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        left_list = []
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        for symbol in s:
            try:
                if symbol == '(' or symbol == '[' or symbol == '{':
                    left_list.append(symbol)
                elif symbol == ')':
                    if left_list.pop() != '(': return False
                elif symbol == ']':
                    if left_list.pop() != '[': return False
                elif symbol == '}':
                    if left_list.pop() != '{': return False
            except:
                return False
        if len(left_list) != 0:
            return False
        else:
            return True
            
                
                
