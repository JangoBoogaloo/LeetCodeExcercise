class Solution:
    def isValid(self, s: str) -> bool:
        openBracketStack = []
        openBracketTypes = {"{", "[", "("}
        bracketMap = {"}": "{", "]": "[", ")": "("}
        for ch in s:
            if ch in openBracketTypes:
                openBracketStack.append(ch)
            elif openBracketStack and bracketMap[ch] == openBracketStack[-1]:
                openBracketStack.pop()
            else:
                return False
        return not openBracketStack
