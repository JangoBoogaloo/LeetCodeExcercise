class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {'(', '[', '{'}
        close = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in opens:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif close[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
